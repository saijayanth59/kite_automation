import requests
import json
import pandas as pd
from datetime import datetime, timedelta

TIMEFRAME_LIMITS = {
    "day": 2000,
    "minute": 60,
    "5minute": 100,
    "15minute": 200,
}


def save_data_to_csv(raw_data, symbol, from_date, to_date, timeframe):
    try:
        data = raw_data.get("data", {}).get("candles", [])
        if not data:
            print("No data available.")
            return

        df = pd.DataFrame(
            data, columns=["Datetime", "Open", "High", "Low", "Close", "Volume", "OI"])

        df["Datetime"] = pd.to_datetime(df["Datetime"])
        df["Datetime"] = df["Datetime"].dt.tz_convert("Asia/Kolkata")

        df["Date"] = df["Datetime"].dt.date
        df["Time"] = df["Datetime"].dt.time

        filename = f"{symbol}_{from_date}_{to_date}_{timeframe}.csv"

        df.to_csv(f"onepiece/{filename}", index=False)

        print(f"Data saved successfully to {filename}")

    except Exception as e:
        print(f"Error processing data: {e}")


def fetch_historical_data(instrument_token, symbol):

    for timeframe in TIMEFRAME_LIMITS:
        end_date = datetime.today()
        start_date = end_date - timedelta(days=TIMEFRAME_LIMITS[timeframe] - 1)

        from_date = start_date.strftime("%Y-%m-%d")
        to_date = end_date.strftime("%Y-%m-%d")

        url = f"https://kite.zerodha.com/oms/instruments/historical/{
            instrument_token}/{timeframe}"

        params = {
            "user_id": "WF4546",
            "oi": "1",
            "from": from_date,
            "to": to_date,
        }

        headers = {
            "accept": "*/*",
            "authorization": "enctoken FEWYJQGzKD2lctDesKERduldq3pQw514i4jH4BsC/ZGolJBr93li5EzRwePkwP0Zgy5xUAkmCN3zBkl1nI84WgNrTHpRpaSMSLjARsWxiItsZJ03Azj4iA==",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        }

        response = requests.get(url, headers=headers, params=params)
        content = json.loads(response.content)
        save_data_to_csv(content, symbol, from_date, to_date, timeframe)


if __name__ == "__main__":
    symbol = input("Enter stock symbol: ")
    token = input("Enter stock token: ")
    fetch_historical_data(instrument_token=token, symbol=symbol)
