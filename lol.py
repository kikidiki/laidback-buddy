import requests

class Stocks:
    def __init__(self):
        self.symbol = input("Enter the ticker symbol: ")

    @staticmethod
    def get_stock_price(api_key, symbol):
        base_url = "https://www.alphavantage.co/query"
        function = "TIME_SERIES_INTRADAY"
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

def stock_price():

    api_key = 'YOUR_API_KEY_HERE'  # Replace with your Alpha Vantage API key

    # Create an instance of the Stocks class
    stock = Stocks()

    # Call the static method using the instance and symbol
    stock_price = stock.get_stock_price(api_key, stock.symbol)

    if isinstance(stock_price, float):
        print(f"{stock.symbol} stock price: ${stock_price:.2f}")
    else:
        print(stock_price)


if __name__ == "__main__":
    stock_price()