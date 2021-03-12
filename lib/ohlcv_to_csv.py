import pandas as pd
from lib.fetch_ohlcv import fetch_ohlcv

printer = print

def ohlcv_to_csv(symbol, start=None, end=None, per=False, pbr=False, roe=False, print=False):

    # Fetch OHLCV data
    qoute_list = fetch_ohlcv(symbol, start, end)

    if per:
        pass

    if pbr:
        pass

    if roe:
        pass
    
    if print:
        printer(qoute_list)

    # Save to csv
    f_name = symbol + "_" + start + ("_" + end if end else "")
    qoute_list.to_csv(f_name)