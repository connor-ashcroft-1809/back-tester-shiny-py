import yfinance as yf

def get_data(start_date,end_date,ticker):
    interval = "1d"
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval, progress=False).reset_index()
    return data
