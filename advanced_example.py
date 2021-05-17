import clr
clr.AddReference(r'dll/Skender.Stock.Indicators')

import FinanceHistoryDataReader.QouteHistory as qh
import FinanceHistoryDataReader.Indicator as Indicator
import FinanceHistoryDataReader.processing as processing

##############################
TICKER = "XOM"

MARKET = "XNYS"
MARKET_NAME = "nyse"
MARKET_TICKER = "IXIC"

YEAR_FROM = "2020"

WTI_ENABLE = True
NLP_ENABLE = False
##############################
feature_list = []

# Fetching
print("Fetching OHLCV and other related price data...")
price_history = qh.get_history(TICKER, YEAR_FROM, market=MARKET, per=True, pbr=True)

# Technical Indicators
qh.add_column_by_day(price_history, "aroon_5", Indicator.get_AROON(price_history, 5))
qh.add_column_by_day(price_history, "adx_5", Indicator.get_ADX(price_history, 5))
qh.add_column_by_day(price_history, "elder_ray_bull_5", Indicator.get_elder_ray_bull(price_history, 5))
qh.add_column_by_day(price_history, "elder_ray_bear_5", Indicator.get_elder_ray_bear(price_history, 5))
qh.add_column_by_day(price_history, "vortex_pos_5", Indicator.get_vortex_positive(price_history, 5))
qh.add_column_by_day(price_history, "vortex_neg_5", Indicator.get_vortex_negative(price_history, 5))
qh.add_column_by_day(price_history, "donchian_5", Indicator.get_donchian(price_history, 5))
qh.add_column_by_day(price_history, "fcb_upper_5", Indicator.get_fcb_upper(price_history, 5))
qh.add_column_by_day(price_history, "fcb_lower_5", Indicator.get_fcb_lower(price_history, 5))

qh.add_column_by_day(price_history, "gator_upper", Indicator.get_gator_upper(price_history))
qh.add_column_by_day(price_history, "gator_lower", Indicator.get_gator_lower(price_history))
qh.add_column_by_day(price_history, "alligator_jaw", Indicator.get_alligator_jaw(price_history))
qh.add_column_by_day(price_history, "alligator_teeth", Indicator.get_alligator_teeth(price_history))
qh.add_column_by_day(price_history, "alligator_lips", Indicator.get_alligator_lips(price_history))

qh.add_column_by_day(price_history, "ichimoku_9_26_52", Indicator.get_ichimoku(price_history, 9, 26, 52))
qh.add_column_by_day(price_history, "macd_12_26_9", Indicator.get_macd(price_history, 12, 26, 9))
qh.add_column_by_day(price_history, "super_trend_14_3", Indicator.get_super_trend(price_history, 14,3))
qh.add_column_by_day(price_history, "bollinger_bands_upper_20_2", Indicator.get_bollinger_bands_upper(price_history, 20,2))
qh.add_column_by_day(price_history, "bollinger_bands_lower_20_2", Indicator.get_bollinger_bands_lower(price_history, 20,2))
qh.add_column_by_day(price_history, "std_dev_channels_20_2", Indicator.get_std_dev_channels(price_history, 20,2))

# Market Moving Avg
print(f"Calculating Market({MARKET_NAME}) Moving Avg...")
market_history = qh.get_history(MARKET_TICKER, YEAR_FROM)
market_sma5 = Indicator.get_SMA(market_history, 5)
market_sma20 = Indicator.get_SMA(market_history, 20)
market_sma60 = Indicator.get_SMA(market_history, 60)
market_sma120 = Indicator.get_SMA(market_history, 120)

qh.add_column_by_day(price_history, "market_sma5", market_sma5)
qh.add_column_by_day(price_history, "market_sma20", market_sma20)
qh.add_column_by_day(price_history, "market_sma60", market_sma60)
qh.add_column_by_day(price_history, "market_sma120", market_sma120)

# U.S bond Moving Avg
print("Calculating U.S bond Moving Avg...")
bond_u3y_history = qh.get_history('US3YT=X', YEAR_FROM)
bond_u3y_sma5 = Indicator.get_SMA(bond_u3y_history, 5)
bond_u3y_sma20 = Indicator.get_SMA(bond_u3y_history, 20)
bond_u3y_sma60 = Indicator.get_SMA(bond_u3y_history, 60)
bond_u3y_sma120 = Indicator.get_SMA(bond_u3y_history, 120)

qh.add_column_by_day(price_history, "bond_u3y_sma5", bond_u3y_sma5)
qh.add_column_by_day(price_history, "bond_u3y_sma20", bond_u3y_sma20)
qh.add_column_by_day(price_history, "bond_u3y_sma60", bond_u3y_sma60)
qh.add_column_by_day(price_history, "bond_u3y_sma120", bond_u3y_sma120)

# WTI Moving Avg
if WTI_ENABLE:
    print("Calculating WTI Moving Avg...")
    wti_history = qh.get_history("CL", YEAR_FROM)
    wti_sma5 = Indicator.get_SMA(wti_history, 5)
    wti_sma20 = Indicator.get_SMA(wti_history, 20)
    wti_sma60 = Indicator.get_SMA(wti_history, 60)
    wti_sma120 = Indicator.get_SMA(wti_history, 120)
        
    qh.add_column_by_day(price_history, "wti_sma5", wti_sma5)
    qh.add_column_by_day(price_history, "wti_sma20", wti_sma20)
    qh.add_column_by_day(price_history, "wti_sma60", wti_sma60)
    qh.add_column_by_day(price_history, "wti_sma120", wti_sma120)

# Post-processing
print("Post-processing data...")
feature_list += [
    "market_sma5", "market_sma20", "market_sma60", "market_sma120", 
    "bond_u3y_sma5", "bond_u3y_sma20", "bond_u3y_sma60", "bond_u3y_sma120",  
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
if WTI_ENABLE:
    feature_list += [ "wti_sma5", "wti_sma20", "wti_sma60", "wti_sma120" ]

for feature in feature_list:
    processing.standardize(price_history, feature)


# NLP(https://github.com/kwangwoon-sanhak/SentimentalAnalysis)
if NLP_ENABLE:
    print("Starting NLP...")
    from calculate_sentiment_score.calculate_sent_score import VocabDictionary
    vocab_dic = VocabDictionary("VADER")
    score = vocab_dic.sentiment_analysis()

    qh.add_column_by_day(price_history, "nlp_pos", score['pos'])
    qh.add_column_by_day(price_history, "nlp_neg", score['neu'])
    qh.add_column_by_day(price_history, "nlp_neu", score['neg'])
    qh.add_column_by_day(price_history, "nlp_compound", score['compound'])
    print("NLP finished.")

    print("Filling NAN...")
    qh.fill_nan(price_history, "nlp_pos")
    qh.fill_nan(price_history, "nlp_neg")
    qh.fill_nan(price_history, "nlp_neu")
    qh.fill_nan(price_history, "nlp_compound")


# Save
price_history = price_history.dropna()

file_name = f"{TICKER}_{YEAR_FROM}_with_{MARKET_NAME}_TA"
if WTI_ENABLE:
    file_name += "_wti"

if NLP_ENABLE:
    file_name += "_nlp"

qh.save_as_csv(price_history, f"{file_name}.csv")

print(price_history)