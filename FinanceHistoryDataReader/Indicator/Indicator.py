from datetime import datetime
from System import Decimal as CsDecimal
from System.Collections.Generic import List
from Skender.Stock.Indicators import Indicator
from .Qoute import Qoute


def get_SMA(history, lookbackPeriod):
    sma_list = Indicator.GetSma[Qoute](_convert_df_to_csharp_list(history), lookbackPeriod)
    sma_dict = { _convert_csharp_datetime(i.Date) : (float(str(i.Sma)) if i.Sma else None) for i in sma_list }

    return sma_dict

def get_AROON(history, lookbackPeriod):
    aroon_list = Indicator.GetAroon[Qoute](_convert_df_to_csharp_list(history), lookbackPeriod)
    aroon_dict = { _convert_csharp_datetime(i.Date) : (float(str(i.Oscillator)) if i.Oscillator else None) for i in aroon_list }

    return aroon_dict


def get_ADX(history, lookbackPeriod):
    adx_list = Indicator.GetAdx[Qoute](_convert_df_to_csharp_list(history), lookbackPeriod)
    adx_dict = { _convert_csharp_datetime(i.Date) : (float(str(i.Adx)) if i.Adx else None) for i in adx_list }

    return adx_dict

def get_elder_ray_bull(history, lookbackPeriod):
    _list = Indicator.GetElderRay[Qoute](_convert_df_to_csharp_list(history), lookbackPeriod)
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.BullPower)) if i.BullPower else None) for i in _list }

    return _dict

def get_elder_ray_bear(history, lookbackPeriod):
    _list = Indicator.GetElderRay[Qoute](_convert_df_to_csharp_list(history), lookbackPeriod)
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.BearPower)) if i.BearPower else None) for i in _list }

    return _dict

def get_elder_ray_bear(history, lookbackPeriod):
    _list = Indicator.GetElderRay[Qoute](_convert_df_to_csharp_list(history), lookbackPeriod)
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.BearPower)) if i.BearPower else None) for i in _list }

    return _dict

def get_gator_upper(history):
    _list = Indicator.GetGator[Qoute](_convert_df_to_csharp_list(history))
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.Upper)) if i.Upper else None) for i in _list }

    return _dict

def get_gator_lower(history):
    _list = Indicator.GetGator[Qoute](_convert_df_to_csharp_list(history))
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.Lower)) if i.Lower else None) for i in _list }

    return _dict

def get_ichimoku(history, signalPeriod, shortSpanPeriod, longSpanPeriod):
    _list = Indicator.GetIchimoku[Qoute](_convert_df_to_csharp_list(history), signalPeriod, shortSpanPeriod, longSpanPeriod)
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.TenkanSen)) if i.TenkanSen else None) for i in _list }

    return _dict

def get_macd(history, fastPeriod, slowPeriod, signalPeriod):
    _list = Indicator.GetMacd[Qoute](_convert_df_to_csharp_list(history), fastPeriod, slowPeriod, signalPeriod)
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.Macd)) if i.Macd else None) for i in _list }

    return _dict

def get_super_trend(history, lookbackPeriod, multiplier):
    _list = Indicator.GetSuperTrend[Qoute](_convert_df_to_csharp_list(history), lookbackPeriod, CsDecimal.Parse(str(multiplier)))
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.SuperTrend)) if i.SuperTrend else None) for i in _list }

    return _dict

def get_vortex_positive(history, lookbackPeriod):
    _list = Indicator.GetVortex[Qoute](_convert_df_to_csharp_list(history), lookbackPeriod)
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.Pvi)) if i.Pvi else None) for i in _list }

    return _dict

def get_vortex_negative(history, lookbackPeriod):
    _list = Indicator.GetVortex[Qoute](_convert_df_to_csharp_list(history), lookbackPeriod)
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.Nvi)) if i.Nvi else None) for i in _list }

    return _dict

def get_alligator_jaw(history):
    _list = Indicator.GetAlligator[Qoute](_convert_df_to_csharp_list(history))
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.Jaw)) if i.Jaw else None) for i in _list }

    return _dict

def get_alligator_teeth(history):
    _list = Indicator.GetAlligator[Qoute](_convert_df_to_csharp_list(history))
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.Teeth)) if i.Teeth else None) for i in _list }

    return _dict

def get_alligator_lips(history):
    _list = Indicator.GetAlligator[Qoute](_convert_df_to_csharp_list(history))
    _dict = { _convert_csharp_datetime(i.Date) : (float(str(i.Lips)) if i.Lips else None) for i in _list }

    return _dict













def _convert_csharp_datetime(csharp_datetime):
    return datetime.strptime(str(csharp_datetime).split(" ")[0], '%m/%d/%Y').strftime('%Y-%m-%d')

def _convert_df_to_csharp_list(history):
    listed = List[Qoute]()
    history.apply(lambda x: listed.Add(Qoute(x)), axis=1)
    
    return listed
