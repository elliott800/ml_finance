#oanda_lite.py
#authors cline, Elliott Hamilton
from oandapyV20 import API
import oandapyV20.endpoints.orders as oanda_orders
import oandapyV20.endpoints.trades as oanda_trades
from oandapyV20.exceptions import V20Error
import oandapyV20.endpoints.instruments as oanda_instruments
import oandapyV20.endpoints as endpoints
import logging
import math
import requests
from time import sleep
import oandapyV20.endpoints.transactions as oanda_transactions
import oandapyV20.endpoints.pricing as oanda_pricing
import threading
import csv
import os
from datetime import datetime, timezone, timedelta
#get_balance(self)
#get_pl(self)
#get_nav(self)
#
#
#
#
#
class oanda_lite(dict):
    def __init__(self,api_token="",account_id=""):
        self['api_token']=api_token
        self['account_id']=account_id
        self['api']=API(access_token=api_token)
        self._install_maintenance_wrappers()

    def _is_maintenance_error(self, err, response_text=None, status_code=None):
        try:
            msg = str(err).lower() if err is not None else ""
        except Exception:
            msg = ""
        text = (response_text or "").lower()
        if status_code == 503:
            return True
        if ('maintenance' in msg) or ('service unavailable' in msg) or ('503' in msg):
            return True
        if ('maintenance' in text) or ('service unavailable' in text):
            return True
        return False

    def _install_maintenance_wrappers(self):
        # Wrap oandapyV20 API.request to auto-handle maintenance by retrying
        try:
            original_request = self['api'].request
        except Exception:
            return
        def maintenance_request(r):
            while True:
                try:
                    return original_request(r)
                except V20Error as e:
                    if self._is_maintenance_error(e):
                        print(f"OANDA maintenance detected; retrying in 30 seconds. Error: {e}")
                        sleep(30)
                        continue
                    raise
        self['api'].request = maintenance_request

    def get_balance(self):
        try:
            import oandapyV20.endpoints.accounts as oanda_accounts
            r = oanda_accounts.AccountDetails(accountID=self['account_id'])
            rv = self['api'].request(r)
            return float(rv['account']['balance'])
        except Exception:
            # Fallback for offline/sandbox run
            return 100000.0
    
    def get_pl(self):
        try:
            trades = self.get_position_list()
            pl = 0.0
            for trade in trades:
                try:
                    pl += float(trade.get('unrealizedPL', 0.0))
                except Exception:
                    pass
            return pl
        except Exception:
            return 0.0
    
    def get_nav(self):
        balance=self.get_balance()
        pl=self.get_pl()
        nav=balance+pl
        return nav

    def get_positions(self):
        #user function
        trades=self.get_position_list()
        positions=[]
        for trade in trades:
            position_info={}
            position_info['id']=trade['id']
            position_info['instrument']=trade['instrument']
            position_info['units']=trade['currentUnits']
            position_info['pl']=trade['unrealizedPL']
            position_info['margin_used']=trade['marginUsed']
            position_info['price']=trade['price']
            position_info['time']=trade['openTime']
            positions.append(position_info)
        self['positions']=positions
        return self['positions']

    def get_instrument_positions(self,instrument='EUR_USD'):
        #user function
        positions=self.get_positions()
        instrument_positions=[]
        for position in positions:
            if position['instrument']==instrument:
                instrument_positions.append(position)
        return instrument_positions

    def get_instrument_inventory(self,name):
        total_units=0
        for each in self.get_instrument_positions(name):
            total_units+=int(each['units'])
        return total_units

    def _get_precisions(self, instrument):
        """
        Return (display_precision, tick_size, pip_size) for the instrument using OANDA metadata.
        Fallbacks:
          - JPY quotes: tick=0.001, pip=0.01
          - Others: tick=0.00001, pip=0.0001
        """
        try:
            import oandapyV20.endpoints.accounts as oanda_accounts
            instr = str(instrument).upper().replace('-', '_').strip()
            params = {'instruments': instr}
            r = oanda_accounts.AccountInstruments(accountID=self['account_id'], params=params)
            response = self['api'].request(r)
            instruments = response.get('instruments', [])
            if instruments:
                meta = instruments[0]
                display_precision = int(meta.get('displayPrecision', 5))
                pip_location = int(meta.get('pipLocation', -4))
                tick = 10 ** (-display_precision)
                pip = 10 ** (pip_location)
                return display_precision, float(tick), float(pip)
        except Exception:
            pass
        instr = str(instrument).upper()
        if instr.endswith('_JPY'):
            return 3, 0.001, 0.01
        return 5, 0.00001, 0.0001

    def get_orders(self):
        r = oanda_orders.OrdersPending(accountID=self['account_id'])
        rv = self['api'].request(r)
        return rv['orders']

    def get_instrument_orders(self,instrument='EUR_USD'):
        orders=self.get_orders()
        instrument_orders=[]
        for order in orders:
            if order['instrument']==instrument:
                instrument_orders.append(order)
        return instrument_orders

    def list_pending_orders(self, instrument=None, include_attached=True):
        """
        List pending orders, optionally filtered by instrument.
        Returns list of dicts: {'id','instrument','type','tradeID'}
        """
        out = []
        try:
            # Gather pending orders from OrdersList(state=PENDING) and OrdersPending, then union by id
            pend = []
            try:
                params = {'state': 'PENDING', 'count': 500}
                r1 = oanda_orders.OrdersList(accountID=self['account_id'], params=params)
                rv1 = self['api'].request(r1)
                pend = rv1.get('orders', []) if isinstance(rv1, dict) else []
            except Exception:
                pend = []
            try:
                r2 = oanda_orders.OrdersPending(accountID=self['account_id'])
                rv2 = self['api'].request(r2)
                pend2 = rv2.get('orders', []) if isinstance(rv2, dict) else []
            except Exception:
                pend2 = []
            tmp = []
            seen = set()
            for od in (pend + pend2):
                oid = od.get('id')
                if oid in seen:
                    continue
                seen.add(oid)
                tmp.append(od)
            pend = tmp
            instr = str(instrument).upper().replace('-', '_').strip() if instrument else None
            for od in pend:
                od_type = str(od.get('type', '')).upper()
                if not include_attached and od_type in ('STOP_LOSS', 'TAKE_PROFIT', 'TRAILING_STOP_LOSS'):
                    continue
                ins = str(od.get('instrument', '')).upper()
                if instr:
                    if ins == instr:
                        out.append({'id': od.get('id'), 'instrument': ins, 'type': od_type, 'tradeID': od.get('tradeID') or od.get('tradeId')})
                    else:
                        # For attached orders with no instrument, try resolving via TradeDetails
                        if include_attached and od_type in ('STOP_LOSS', 'TAKE_PROFIT', 'TRAILING_STOP_LOSS'):
                            tid = od.get('tradeID') or od.get('tradeId')
                            if tid:
                                try:
                                    td = oanda_trades.TradeDetails(accountID=self['account_id'], tradeID=str(tid))
                                    tinfo = self['api'].request(td)
                                    t = tinfo.get('trade', {}) if isinstance(tinfo, dict) else {}
                                    tins = str(t.get('instrument', '')).upper()
                                    if tins == instr:
                                        out.append({'id': od.get('id'), 'instrument': tins, 'type': od_type, 'tradeID': tid})
                                except Exception:
                                    pass
                else:
                    out.append({'id': od.get('id'), 'instrument': ins, 'type': od_type, 'tradeID': od.get('tradeID') or od.get('tradeId')})
        except Exception:
            pass
        return out


    def get_total_margin_used(self):
        trades=self.get_position_list()
        total_margin_used=0.0
        for trade in trades:
            total_margin_used+=float(trade['marginUsed'])
        return total_margin_used

    def get_total_margin_available(self):
        balance=self.get_balance()
        total_margin_used=self.get_total_margin_used()
        total_margin_available=balance-total_margin_used
        return total_margin_available
    
    def get_instrument_margin_available(self,instrument,status='switch'):
        margin_percent=self.get_margin_percent(instrument)
        if margin_percent is None:
            return None
        total_margin_available=self.get_total_margin_available()*.9
        if margin_percent==0:
            return None
        instrument_margin_available=total_margin_available/margin_percent
        if status=='not_switch':
            return self.convert_currency('USD',instrument.split('_')[0],instrument_margin_available)
        if status=='switch':
            positions=self.get_instrument_positions(instrument)
            units=0
            for position in positions:
                units+=abs(float(position['units']))
            return self.convert_currency('USD',instrument.split('_')[0],instrument_margin_available)+units*2*.9

    def get_position_list(self):
        #user function with offline fallback
        try:
            r = oanda_trades.OpenTrades(accountID=self['account_id'])
            rv = self['api'].request(r)
            return rv.get('trades', [])
        except Exception:
            return []

    def _load_tradable_instruments(self):
        # Fetch and cache tradable instrument names for the account to avoid invalid API calls
        import oandapyV20.endpoints.accounts as oanda_accounts
        r = oanda_accounts.AccountInstruments(accountID=self['account_id'])
        resp = self['api'].request(r)
        names = set(i.get('name') for i in resp.get('instruments', []) if isinstance(i, dict) and 'name' in i)
        self['_instrument_set'] = names
        return names
            
    def _has_instrument(self, name):
        s = self.get('_instrument_set')
        if not s:
            try:
                s = self._load_tradable_instruments()
            except V20Error:
                return False
        return name in s

    def _invert_bid_ask(self, bid, ask):
        """
        Invert a bid/ask quote (e.g., for converting EUR_USD to USD_EUR):
        new_bid = 1/ask; new_ask = 1/bid
        """
        bid = float(bid)
        ask = float(ask)
        if bid <= 0.0 or ask <= 0.0:
            raise ValueError("Bid/Ask must be positive to invert")
        return (1.0 / ask, 1.0 / bid)

    def current_price(self,instrument="EUR_USD"):
        try:
            import oandapyV20.endpoints.pricing as oanda_pricing
            instr = str(instrument).upper()
            invert = False
            if self._has_instrument(instr):
                query_instr = instr
            else:
                rev = "_".join(instr.split("_")[::-1]) if "_" in instr else None
                if rev and self._has_instrument(rev):
                    query_instr = rev
                    invert = True
                else:
                    # Fallback immediately if instrument not available
                    return {'bid': 1.0, 'ask': 1.0, 'mid': 1.0}
            r = oanda_pricing.PricingInfo(accountID=self['account_id'], params={'instruments': query_instr})
            rv = self['api'].request(r)
            prices = rv.get('prices', [])
            if not prices:
                return {'bid': 1.0, 'ask': 1.0, 'mid': 1.0}

            p = prices[0]
            # Prefer bid/ask arrays if present
            if 'bids' in p and 'asks' in p and p['bids'] and p['asks']:
                bid = float(p['bids'][0]['price'])
                ask = float(p['asks'][0]['price'])
            # Fallback to closeout bid/ask if present
            elif 'closeoutBid' in p and 'closeoutAsk' in p:
                bid = float(p['closeoutBid'])
                ask = float(p['closeoutAsk'])
            else:
                return {'bid': 1.0, 'ask': 1.0, 'mid': 1.0}

            if invert:
                bid, ask = self._invert_bid_ask(bid, ask)

            mid = (bid + ask) / 2.0
            return {'bid': bid, 'ask': ask, 'mid': mid}
        except Exception:
            return {'bid': 1.0, 'ask': 1.0, 'mid': 1.0}
    
    def convert_currency(self, from_currency, to_currency, amount=1.0, price_type='mid'):
        """
        Convert an amount from one currency to another. Falls back to 1:1 if pricing unavailable.
        """
        try:
            import oandapyV20.endpoints.pricing as oanda_pricing
            base = str(from_currency).upper()
            quote = str(to_currency).upper()
            instr = f"{base}_{quote}"
            invert = False
            if base == quote:
                return float(amount)

            if self._has_instrument(instr):
                query_instr = instr
            else:
                rev = f"{quote}_{base}"
                if self._has_instrument(rev):
                    query_instr = rev
                    invert = True
                else:
                    return float(amount)  # Fallback 1:1 conversion

            r = oanda_pricing.PricingInfo(accountID=self['account_id'], params={'instruments': query_instr})
            rv = self['api'].request(r)
            prices = rv.get('prices', [])
            if not prices:
                return float(amount)

            p = prices[0]
            if 'bids' in p and 'asks' in p and p['bids'] and p['asks']:
                bid = float(p['bids'][0]['price'])
                ask = float(p['asks'][0]['price'])
            elif 'closeoutBid' in p and 'closeoutAsk' in p:
                bid = float(p['closeoutBid'])
                ask = float(p['closeoutAsk'])
            else:
                return float(amount)

            if invert:
                bid, ask = (1.0 / ask, 1.0 / bid)

            mid = (bid + ask) / 2.0
            pt = str(price_type).lower()
            rate = bid if pt == 'bid' else ask if pt == 'ask' else mid
            return float(amount) * rate
        except Exception:
            return float(amount)
    
    def get_margin_percent(self,instrument):
        # Fetch marginRate for the given instrument. Fallback to 0.02 if unavailable.
        try:
            import oandapyV20.endpoints.accounts as oanda_accounts
            params = {'instruments': instrument}
            r = oanda_accounts.AccountInstruments(accountID=self['account_id'], params=params)
            response = self['api'].request(r)
            instruments = response.get('instruments', [])
            if not instruments:
                return 0.02
            margin_rate = instruments[0].get('marginRate')
            return float(margin_rate) if margin_rate is not None else 0.02
        except Exception:
            return 0.02

    def get_symbol_history(self,instrument="EUR_USD",data_rate="M1",periods=250):
        if isinstance(instrument, list):
            rDict={}
            for instr in instrument:
                rDict[instr]=self.get_candle_history(instrument=instr.upper(), data_rate=data_rate.upper(), periods=periods)
            return rDict
        else:        
            return self.get_candle_history(instrument=instrument, data_rate=data_rate, periods=periods)

    def get_candle_history(self,instrument="EUR_USD",data_rate="M1",periods=250):
        # Returns a pandas DataFrame with columns: open, high, low, close, volume
        try:
            # Validate/normalize granularity
            granularity_map = {
                "S5": "S5", "S10": "S10", "S15": "S15", "S30": "S30",
                "M1": "M1", "M2": "M2", "M4": "M4", "M5": "M5", "M10": "M10",
                "M15": "M15", "M30": "M30",
                "H1": "H1", "H2": "H2", "H3": "H3", "H4": "H4", "H6": "H6",
                "H8": "H8", "H12": "H12",
                "D": "D", "W": "W", "M": "M"
            }
            granularity = granularity_map.get(str(data_rate).upper(), str(data_rate).upper())
            # Clamp count to OANDA max 5000
            count = int(periods)
            if count > 5000:
                count = 5000
            params = {
                "granularity": granularity,
                "count": count,
                "price": "M"
            }
            r = oanda_instruments.InstrumentsCandles(instrument=instrument, params=params)
            response = self['api'].request(r)
            rows = []
            candles = response.get('candles', [])
            if not candles:
                raise ValueError("No candles")
            for c in candles:
                if c.get('complete') is False:
                    continue
                t = c.get('time')
                vol = float(c.get('volume', 0))
                if 'mid' not in c:
                    continue
                o = float(c['mid']['o']); h = float(c['mid']['h']); l = float(c['mid']['l']); cl = float(c['mid']['c'])
                rows.append([t, o, h, l, cl, vol])
            df = pd.DataFrame(rows, columns=['time','open','high','low','close','volume'])
            if df.empty:
                raise ValueError("Empty candle DataFrame")
            df['time'] = pd.to_datetime(df['time'], utc=True)
            for col in ['open','high','low','close','volume']:
                df[col] = df[col].astype(float)
            df.index=range(len(df))
            return df
        except Exception:
            # Synthetic fallback: simple random walk to allow offline runs
            n = max(int(periods), 2)
            rng = np.random.default_rng(42)
            steps = rng.normal(loc=0.0, scale=0.001, size=n)
            close = 1.0 + np.cumsum(steps)
            open_ = np.concatenate(([close[0]], close[:-1]))
            high = np.maximum(open_, close) + rng.normal(0, 0.0005, size=n)
            low = np.minimum(open_, close) - rng.normal(0, 0.0005, size=n)
            volume = np.abs(rng.normal(1000, 50, size=n))
            df = pd.DataFrame({
                'open': open_,
                'high': high,
                'low': low,
                'close': close,
                'volume': volume
            })
            df.index = range(len(df))
            return df
        
    def get_all_resting_bids_list(self, instrument='EUR_USD', scale=None, round_price=True, sort='desc'):
        """
        Return all resting bid buckets as a list of {'price': ..., 'units': ...} sorted by price.
        - units are integer volumes converted from OANDA longCountPercent using scale or configured default.
        - sort: 'desc' (high to low), 'asc' (low to high), or None for insertion order.
        """
        instr = str(instrument).upper().replace('-', '_').strip()
        ob = self.get_order_book_snapshot(instrument=instr, at=None)
        order_book = ob.get('orderBook') if isinstance(ob, dict) else None
        if not order_book:
            return []
        # best bid to partition
        px = self.current_price(instrument=instr)
        try:
            best_bid = float(px.get('bid', 0.0))
        except Exception:
            best_bid = 0.0
        try:
            disp, _, _ = self._get_precisions(instr)
        except Exception:
            disp = 5
        def _rp(v):
            if not round_price:
                return float(v)
            try:
                return round(float(v), int(disp))
            except Exception:
                return float(v)
        out = []
        for b in (order_book.get('buckets') or []):
            try:
                pr = float(b.get('price'))
            except Exception:
                continue
            try:
                lp = float(b.get('longCountPercent', 0.0))
            except Exception:
                lp = 0.0
            if pr <= best_bid and lp > 0.0:
                units = int(round(self._percent_to_units(lp, scale)))
                out.append({'price': _rp(pr), 'units': units})
        if sort in ('desc', 'asc'):
            out.sort(key=lambda x: x['price'], reverse=(sort == 'desc'))
        return out

    def get_all_resting_asks_list(self, instrument='EUR_USD', scale=None, round_price=True, sort='asc'):
        """
        Return all resting ask buckets as a list of {'price': ..., 'units': ...} sorted by price.
        - units are integer volumes converted from OANDA shortCountPercent using scale or configured default.
        - sort: 'asc' (low to high, default), 'desc' (high to low), or None for insertion order.
        """
        instr = str(instrument).upper().replace('-', '_').strip()
        ob = self.get_order_book_snapshot(instrument=instr, at=None)
        order_book = ob.get('orderBook') if isinstance(ob, dict) else None
        if not order_book:
            return []
        # best ask to partition
        px = self.current_price(instrument=instr)
        try:
            best_ask = float(px.get('ask', 0.0))
        except Exception:
            best_ask = 0.0
        try:
            disp, _, _ = self._get_precisions(instr)
        except Exception:
            disp = 5
        def _rp(v):
            if not round_price:
                return float(v)
            try:
                return round(float(v), int(disp))
            except Exception:
                return float(v)
        out = []
        for b in (order_book.get('buckets') or []):
            try:
                pr = float(b.get('price'))
            except Exception:
                continue
            try:
                sp = float(b.get('shortCountPercent', 0.0))
            except Exception:
                sp = 0.0
            if pr >= best_ask and sp > 0.0:
                units = int(round(self._percent_to_units(sp, scale)))
                out.append({'price': _rp(pr), 'units': units})
        if sort in ('desc', 'asc'):
            out.sort(key=lambda x: x['price'], reverse=(sort == 'desc'))
        return out

    def get_bid_ask_candles(self, instrument='EUR_USD', data_rate='M30', periods=1, include_incomplete=False, as_dataframe=True):
        """
        Fetch bid/ask OHLC candles for a given instrument and bar interval.
        - instrument: OANDA instrument (e.g., 'EUR_USD')
        - data_rate: granularity (e.g., 'M1','M5','M15','M30','H1',...)
        - periods: number of bars to return
        - include_incomplete: include the current in-progress bar if available
        - as_dataframe: return pandas DataFrame if pandas is available; else list of dicts
        DataFrame columns (if available): time, complete, volume, bid_o, bid_h, bid_l, bid_c, ask_o, ask_h, ask_l, ask_c
        """
        try:
            instr = str(instrument).upper().replace('-', '_').strip()
            # Normalize granularity (allow pass-through)
            granularity_map = {
                "S5": "S5", "S10": "S10", "S15": "S15", "S30": "S30",
                "M1": "M1", "M2": "M2", "M4": "M4", "M5": "M5", "M10": "M10",
                "M15": "M15", "M30": "M30",
                "H1": "H1", "H2": "H2", "H3": "H3", "H4": "H4", "H6": "H6",
                "H8": "H8", "H12": "H12",
                "D": "D", "W": "W", "M": "M"
            }
            granularity = granularity_map.get(str(data_rate).upper(), str(data_rate).upper())
            count = max(int(periods), 1)
            req_count = count + (0 if include_incomplete else 1)  # over-fetch one to ensure enough completed bars
            params = {
                "granularity": granularity,
                "count": req_count,
                "price": "BA"  # Bid/Ask candles
            }
            r = oanda_instruments.InstrumentsCandles(instrument=instr, params=params)
            response = self['api'].request(r)
            candles = response.get('candles', [])
            rows = []
            for c in candles:
                complete = bool(c.get('complete', False))
                if not include_incomplete and not complete:
                    continue
                t = c.get('time')
                vol = float(c.get('volume', 0))
                bid = c.get('bid') or {}
                ask = c.get('ask') or {}
                def _f(x):
                    try:
                        return float(x)
                    except Exception:
                        return None
                rows.append({
                    'time': t,
                    'complete': complete,
                    'volume': vol,
                    'bid_o': _f(bid.get('o')), 'bid_h': _f(bid.get('h')),
                    'bid_l': _f(bid.get('l')), 'bid_c': _f(bid.get('c')),
                    'ask_o': _f(ask.get('o')), 'ask_h': _f(ask.get('h')),
                    'ask_l': _f(ask.get('l')), 'ask_c': _f(ask.get('c'))
                })
            if not rows:
                # nothing available
                return [] if not (as_dataframe and 'pd' in globals()) else pd.DataFrame(columns=[
                    'time','complete','volume','bid_o','bid_h','bid_l','bid_c','ask_o','ask_h','ask_l','ask_c'
                ])
            # Keep the most recent N rows
            rows = rows[-count:]
            if as_dataframe and 'pd' in globals():
                df = pd.DataFrame(rows)
                try:
                    df['time'] = pd.to_datetime(df['time'], utc=True)
                except Exception:
                    pass
                return df
            return rows
        except Exception:
            # Graceful fallback
            if as_dataframe and 'pd' in globals():
                try:
                    return pd.DataFrame(columns=[
                        'time','complete','volume','bid_o','bid_h','bid_l','bid_c','ask_o','ask_h','ask_l','ask_c'
                    ])
                except Exception:
                    pass
            return []
        

    def get_market_order_volume_ewma(self, instrument='EUR_USD', granularity='M1', samples=1000, span=36, order_tick_ratio=1.0, as_dataframe=True):
        """
        Compute an exponentially weighted moving average (EWMA) of estimated market-order volume
        over the last 'samples' candles at a given granularity.
        - market-order volume per sample is estimated as: tick_volume * order_tick_ratio
        - EWMA uses span=N (alpha = 2/(N+1)), default span=36
        Returns a pandas DataFrame if available and as_dataframe=True with columns:
          time (if available), volume (tick volume), market_volume, ewma
        Otherwise returns a list of dicts with the same fields where present.
        """
        try:
            n = int(samples)
            s = int(span) if int(span) > 0 else 36
        except Exception:
            n = 1000; s = 36
        alpha = 2.0 / (s + 1.0)
        try:
            df = self.get_candle_history(instrument=instrument, data_rate=str(granularity).upper(), periods=n)
        except Exception:
            df = None
        try:
            # build sequences
            vol_seq = []
            time_seq = []
            if df is not None and 'volume' in df.columns:
                try:
                    vol_seq = [float(v) for v in df['volume'].tolist()]
                except Exception:
                    vol_seq = []
                if 'time' in df.columns:
                    try:
                        time_seq = df['time'].tolist()
                    except Exception:
                        time_seq = [None] * len(vol_seq)
                else:
                    time_seq = [None] * len(vol_seq)
            # EWMA compute
            if not vol_seq:
                return (df if (as_dataframe and 'pd' in globals()) else [])
            mv = [float(order_tick_ratio) * v for v in vol_seq]
            ew = [mv[0]]
            for i in range(1, len(mv)):
                ew.append(alpha * mv[i] + (1.0 - alpha) * ew[-1])
            if as_dataframe and 'pd' in globals():
                try:
                    out = {
                        'market_volume': mv,
                        'ewma': ew,
                        'volume': vol_seq
                    }
                    if any(t is not None for t in time_seq):
                        out['time'] = time_seq
                    res = pd.DataFrame(out)
                    return res
                except Exception:
                    pass
            # fallback: list of dicts
            rows = []
            for i in range(len(mv)):
                rows.append({
                    'time': time_seq[i] if i < len(time_seq) else None,
                    'volume': vol_seq[i],
                    'market_volume': mv[i],
                    'ewma': ew[i]
                })
            return rows
        except Exception:
            # final fallback
            return pd.DataFrame(columns=['time','volume','market_volume','ewma']) if (as_dataframe and 'pd' in globals()) else []



    def place_order(self, instrument='EUR_USD', units=1000, price=None,stop=False, wait=False, timeout=60, poll_interval=1.0):
        # normalize and validate instrument for orders
        instr = str(instrument).upper().replace('-', '_').strip()
        disp, tick, pip = self._get_precisions(instr)
        if not self._has_instrument(instr):
            logging.error(f"Failed to place order: invalid instrument '{instrument}' for account {self['account_id']}")
            return None
        #user function
        data = {
            "order": {
                "units": str(units),
                "instrument": instr,
                "timeInForce": "FOK",
                "type": "MARKET",
                "positionFill": "DEFAULT"
            }
        }
        if price is not None:
            data['order']['price'] = str(price)
            data['order']['type'] = 'STOP'
            data['order']['timeInForce'] = 'GTC'
        if stop:
            #data['order']['type'] = 'stopLimit'
            data["stopPrice"]=str(price)
            data['order']['stopLossOnFill']={'distance':pip*5}
            data['order']['timeInForce'] = 'GTC'    
        r = oanda_orders.OrderCreate(accountID=self['account_id'], data=data)
        try:
            rv = self['api'].request(r)
            logging.info(f"Placed order: {rv}")
            if wait and rv is not None:
                try:
                    return self.wait_for_order_completion(rv, timeout=timeout, poll_interval=poll_interval)
                except Exception as ex:
                    logging.error(f"wait_for_order_completion failed: {ex}")
                    return rv
            return rv
        except V20Error as e:
            logging.error(f"Failed to place order: {e}")
            return None

    def buy(self, instrument='EUR_USD', units=1000, price=None,stop=False, wait=False, timeout=60, poll_interval=1.0):
        #user function
        units = abs(units)
        return self.place_order(instrument=instrument, units=units, price=price,stop=stop, wait=wait, timeout=timeout, poll_interval=poll_interval)
        
    def sell(self, instrument='EUR_USD', units=1000, price=None,stop=False, wait=False, timeout=60, poll_interval=1.0):
        #user function
        units = abs(units)
        return self.place_order(instrument=instrument, units=-units, price=price,stop=stop, wait=wait, timeout=timeout, poll_interval=poll_interval)

    def cancel_orders(self):
        """
        Cancel ALL pending orders across all instruments for this account.
        Returns a summary dict:
          {
            'attempted': int,
            'canceled': int,
            'errors': int,
            'details': [{'orderID', 'status', 'response'|'error'}...]
          }
        """
        results = {
            'attempted': 0,
            'canceled': 0,
            'errors': 0,
            'details': []
        }
        # Collect pending orders using both OrdersList(state=PENDING) and OrdersPending for robustness
        try:
            lst = []
            try:
                params = {'state': 'PENDING', 'count': 500}
                r1 = oanda_orders.OrdersList(accountID=self['account_id'], params=params)
                rv1 = self['api'].request(r1)
                lst = rv1.get('orders', []) if isinstance(rv1, dict) else []
            except Exception:
                lst = []
            try:
                r2 = oanda_orders.OrdersPending(accountID=self['account_id'])
                rv2 = self['api'].request(r2)
                pend2 = rv2.get('orders', []) if isinstance(rv2, dict) else []
            except Exception:
                pend2 = []
            # Deduplicate by order id
            seen = set()
            pending = []
            for od in (lst + pend2):
                oid = od.get('id')
                if oid in seen:
                    continue
                seen.add(oid)
                pending.append(od)
        except Exception:
            pending = []
        for od in pending:
            try:
                oid = od.get('id')
                if not oid:
                    continue
                results['attempted'] += 1
                try:
                    cr = oanda_orders.OrderCancel(accountID=self['account_id'], orderID=str(oid))
                    resp = self['api'].request(cr)
                    results['canceled'] += 1
                    results['details'].append({'orderID': oid, 'status': 'canceled', 'response': resp})
                except V20Error as e:
                    results['errors'] += 1
                    results['details'].append({'orderID': oid, 'status': 'error', 'error': str(e)})
                except Exception as e:
                    results['errors'] += 1
                    results['details'].append({'orderID': oid, 'status': 'error', 'error': str(e)})
            except Exception as e:
                results['errors'] += 1
                results['details'].append({'status': 'error', 'error': str(e)})
        return results

    def cancel_instrument_orders(self, instrument='EUR_USD', include_attached=False, order_types=None, max_retries=3, retry_sleep=1.0):
        """
        Cancel pending orders for a specific instrument.
        - include_attached: include protection orders (STOP_LOSS, TAKE_PROFIT, TRAILING_STOP_LOSS)
        - order_types: optional iterable of order 'type' strings to restrict cancellation
        - max_retries/retry_sleep: retry on transient failures
        Returns summary dict: {'instrument','attempted','canceled','errors','details':[...] }
        """
        instr = str(instrument).upper().replace('-', '_').strip()
        results = {
            'instrument': instr,
            'attempted': 0,
            'canceled': 0,
            'errors': 0,
            'details': []
        }
        # Resolve allowed types if provided
        allowed_types = None
        if order_types:
            try:
                allowed_types = {str(t).upper() for t in order_types}
            except Exception:
                allowed_types = None
        try:
            pend = self.list_pending_orders(instrument=instr, include_attached=True)
        except Exception:
            pend = []
        for od in pend:
            try:
                od_type = str(od.get('type', '')).upper()
                # Filter attached protections unless requested
                if not include_attached and od_type in ('STOP_LOSS', 'TAKE_PROFIT', 'TRAILING_STOP_LOSS'):
                    continue
                # Filter by explicit order types if provided
                if allowed_types is not None and od_type not in allowed_types:
                    continue
                od_id = od.get('id')
                if not od_id:
                    continue
                results['attempted'] += 1
                tries = 0
                while True:
                    try:
                        cr = oanda_orders.OrderCancel(accountID=self['account_id'], orderID=str(od_id))
                        resp = self['api'].request(cr)
                        results['canceled'] += 1
                        results['details'].append({'orderID': od_id, 'status': 'canceled', 'response': resp})
                        break
                    except V20Error as e:
                        msg = str(e).lower()
                        if ('429' in msg or 'rate limit' in msg) and tries < int(max_retries):
                            tries += 1
                            sleep(float(retry_sleep) * tries)
                            continue
                        results['errors'] += 1
                        results['details'].append({'orderID': od_id, 'status': 'error', 'error': str(e)})
                        break
                    except Exception as e:
                        if tries < int(max_retries):
                            tries += 1
                            sleep(float(retry_sleep) * tries)
                            continue
                        results['errors'] += 1
                        results['details'].append({'orderID': od_id, 'status': 'error', 'error': str(e)})
                        break
            except Exception as e:
                results['errors'] += 1
                results['details'].append({'status': 'error', 'error': str(e)})
        return results


    def close_instrument_positions(self, instrument, long=True, short=True):
        """
        Close open position side(s) for a specific instrument using OANDA v20 Positions endpoint.
        Only sends longUnits/shortUnits for sides that are actually open to avoid 400 errors.
        - instrument: string like 'EUR_USD'
        - long/short: booleans indicating which side(s) to attempt to close
        Returns API response dict on success, or a dict with 'instrument' and 'closed': False when nothing to close.
        """
        import oandapyV20.endpoints.positions as oanda_positions
        instr = str(instrument).upper()
        # Inspect current position details to know which sides are open
        try:
            details_req = oanda_positions.PositionDetails(accountID=self['account_id'], instrument=instr)
            details = self['api'].request(details_req)
            pos = details.get('position', {}) if isinstance(details, dict) else {}
        except V20Error as e:
            logging.error(f"PositionDetails failed for {instr}: {e}")
            # If no position exists or instrument invalid, return a consistent structure
            return {'instrument': instr, 'closed': False, 'error': str(e)}
        except Exception as e:
            logging.error(f"Unexpected error fetching PositionDetails for {instr}: {e}")
            return {'instrument': instr, 'closed': False, 'error': str(e)}

        def _get_units(side):
            try:
                return float(pos.get(side, {}).get('units', '0'))
            except Exception:
                return 0.0

        long_units_open = _get_units('long')
        short_units_open = _get_units('short')

        data = {}
        if long and long_units_open != 0.0:
            data['longUnits'] = 'ALL'
        if short and short_units_open != 0.0:
            data['shortUnits'] = 'ALL'

        if not data:
            # Nothing to close for requested sides
            return {'instrument': instr, 'closed': False, 'reason': 'no open sides to close for requested direction(s)'}

        try:
            r = oanda_positions.PositionClose(accountID=self['account_id'], instrument=instr, data=data)
            resp = self['api'].request(r)
            return resp
        except V20Error as e:
            logging.error(f"PositionClose failed for {instr} with payload {data}: {e}")
            return {'instrument': instr, 'closed': False, 'error': str(e), 'payload': data}
        except Exception as e:
            logging.error(f"Unexpected error closing {instr} with payload {data}: {e}")
            return {'instrument': instr, 'closed': False, 'error': str(e), 'payload': data}

    def close_positions(self):
        """
        Close all open positions across all instruments in the account.
        Returns a list of API responses per instrument attempted.
        """
        import oandapyV20.endpoints.positions as oanda_positions
        results = []
        # Get open positions
        try:
            r = oanda_positions.OpenPositions(accountID=self['account_id'])
            rv = self['api'].request(r)
            positions = rv.get('positions', [])
        except V20Error as e:
            logging.error(f"Failed to fetch open positions: {e}")
            return results

        for pos in positions:
            instrument = pos.get('instrument')
            if not instrument:
                continue
            # Determine which sides are open
            data = {}
            try:
                long_units = float(pos.get('long', {}).get('units', '0'))
            except Exception:
                long_units = 0.0
            try:
                short_units = float(pos.get('short', {}).get('units', '0'))
            except Exception:
                short_units = 0.0
            if long_units != 0.0:
                data['longUnits'] = 'ALL'
            if short_units != 0.0:
                data['shortUnits'] = 'ALL'
            if not data:
                continue  # nothing to close
            try:
                req = oanda_positions.PositionClose(accountID=self['account_id'], instrument=instrument, data=data)
                res = self['api'].request(req)
                results.append(res)
            except V20Error as e:
                logging.error(f"Failed to close position {instrument}: {e}")
                results.append({'instrument': instrument, 'error': str(e)})
        return results

    

if __name__ == "__main__":
    e = ether()
    #print(e.get_all_ask_depth())
    #print(e.get_all_bid_depth())
    #print(e.get_bid_ask_candles('eur_usd','m15',5,True))
    #print(e.get_price_ladder_from_spread('eur_usd',5,1.0,'both',1000,False,True))
    
    #print(e.get_all_ask_depth_at_bar('eur_usd','h4',200,0.0,None,True))    
    #print(e.get_all_resting_asks_list('eur_usd',None,True))
    #get_average_expected_filled_order_units
    #e.get_average_expected_filled_order_units('eur_usd','m1',1000,36,100000,True,36,True)
    #e.buy()
    #e.sell("EUR_USD",1000)
    #e.sell("EUR_USD",1000,price=round(e.get_bid_ask_candles('EUR_USD')['ask_c'].iloc[-1]+.005,4))
    #e.sell("USD_JPY",1000,price=round(e.get_bid_ask_candles('USD_JPY')['ask_c'].iloc[-1]+.005,4))
    #e.sell("USD_JPY",1000)
    #e.cancel_instrument_orders('EUR_USD')
    #e.close_positions()
    ###########################################################################
