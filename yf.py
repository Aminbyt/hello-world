import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
btc = yf.download("BTC-USD")
df = pd.DataFrame(btc)

print(btc.corr())

plt.plot(df)
plt.show()