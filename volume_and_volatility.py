import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Asus\Desktop\ML\AI-ML-DS\data\ethereum_ohlcv_sample.csv", parse_dates = ['Date'])

df = df.sort_values("Date").reset_index(drop = True)    


short_period = 5

long_period = 10

df['Vol_MA_Short'] = df['Volume'].rolling(window = short_period).mean()

df['Vol_MA_Long'] = df['Volume'].rolling(window= long_period).mean()

df['Volume_Oscillator'] = ((df['Vol_MA_Short'] - df['Vol_MA_Long']) /df['Vol_MA_Long']) * 100

#Average True Range(ATR)
df['High-Low'] = df['High'] - df['Low']
df['High-Close'] = np.abs(df['High'] - df['Close'].shift(1))
df['Low-Close'] = np.abs(df['Low'] - df['Close'].shift(1))
df["True_Range"] = df[['High-Low', 'High-Close', 'Low-Close']].max(axis = 1)
df['ATR'] = df['True_Range'].rolling(window = 14).mean()

# Volume to Volatility Ratio

df['Volatility_Score'] = df['Volume'] / df['ATR']

# Plot

plt.figure(figsize = (14,8))

#Subplot 1: Price

plt.subplot(3,1,1)
plt.plot(df['Date'], df["Close"], label = 'Close Price')
plt.title("Price Chart")
plt.legend()

#VOlume Oscillator

plt.subplot(3,1,2)

plt.plot(df['Date'], df['Volume_Oscillator'], color = 'orange', label = 'VOlume Oscillator')
plt.axhline(0, color='gray', linestyle='--')
plt.legend()

# Subplot 3: Volume to Volatility Ratio
plt.subplot(3, 1, 3)
plt.plot(df['Date'], df['Volatility_Score'], color='green', label='Volume/ATR (Volatility Score)')
plt.title('Volume to Volatility Ratio')
plt.legend()

plt.tight_layout()
plt.show()

