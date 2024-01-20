import plotly.express as px
import pandas as pd
from shiny import App, reactive, ui
from shinywidgets import output_widget, render_widget
import yfinance as yf


app_ui = ui.page_sidebar( 
    ui.sidebar(ui.input_select( 
        "select", 
        "Select a ticker symbol:", 
        ["GBPUSD=X","GBPEUR=X","BTC-GBP"], 
    )), 
    output_widget("timeseries")
    
)

def server(input, output, session):
    @render_widget  
    def timeseries(): 
        ticker = input.select()
        start_date = "2021-01-01" 
        end_date = "2021-12-30"
        interval = "1d"

        df = yf.download(ticker, start=start_date, end=end_date, interval=interval).reset_index()
        scatterplot = px.line(
            data_frame=df, x="Date",y='Close'
        ).update_layout(
            title={"text": "Close", "x": 0.5},
            yaxis_title="Price",
            xaxis_title="Date"
        )

        return scatterplot  

app = App(app_ui, server)