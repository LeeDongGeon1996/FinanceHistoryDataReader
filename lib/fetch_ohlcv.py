import FinanceDataReader as fdr
import pandas as pd

def fetch_ohlcv(symbol, start=None, end=None, exchange=None, data_source=None, show_change = False):
    df = fdr.DataReader(symbol, start, end, exchange, data_source)

    # Reorder to OHLCV
    cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    if show_change:
        cols.append('Change')
    
    df = df[cols]    
    return df
