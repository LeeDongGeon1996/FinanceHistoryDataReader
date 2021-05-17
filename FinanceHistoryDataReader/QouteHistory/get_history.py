import math
import pandas as pd
from .fetch_ohlcv import fetch_ohlcv
from .MorningStarCrawler import MorningStarCrawler

printer = print

def get_history(symbol, start=None, end=None, market='XNAS', per=False, pbr=False, roe=False, print=False, order=None):

    msc = None

    # Fetch OHLCV data
    qoute_list = fetch_ohlcv(symbol.replace('.',''), start, end)

    if per:
        if not msc:
            msc = MorningStarCrawler(symbol, market)

        per = msc.get_per()
        add_column_by_year(qoute_list, 'per', per)
            
    if pbr:
        if not msc:
            msc = MorningStarCrawler(symbol, market)

        pbr = msc.get_pbr()
        add_column_by_year(qoute_list, 'pbr', pbr)

    if roe:
        if not msc:
            msc = MorningStarCrawler(symbol, market)
        
        roe = msc.get_roe()
        add_column_by_year(qoute_list, 'roe', roe)
    
    if order and isinstance(order, list):
        qoute_list = qoute_list[order]

    if print:
        printer(qoute_list)

    return qoute_list

def add_column_by_year(data_frame, col_name, col_as_dict):
    try:
        data_frame[col_name] = data_frame.apply(lambda x: col_as_dict.get(str(x.name)[:4]), axis=1)
    except KeyError as e:
        _handleKeyError(e)

    return data_frame

def add_column_by_day(data_frame, col_name, col_as_dict):
    try:
        data_frame[col_name] = data_frame.apply(lambda x: col_as_dict.get(str(x.name)[:10]) or None, axis=1)
    except KeyError as e:
        _handleKeyError(e)

    return data_frame

def fill_nan(data_frame, col_name):
    target_col = data_frame[col_name]
    if target_col is not None:
        default_value = None
        for idx, val in target_col.items():
            try:
                if math.isnan(float(val)):
                    target_col[idx] = default_value
                else:
                    default_value = val
            except:
                target_col[idx] = default_value
    else:
        raise KeyError()


def save_as_csv(data_fram, name):
    data_fram.to_csv(name if str(name).endswith('.csv') else name + '.csv', float_format='%.4f')

def _handleKeyError(e):
    print("Not enough data for the year: " + str(e))
    exit()