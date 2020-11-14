import yahooFinance as Y

msft = Y.Ticker("TSLA")

# get stock info
print(tsla.info)

# get historical market data
hist = tsla.history(period="365d")
