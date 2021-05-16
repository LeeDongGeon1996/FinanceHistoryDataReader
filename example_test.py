import clr
clr.AddReference(r'dll/Skender.Stock.Indicators')

import FinanceHistoryDataReader.QouteHistory as qh
import FinanceHistoryDataReader.Indicator as Indicator
import FinanceHistoryDataReader.processing as processing

# Fetching
exxon_history = qh.get_history("XOM", "2020", market='XNYS', per=True, pbr=True)
print("OHLCV and other related price data are fetched.")

qh.add_column_by_day(exxon_history, "aroon_5", Indicator.get_AROON(exxon_history, 5))
qh.add_column_by_day(exxon_history, "adx_5", Indicator.get_ADX(exxon_history, 5))
qh.add_column_by_day(exxon_history, "elder_ray_bull_5", Indicator.get_elder_ray_bull(exxon_history, 5))
qh.add_column_by_day(exxon_history, "elder_ray_bear_5", Indicator.get_elder_ray_bear(exxon_history, 5))
qh.add_column_by_day(exxon_history, "vortex_pos_5", Indicator.get_vortex_positive(exxon_history, 5))
qh.add_column_by_day(exxon_history, "vortex_neg_5", Indicator.get_vortex_negative(exxon_history, 5))
qh.add_column_by_day(exxon_history, "donchian_5", Indicator.get_donchian(exxon_history, 5))
qh.add_column_by_day(exxon_history, "fcb_upper_5", Indicator.get_fcb_upper(exxon_history, 5))
qh.add_column_by_day(exxon_history, "fcb_lower_5", Indicator.get_fcb_lower(exxon_history, 5))



qh.add_column_by_day(exxon_history, "gator_upper", Indicator.get_gator_upper(exxon_history))
qh.add_column_by_day(exxon_history, "gator_lower", Indicator.get_gator_lower(exxon_history))
qh.add_column_by_day(exxon_history, "alligator_jaw", Indicator.get_alligator_jaw(exxon_history))
qh.add_column_by_day(exxon_history, "alligator_teeth", Indicator.get_alligator_teeth(exxon_history))
qh.add_column_by_day(exxon_history, "alligator_lips", Indicator.get_alligator_lips(exxon_history))


qh.add_column_by_day(exxon_history, "ichimoku_9_26_52", Indicator.get_ichimoku(exxon_history, 9, 26, 52))
qh.add_column_by_day(exxon_history, "macd_12_26_9", Indicator.get_macd(exxon_history, 12, 26, 9))
qh.add_column_by_day(exxon_history, "super_trend_14_3", Indicator.get_super_trend(exxon_history, 14,3))
qh.add_column_by_day(exxon_history, "bollinger_bands_upper_20_2", Indicator.get_bollinger_bands_upper(exxon_history, 20,2))
qh.add_column_by_day(exxon_history, "bollinger_bands_lower_20_2", Indicator.get_bollinger_bands_lower(exxon_history, 20,2))
qh.add_column_by_day(exxon_history, "std_dev_channels_20_2", Indicator.get_std_dev_channels(exxon_history, 20,2))


exxon_history = exxon_history.dropna()
print(exxon_history)