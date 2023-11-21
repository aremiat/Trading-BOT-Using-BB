class CasualBrownDonkey(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015, 1, 1)  # Set Start Date
        self.SetEndDate(2021, 1, 1)
        self.SetCash(100000)  # Set Strategy Cash

        self.eurusd = self.AddForex("EURUSD", Resolution.Daily, Market.Oanda).Symbol

        self.bb =self.BB(self.eurusd, 20, 2)

       
def OnData(self, data):

        if not self.bb.IsReady:
            return



        price = self.Securities[self.eurusd].Price

 
        if price > self.bb.UpperBand.Current.Value:
            if not self.Portfolio[self.eurusd].IsShort:
                self.SetHoldings(self.eurusd, -1)


        elif price < self.bb.LowerBand.Current.Value:
            if not self.Portfolio[self.eurusd].IsLong:
                self.SetHoldings(self.eurusd, 1)

        else:
            if price < self.bb.LowerBand.Current.Value and self.Portfolio[self.eurusd].IsShort:
                self.Liquidate()
            elif price > self.bb.UpperBand.Current.Value and self.Portfolio[self.eurusd].IsLong:
                self.Liquidate()
