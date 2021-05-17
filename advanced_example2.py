import clr
clr.AddReference(r'dll/Skender.Stock.Indicators')

import FinanceHistoryDataReader.QouteHistory as qh
import FinanceHistoryDataReader.Indicator as Indicator
import FinanceHistoryDataReader.processing as processing

# Fetching
print("Fetching OHLCV and other related price data...")
exxon_history = qh.get_history("XOM", "2010", market='XNYS', per=True, pbr=True)
nasdaq_history = qh.get_history("IXIC", "2010")
bond_u3y_history = qh.get_history('US3YT=X', "2010")
wti_history = qh.get_history("CL", "2010")


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
print("Merging data...(+ Technical Indicators)")
qh.add_column_by_day(exxon_history, "nasdaq_sma5", nasdaq_sma5)
qh.add_column_by_day(exxon_history, "nasdaq_sma20", nasdaq_sma20)
qh.add_column_by_day(exxon_history, "nasdaq_sma60", nasdaq_sma60)
qh.add_column_by_day(exxon_history, "nasdaq_sma120", nasdaq_sma120)
qh.add_column_by_day(exxon_history, "bond_u3y_sma5", bond_u3y_sma5)
qh.add_column_by_day(exxon_history, "bond_u3y_sma20", bond_u3y_sma20)
qh.add_column_by_day(exxon_history, "bond_u3y_sma60", bond_u3y_sma60)
qh.add_column_by_day(exxon_history, "bond_u3y_sma120", bond_u3y_sma120)
qh.add_column_by_day(exxon_history, "wti_sma5", wti_sma5)
qh.add_column_by_day(exxon_history, "wti_sma20", wti_sma20)
qh.add_column_by_day(exxon_history, "wti_sma60", wti_sma60)
qh.add_column_by_day(exxon_history, "wti_sma120", wti_sma120)

# Technical Indicators
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


# Post-processing
feature_list = [
    "nasdaq_sma5", "nasdaq_sma20", "nasdaq_sma60", "nasdaq_sma120", 
    "bond_u3y_sma5", "bond_u3y_sma20", "bond_u3y_sma60", "bond_u3y_sma120",
    "wti_sma5", "wti_sma20", "wti_sma60", "wti_sma120",   
    "aroon_5",
    "adx_5",
    "elder_ray_bull_5",
    "elder_ray_bear_5",
    "vortex_pos_5",
    "vortex_neg_5",
    "donchian_5",
    "fcb_upper_5",
    "fcb_lower_5",
    "gator_upper",
    "gator_lower",
    "alligator_jaw",
    "alligator_teeth",
    "alligator_lips",
    "ichimoku_9_26_52",
    "macd_12_26_9",
    "super_trend_14_3",
    "bollinger_bands_upper_20_2",
    "bollinger_bands_lower_20_2",
    "std_dev_channels_20_2",
]
for feature in feature_list:
    processing.standardize(exxon_history, feature)


# NLP(https://github.com/kwangwoon-sanhak/SentimentalAnalysis)
# ---------------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------------

# Save
exxon_history = exxon_history.dropna()
qh.save_as_csv(exxon_history, "XOM_2010_with_nasdaq_ma_bond_wti_NLP_TA.csv")

print(exxon_history)