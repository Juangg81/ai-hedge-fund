import yfinance as yf
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import List
from models import Price


def df_to_prices(df: pd.DataFrame) -> List[Price]:
    """Convert a DataFrame to a list of Price objects."""
    prices = []
    for index, row in df.iterrows():
        try:
            price = Price(open=float(row["open"]), close=float(row["close"]), high=float(row["high"]), low=float(row["low"]), volume=int(row["volume"]), time=str(index))  # Assuming index is the date/time
            prices.append(price)
        except (ValueError, KeyError) as e:
            print(f"Error processing row {index}: {e}")
            continue  # Skip rows with missing or invalid data
    return prices


# formats DF to native expected format by AI hedge fund
def get_prices(ticker: str, start_date: str, end_date: str) -> list[Price]:
    """Fetch price data from cache or API."""
    prices_df = get_price_data(ticker, start_date, end_date)
    prices = df_to_prices(prices_df)
    if not prices:
        prices = []
    return prices


# get price data from Yahoo Finance in DF
def get_price_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    stock = yf.Ticker(ticker)
    stock_historical = stock.history(start=start_date, end=end_date, interval="1d")
    stock_historical.columns = stock_historical.columns.str.lower()

    return stock_historical


def main():

    ticker = "AAPL"
    end_date = datetime.now().strftime("%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    start_date = (end_date_obj - relativedelta(months=3)).strftime("%Y-%m-%d")
    end_date = end_date_obj + relativedelta(days=1)

    # print(stock.info["regularMarketPrice"])

    # original = get_price_data(ticker=ticker, start_date=start_date, end_date=end_date)
    # print(type(original))
    # print(original)

    original2 = get_prices(ticker=ticker, start_date=start_date, end_date=end_date)
    print(type(original2))
    print(original2)
    # print(stock.info)
    # add data form today using .info

    # print(type(stock_historical))
    # print(stock_historical)


if __name__ == "__main__":
    print("Information from yahoo!")
    print("Documentation: https://github.com/ranaroussi/yfinance")
    main()  # call the user code above
