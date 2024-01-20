import yfinance as yf

# Define the ticker, start and end dates, and interval
#ticker = "MAERSK-B.CO"  # Replace with the desired ticker symbol
#start_date = "2021-01-01"  # Replace with the desired start date
#end_date = "2021-12-30"   # Replace with the desired end date
#interval = "1d"  # Valid intervals include 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo

def get_data_yfinance(ticker,start_date,end_date,interval):
    # Download the data using yfinance's download function
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval).reset_index()
    return data
