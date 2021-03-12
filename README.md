# Usage
You can simply save historical price quotes to csv file using `indicators_to_csv`
```
# Amazon(AMZN), Whole period
indicators_to_csv('AMZN')

# Microsoft(MSFT) 2021-02-14 ~ Now
indicators_to_csv("MSFT", "2021-02-14")

# Apple(AAPL) 2021-03-01 ~ 2021-03-09
indicators_to_csv("AAPL", "2021-03-01", "2021-03-09")
```

