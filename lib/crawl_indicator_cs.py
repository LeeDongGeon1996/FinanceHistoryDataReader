import clr
clr.AddReference('Skender.Stock.Indicators')

from Skender.Stock.Indicators import Indicator
Indicator.GetSma(None, 20);