import pandas as pd
import yfinance as yf

# Define ticker symbol
ticker_symbol = "NVDA"

# Download latest data
nvda = yf.Ticker(ticker_symbol)

# Get the latest market data (last 1 day)
data = nvda.history(period="1d")

# Extract the latest close price
latest_price = data['Close'].iloc[-1]

# Create a pandas DataFrame
df = pd.DataFrame({
    "Ticker": [ticker_symbol],
    "Latest Price": [latest_price]
})

print(df)

# Optional: save to CSV or Excel
df.to_csv("nvda_price.csv", index=False)
df.to_excel("nvda_price.xlsx", index=False)
