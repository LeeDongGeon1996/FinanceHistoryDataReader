from lib import ohlcv_to_csv as csv
from lib.MorningStarCrawler import MorningStarCrawler

csv.ohlcv_to_csv("AAPL", "2019-01-01", "2019-01-29", per=True, pbr=True, roe=True, print=True)



