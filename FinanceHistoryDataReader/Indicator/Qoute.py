# C-Sharp Modules
from Skender.Stock.Indicators import Quote
from System import DateTime, Decimal

class Qoute(Quote):
    def __init__(self, pandasSeries):
        t = str(pandasSeries.name)[:10].split("-")
        self.Date = DateTime(int(t[0]), int(t[1]), int(t[2]))
        self.Open = Decimal(float(pandasSeries["open"]))
        self.High = Decimal(float(pandasSeries["high"]))
        self.Low = Decimal(float(pandasSeries["low"]))
        self.Close = Decimal(float(pandasSeries["close"]))
        self.Volume = Decimal(float(pandasSeries["volume"]))
