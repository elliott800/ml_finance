import pytest
from datetime import datetime, timezone
from ml_finance.broker_api import oanda_api


def test_invert_bid_ask_success():
    api = oanda_api(api_token="T", account_id="A")
    b, a = api._invert_bid_ask(1.1, 1.2)
    assert pytest.approx(b, rel=1e-9) == 1.0 / 1.2
    assert pytest.approx(a, rel=1e-9) == 1.0 / 1.1


def test_invert_bid_ask_invalid():
    api = oanda_api(api_token="T", account_id="A")
    with pytest.raises(ValueError):
        api._invert_bid_ask(0.0, 1.0)


def test_percent_to_units_with_scale_and_default():
    api = oanda_api(api_token="T", account_id="A")
    # explicit scale
    assert api._percent_to_units(10, scale=1000) == pytest.approx(100.0)
    # default scale from internal setting
    api["_orderbook_scale"] = 2000000.0
    assert api._percent_to_units(1) == pytest.approx(20000.0)


def test_to_rfc3339_naive_and_aware():
    api = oanda_api(api_token="T", account_id="A")
    # naive datetime should be treated as UTC
    dt = datetime(2020, 1, 2, 3, 4, 5)
    s = api._to_rfc3339(dt)
    assert s.startswith("2020-01-02T03:04:05") and s.endswith("Z")

    # aware datetime in other tz is converted to UTC
    aware = datetime(2020, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    s2 = api._to_rfc3339(aware)
    assert s2 == "2020-01-02T03:04:05Z"


def test_get_precisions_fallbacks():
    api = oanda_api(api_token="T", account_id="A")
    # JPY instrument fallback
    disp, tick, pip = api._get_precisions("USD_JPY")
    assert (disp, tick, pip) == (3, 0.001, 0.01)
    # default fallback
    disp2, tick2, pip2 = api._get_precisions("EUR_USD")
    assert (disp2, tick2, pip2) == (5, 0.00001, 0.0001)


def test_is_maintenance_error_cases():
    api = oanda_api(api_token="T", account_id="A")
    # status code 503 -> maintenance
    assert api._is_maintenance_error(None, response_text=None, status_code=503)
    # error message contains maintenance
    assert api._is_maintenance_error(
        Exception("Maintenance window"), response_text=None, status_code=None
    )
    # response_text indicates service unavailable
    assert api._is_maintenance_error(
        None, response_text="Service Unavailable", status_code=None
    )
    # non-maintenance
    assert not api._is_maintenance_error(
        Exception("other error"), response_text="all good", status_code=200
    )


def test_position_inventory_and_nav_and_pl():
    api = oanda_api(api_token="T", account_id="A")

    # monkeypatch get_position_list to return predictable trades
    def fake_positions():
        return [
            {
                "id": "t1",
                "instrument": "EUR_USD",
                "currentUnits": "100",
                "unrealizedPL": "5",
                "marginUsed": "10",
                "price": "1.1",
                "openTime": "now",
            },
            {
                "id": "t2",
                "instrument": "EUR_USD",
                "currentUnits": "-50",
                "unrealizedPL": "-2",
                "marginUsed": "4",
                "price": "1.2",
                "openTime": "now",
            },
        ]

    api.get_position_list = fake_positions
    positions = api.get_positions()
    assert isinstance(positions, list)
    instr_positions = api.get_instrument_positions("EUR_USD")
    assert len(instr_positions) == 2
    inventory = api.get_instrument_inventory("EUR_USD")
    # units are summed as int(100) + int(-50) = 50
    assert inventory == 50
    pl = api.get_pl()
    assert pl == pytest.approx(3.0)
    # balance fallback is 100000.0 so nav = 100000 + pl
    nav = api.get_nav()
    assert nav == pytest.approx(100000.0 + 3.0)
