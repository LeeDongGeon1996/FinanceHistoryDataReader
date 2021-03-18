# FinanceHistoryDataReader

## Requirements
```
pip install finance-datareader, pythonnet, beautifulsoup4, requests, pandas
```

## Usage
You can simply fetch historical price quotes using `get_history`
```
import FinanceHistoryDataReader.QouteHistory as qh

# Amazon(AMZN), Whole period
qh.get_history('AMZN')

# Microsoft(MSFT) 2021-02-14 ~ Now
qh.get_history("MSFT", "2021-02-14")

# Apple(AAPL) 2021-03-01 ~ 2021-03-09
qh.get_history("AAPL", "2021-03-01", "2021-03-09")

# With PER, PBR, ROE, Apple(AAPL) 2019-01-01 ~ Now
qh.get_history("AAPL", "2019", per=True, pbr=True, roe=True)

# Reorder columns, Facebook(FB) 2019-01-01 ~ Now
qh.get_history("FB", "2019-01-01", per=True, order=['per', 'Open', 'High', 'Low', 'Close', 'Volume'])

# Print dataframe, Netflix(NFLX) 2021-01-01 ~ 2021-01-29
qh.get_history("NFLX", "2021-01-01", "2021-01-29", print=True)
```

Also, you can add more indicators like SMA, WMA as columns using `add_column_by_day` or `add_column_by_year`.
To calulate other indicators like SMA, import the dll, `Skender.Stock.Indicators`
```
import clr
clr.AddReference(r'dll/Skender.Stock.Indicators')

import FinanceHistoryDataReader as fdr

apple_history = fdr.QouteHistory.get_history("AAPL", "2021", per=True, pbr=True)
nasdaq_history = fdr.QouteHistory.get_history("IXIC", "2020")

nasdaq_sma5 = fdr.Indicator.get_SMA(nasdaq_history, 5)
nasdaq_sma20 = fdr.Indicator.get_SMA(nasdaq_history, 20)

fdr.QouteHistory.add_column_by_day(apple_history, "nasdaq_ma5", nasdaq_sma5)
fdr.QouteHistory.add_column_by_day(apple_history, "nasdaq_ma20", nasdaq_sma20)

# example:
#               Open    High     Low   Close       Volume   per   pbr  nasdaq_ma5  nasdaq_ma20
# Date
# 2021-01-04  133.52  133.61  126.76  129.41  143300000.0  33.6  31.6   12841.274   12661.7955
# 2021-01-05  128.89  131.74  128.43  131.01   97670000.0  33.6  31.6   12825.182   12679.5320
# 2021-01-06  127.72  131.05  126.38  126.60  155090000.0  33.6  31.6   12803.296   12690.5740
```

If you want to save the data as a csv file, use `save_as_csv`
```
qh.save_as_csv(apple_history, "AAPL_2021_with_nasdaq_ma.csv")
```

## About the DLL
`Skender.Stock.Indicators.dll` is a compiled library package from [DaveSkender/Stock.Indicators](https://github.com/DaveSkender/Stock.Indicators).
It was written in C#, but it complies with the [Common Language Specification (CLS)](https://docs.microsoft.com/en-us/dotnet/standard/common-type-system), so it could be used as a Python module.

## References
 * [jimmysitu/morningstar.com API.md](https://gist.github.com/jimmysitu/161d2effc0d3b17e401fdafa6e5b615d)
