import clr
clr.AddReference(r'dll/Skender.Stock.Indicators')

#import FinanceHistoryDataReader as fdr

import FinanceHistoryDataReader.QouteHistory as qh
import FinanceHistoryDataReader.Indicator as Indicator

#csv.ohlcv_to_csv("AAPL", "2019-01-01", "2019-01-29", per=True, pbr=True, roe=True, print=True)

# NASDAQ
apple_history = qh.get_history("AAPL", "2021", per=True, pbr=True)
nasdaq_history = qh.get_history("IXIC", "2020")

nasdaq_sma5 = Indicator.get_SMA(nasdaq_history, 5)
nasdaq_sma20 = Indicator.get_SMA(nasdaq_history, 20)

qh.add_column_by_day(apple_history, "nasdaq_ma5", nasdaq_sma5)
qh.add_column_by_day(apple_history, "nasdaq_ma20", nasdaq_sma20)

qh.save_as_csv(apple_history, "AAPL_2021_with_nasdaq_ma.csv")

print(apple_history)