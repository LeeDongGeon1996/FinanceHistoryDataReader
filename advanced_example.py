import clr
clr.AddReference(r'dll/Skender.Stock.Indicators')

import FinanceHistoryDataReader.QouteHistory as qh
import FinanceHistoryDataReader.Indicator as Indicator
import FinanceHistoryDataReader.processing as processing

# Fetching
exxon_history = qh.get_history("XOM", "2010", market='XNYS', per=True, pbr=True)
nasdaq_history = qh.get_history("IXIC", "2010")
bond_u3y_history = qh.get_history('US3YT=X', "2010")
wti_history = qh.get_history("CL", "2010")
print("OHLCV and other related price data are fetched.")

# Nasdaq Moving Avg
print("Calculating Nasdaq Moving Avg...")
nasdaq_sma5 = Indicator.get_SMA(nasdaq_history, 5)
nasdaq_sma20 = Indicator.get_SMA(nasdaq_history, 20)
nasdaq_sma60 = Indicator.get_SMA(nasdaq_history, 60)
nasdaq_sma120 = Indicator.get_SMA(nasdaq_history, 120)

# U.S bond Moving Avg
print("Calculating U.S bond Moving Avg...")
bond_u3y_sma5 = Indicator.get_SMA(bond_u3y_history, 5)
bond_u3y_sma20 = Indicator.get_SMA(bond_u3y_history, 20)
bond_u3y_sma60 = Indicator.get_SMA(bond_u3y_history, 60)
bond_u3y_sma120 = Indicator.get_SMA(bond_u3y_history, 120)

# WTI Moving Avg
print("Calculating WTI Moving Avg...")
wti_sma5 = Indicator.get_SMA(wti_history, 5)
wti_sma20 = Indicator.get_SMA(wti_history, 20)
wti_sma60 = Indicator.get_SMA(wti_history, 60)
wti_sma120 = Indicator.get_SMA(wti_history, 120)

# Attach data to data frame
print("Merging data...")
qh.add_column_by_day(exxon_history, "nasdaq_ma5", nasdaq_sma5)
qh.add_column_by_day(exxon_history, "nasdaq_ma20", nasdaq_sma20)
qh.add_column_by_day(exxon_history, "nasdaq_ma60", nasdaq_sma60)
qh.add_column_by_day(exxon_history, "nasdaq_ma120", nasdaq_sma120)
qh.add_column_by_day(exxon_history, "bond_u3y_ma5", bond_u3y_sma5)
qh.add_column_by_day(exxon_history, "bond_u3y_ma20", bond_u3y_sma20)
qh.add_column_by_day(exxon_history, "bond_u3y_ma60", bond_u3y_sma60)
qh.add_column_by_day(exxon_history, "bond_u3y_ma120", bond_u3y_sma120)
qh.add_column_by_day(exxon_history, "wti_ma5", wti_sma5)
qh.add_column_by_day(exxon_history, "wti_ma20", wti_sma20)
qh.add_column_by_day(exxon_history, "wti_ma60", wti_sma60)
qh.add_column_by_day(exxon_history, "wti_ma120", wti_sma120)

# Post-processing
processing.standardize(exxon_history, "nasdaq_ma5")
processing.standardize(exxon_history, "nasdaq_ma20")
processing.standardize(exxon_history, "nasdaq_ma60")
processing.standardize(exxon_history, "nasdaq_ma120")
processing.standardize(exxon_history, "bond_u3y_ma5")
processing.standardize(exxon_history, "bond_u3y_ma20")
processing.standardize(exxon_history, "bond_u3y_ma60")
processing.standardize(exxon_history, "bond_u3y_ma120")
processing.standardize(exxon_history, "wti_ma5")
processing.standardize(exxon_history, "wti_ma20")
processing.standardize(exxon_history, "wti_ma60")
processing.standardize(exxon_history, "wti_ma120")


# NLP(https://github.com/kwangwoon-sanhak/SentimentalAnalysis)
print("Starting NLP...")
from calculate_sentiment_score.calculate_sent_score import VocabDictionary
vocab_dic = VocabDictionary("VADER")
score = vocab_dic.sentiment_analysis()

qh.add_column_by_day(exxon_history, "nlp_pos", score['pos'])
qh.add_column_by_day(exxon_history, "nlp_neg", score['neu'])
qh.add_column_by_day(exxon_history, "nlp_neu", score['neg'])
qh.add_column_by_day(exxon_history, "nlp_compound", score['compound'])
print("NLP finished.")

print("Filling NAN...")
qh.fill_nan(exxon_history, "nlp_pos")
qh.fill_nan(exxon_history, "nlp_neg")
qh.fill_nan(exxon_history, "nlp_neu")
qh.fill_nan(exxon_history, "nlp_compound")

# Save
qh.save_as_csv(exxon_history, "XOM_2010_with_nasdaq_ma_bond_wti_NLP.csv")

print(exxon_history)