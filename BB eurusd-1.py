def Initialize(self):

    self.SetStarDate(2010,1,1)
    self.SetEndDAte(2020,1,1)
    self.SetCash(100000)

    self.eurusd = self.AddForex("EURUSD", Resolution.Daily, Market.Oanda).Symbol
    self.bb = self.BB(self.eurusd, 20, 2)


def OnData(self, Data):

    if not self.bb.IsReady:
        return





price = self.Securities[self.eurusd].Price

 
if price > self.bb.UpperBand.Current.Value:
    if not self.Portfolio[self.spy].IsShort:
        self.SetHoldings(self.spy, -1)




    elif price < self.bb.LowerBand.Current.Value:
        if not self.Portfolio[self.spy].IsLong:
            self.SetHoldings(self.spy, 1)



    else:
        if self.Portfolio[self.eurusd].IsLong:
            if price > self.bb.MiddleBand.Current.Value:
                self.Liquidate()


        elif self.Portfolio[self.eurusd].IsShort:
            if price < self.bb.MiddleBand.Current.Value:
                self.Liquidate()

self.Plot("Trade Plot", "Price", price)
self.Plot("Trade Plot", "MiddleBand", self.bb.MiddleBand.Current.Value)
self.Plot("Trade Plot", "UpperBand", self.bb.UpperBand.Current.Value)
self.Plot("Trade Plot", "LowerBand", self.bb.LowerBand.Current.Value)




