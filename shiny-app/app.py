import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, ui
from logical_components.classes import dochian_channel
from logical_components.func.get_data import get_data
import matplotlib.pyplot as plt
import numpy as np


ticker = "GBPUSD=X"
equity = 1000

df = get_data("2020-01-01","2021-01-01",ticker)

strategy = dochian_channel(df,equity)
strategy.simulate_trading()


app_ui = ui.page_fillable( 
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_selectize("ticker", "Ticker", choices=['GBPUSD=X','GBPEUR=X']),
            ui.input_date_range("daterange", "Date Range",start="2010-01-01", end="2024-01-01"),
            ui.input_numeric("initial_equity","Initial Equity",1000)
        ),
        ui.panel_main(
            ui.card(
                ui.card_header("Equity"),
                ui.value_box(title=None,value= ["equity"])
            ),
            ui.output_data_frame("df"),
        ),
    ),
) 


def server(input, output, session):
    @reactive.Calc
    def data():
        df = get_data(input.daterange()[0],input.daterange()[1],input.ticker())
        df['Date'] = pd.to_datetime(df['Date']).astype(str)
        df = dochian_channel(df,input.initial_equity())
        df.simulate_trading()

        return df


    @output
    @render.data_frame()
    def df():
        df = data().data
        return render.DataGrid(df,height="50rem")
    
    @output
    @render.text
    def equity():
        return ui.output_text(f"{data().equity}")
    
    
    


app = App(app_ui, server, debug=True)
