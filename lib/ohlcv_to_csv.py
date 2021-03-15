import pandas as pd
from lib.fetch_ohlcv import fetch_ohlcv
from lib.MorningStarCrawler import MorningStarCrawler

printer = print

def ohlcv_to_csv(symbol, start=None, end=None, per=False, pbr=False, roe=False, print=False, order=None):

    msc = None

    # Fetch OHLCV data
    qoute_list = fetch_ohlcv(symbol, start, end)

    if per:
        if not msc:
            msc = MorningStarCrawler(symbol, "XNAS")

        per = msc.get_per()
        try:
            qoute_list['per'] = qoute_list.apply(lambda x: per[int(str(x.name)[:4])], axis=1)
        except KeyError as e:
            _handleKeyError(e)
            
    if pbr:
        if not msc:
            msc = MorningStarCrawler(symbol, "XNAS")

        pbr = msc.get_pbr()
        try:
            qoute_list['pbr'] = qoute_list.apply(lambda x: pbr[int(str(x.name)[:4])], axis=1)
        except KeyError as e:
            _handleKeyError(e)

    if roe:
        if not msc:
            msc = MorningStarCrawler(symbol, "XNAS")
        
        roe = msc.get_roe()
        try:
            qoute_list['roe'] = qoute_list.apply(lambda x: roe[int(str(x.name)[:4])], axis=1)
        except KeyError as e:
            _handleKeyError(e)
    
    if order and isinstance(order, list):
        qoute_list = qoute_list[order]

    if print:
        printer(qoute_list)

    # Save to csv
    f_name = symbol + "_" + start + ("_" + end if end else "") + ".csv"
    qoute_list.to_csv(f_name)

def _handleKeyError(e):
    print("Not enough data for the year: " + str(e))
    exit()