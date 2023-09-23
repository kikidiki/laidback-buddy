import requests


def get_aapl_stock_price(api_key):
    base_url = "https://www.alphavantage.co/query"
    function = "TIME_SERIES_INTRADAY"
    symbol = "AAPL"
    interval = "1min" 

    params = {
        "function": function,
        "symbol": symbol,
        "interval": interval,
        "apikey": api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        latest_time = max(data["Time Series (1min)"].keys())
        price = data["Time Series (1min)"][latest_time]["4. close"]
        return float(price)
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    api_key = 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the ' \
              'visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used ' \
              'as a placeholder before final copy is available. Wikipedia'

    aapl_price = get_aapl_stock_price(api_key)
    if isinstance(aapl_price, float):
        print(f"Apple Inc. (AAPL) stock price: ${aapl_price:.2f}")
    else:
        print(aapl_price)
