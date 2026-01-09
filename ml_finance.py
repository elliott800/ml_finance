#ml_finance.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import yfinance as yf
####################################
#YAHOO DATA#########################
####################################
"""
fetch_asset_history.py

A script to collect asset historical data from Yahoo Finance using the yfinance library.

Usage:
    python fetch_asset_history.py --ticker AAPL --total_periods 30

Arguments:
    --ticker        The asset ticker symbol (e.g., AAPL, MSFT)
    --period_type   Type of period: "d" for days, "wk" for weeks, "mo" for months (optional, currently unused)
    --total_periods Total number of periods to fetch (e.g., 30)
"""
import pandas as pd
import argparse
import yfinance as yf
from datetime import datetime, timedelta

def parse_args():
    parser = argparse.ArgumentParser(description="Fetch asset history using yfinance.")
    parser.add_argument('--ticker', type=str, required=True, help='Asset ticker symbol (e.g., AAPL)')
    parser.add_argument('--period_type', type=str, choices=['d', 'wk', 'mo'], required=False, help='Period type: d=days, wk=weeks, mo=months (optional)')
    parser.add_argument('--total_periods', type=int, required=True, help='Total number of periods to fetch')
    return parser.parse_args()

def get_timedelta(period_size, period_type):
    if period_type == 'd':
        return timedelta(days=period_size)
    elif period_type == 'wk':
        return timedelta(weeks=period_size)
    elif period_type == 'mo':
        # Approximate a month as 30 days
        return timedelta(days=30 * period_size)
    else:
        raise ValueError("Invalid period_type. Use 'd', 'wk', or 'mo'.")

def yh_fetch_history(ticker, period_type, total_periods):
    asset = yf.Ticker(ticker)
    # Always fetch all available data
    df = asset.history(period="max")
    if df.empty:
        print("No data fetched.")
        return None
    # Resample based on period_type
    if period_type == 'wk':
        # Resample to weekly, using last value of each week
        df = df.resample('W').last()
    elif period_type == 'mo':
        # Resample to monthly, using last value of each month
        df = df.resample('ME').last()
    # else: keep as is for 'd' or None
    # Return only the most recent total_periods rows
    if total_periods < len(df):
        df = df.tail(total_periods)
    #print(f"Fetched {len(df)} rows (max available or up to total_periods)")
    return df if not df.empty else None
    
def yh_main():
    args = parse_args()
    all_data = yh_fetch_history(
        args.ticker,
        args.period_type,
        args.total_periods
    )
    # Concatenate all dataframes
    import pandas as pd
    if all_data:
        result = pd.concat(all_data)
        print(result)
    else:
        print("No data fetched.")

def yh_data(pItem,period_type='d',total_periods=1000000):
    rDict={}
    if isinstance(pItem,list):
        # Process the list of assets
        for asset in pItem:
            # Fetch the asset history
            history = yh_fetch_history(asset, period_type, total_periods)
            # Do something with the history
            #print(f"History for {asset}: {history}")
            if isinstance(history, pd.DataFrame):
                if not history.empty:
                    history=history.rename(columns={'Date':'date','Open':'open','High':'high','Low':'low','Close':'close','Volume':'volume','Dividends':'dividends','Stock Splits':'stock splits'})
                    rDict[asset] = history
    else:
        # Fetch the asset history
            history = yh_fetch_history(pItem, period_type, total_periods)
            # Do something with the history
            #print(f"History for {pItem}: {history}")
            if isinstance(history, pd.DataFrame):
                if not history.empty:
                    history=history.rename(columns={'Date':'date','Open':'open','High':'high','Low':'low','Close':'close','Volume':'volume','Dividends':'dividends','Stock Splits':'stock splits'})
                    history.name=pItem
                    rDict = history
    return rDict

class yahoo_api(dict):
    def __init__(self):
        self['name']='yahoo'
    def get_symbol_history(self,pList_sym,period_type='d',total_periods=1000000):
        return yh_data(pList_sym,period_type,total_periods)
####################################
#YAHOO DATA#########################
####################################
if __name__ == "__main__":
    yh_api=yahoo_api()
    print(yh_api.get_symbol_history('uso','d').to_period('M'))
    input()
