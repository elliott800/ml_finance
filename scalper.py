#scalper.py
from broker_api import *
last_order_refresh=now()
distance=1
trade_units=1000
refresh=60*60
api=oanda_api("","")
instruments=list(api._load_tradable_instruments())
def find_place_value(value):
    # Convert the value to string to check where the decimal point is
    value_str = str(value)
    # Split the string at the decimal point
    if '.' in value_str:
        integer_part, decimal_part = value_str.split('.')
        place_value = len(decimal_part)

        return place_value
    else:
        return 0  # No decimal part
while True:#trade loop
    for instrument_name in instruments:
        asset=api.get_candle_history(instrument_name,'M1',500)
        close=asset.close
        disp,tck,pip=api._get_precisions(instrument_name)
        place_value=find_place_value(pip)
        margin_used=api.get_instrument_margin_used(instrument_name)
        inventory=api.get_instrument_inventory(instrument_name)
        bu=api.get_total_pending_buy_units(instrument_name)
        au=api.get_total_pending_sell_units(instrument_name)
        bid_price=round(close.iloc[-1]-distance*pip,place_value)
        ask_price=round(close.iloc[-1]+distance*pip,place_value)
        net=np.floor(au-inventory-bu)#critical mm equation
        even_entry_required=True
        if inventory==0 and bu==0 and au==0:
            even_entry_required=False
            api.buy(instrument_name,trade_units,bid_price);api.sell(instrument_name,trade_units,ask_price)
        if net==0:
            test_units=abs(inventory+bu-au+trade_units)
        else:
            test_units=abs(inventory+bu-au+net)
        if margin_used<10:#critical mm equation
            if net==0 and even_entry_required:api.buy(instrument_name,trade_units,bid_price);api.sell(instrument_name,trade_units,ask_price)#disable to slow down
            if net>0:api.buy(instrument_name,net,bid_price)
            if net<0:api.sell(instrument_name,net,ask_price)
        if now()-last_order_refresh>refresh:
            last_order_refresh=now()
            api.cancel_instrument_orders(instrument_name)
