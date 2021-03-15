# FinanceHistoryDataReader

## Requirements
```
pip install finance-datareader, pythonnet, beautifulsoup4, requests, pandas
```

## Usage
You can simply save historical price quotes to csv file using `indicators_to_csv`
```
# Amazon(AMZN), Whole period
indicators_to_csv('AMZN')

# Microsoft(MSFT) 2021-02-14 ~ Now
indicators_to_csv("MSFT", "2021-02-14")

# Apple(AAPL) 2021-03-01 ~ 2021-03-09
indicators_to_csv("AAPL", "2021-03-01", "2021-03-09")

# With PER, PBR, ROE, Apple(AAPL) 2019-01-01 ~ Now
csv.ohlcv_to_csv("AAPL", "2019", per=True, pbr=True, roe=True)

# Reorder columns, Facebook(FB) 2019-01-01 ~ Now
csv.ohlcv_to_csv("FB", "2019-01-01", per=True, order=['per', 'Open', 'High', 'Low', 'Close', 'Volume'])

# Print dataframe, Netflix(NFLX) 2021-01-01 ~ 2021-01-29
csv.ohlcv_to_csv("NFLX", "2021-01-01", "2021-01-29", print=True)
```

## About the DLL
`Skender.Stock.Indicators.dll` is a compiled library package from [DaveSkender/Stock.Indicators](https://github.com/DaveSkender/Stock.Indicators).
It was written in C#, but it complies with the [Common Language Specification (CLS)](https://docs.microsoft.com/en-us/dotnet/standard/common-type-system), so it could be used as a Python module.

## References
 * [jimmysitu/morningstar.com API.md](https://gist.github.com/jimmysitu/161d2effc0d3b17e401fdafa6e5b615d)
