from lib import ohlcv_to_csv as csv
from lib.MorningStarCrawler import MorningStarCrawler

MorningStarCrawler().get("AAPL", "XNAS")

#csv.ohlcv_to_csv("AAPL", "2021-03-01", "2021-03-09")
# Output Example:
#               Open    High     Low   Close       Volume
# Date
# 2021-03-01  123.75  127.93  122.79  127.79  116310000.0



