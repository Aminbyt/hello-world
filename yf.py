#show BTC in plot
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
btc = yf.download("BTC-USD")
df = pd.DataFrame(btc)

print(btc.corr())

plt.plot(df , labale = 'BTC-USD' , color = 'black')
plt.show()

#bar plot
plt.bar(df , color = 'blue')
