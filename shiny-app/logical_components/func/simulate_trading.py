import pandas as pd
import math

def open_long(self,close,date):
    self.open = close
    self.in_position = 1
    self.open_date = date

def close_long(self,close,date):
    self.close = close
    self.equity += self.equity * ((self.close-self.open)/self.open)
    self.in_position = 0
    self.close_date = date
    self.trading_history.append(["Long",[self.open_date,self.open],[self.close_date,self.close]])


def open_short(self,close,date):
    self.open = close
    self.in_position = -1
    self.open_date = date

def close_short(self,close,date):
    self.close = close
    self.equity +=  self.equity * -((self.close-self.open)/self.open)
    self.in_position = 0
    self.close_date = date
    self.trading_history.append(["Short",[self.open_date,self.open],[self.close_date,self.close]])


def simulate_trading_(self):
    for date, row in self.data.iterrows():

        signal = row['signal']
        close = row['close']

        if signal == "buy":

            if self.in_position == 0:
                open_long(self,close,date)

            if self.in_position == -1:
                close_short(self,close,date)

        elif signal == "sell":

            if self.in_position == 0:
                open_short(self,close,date)

            if self.in_position == 1:
                close_long(self,close,date)

                
    
    if self.in_position == 1:
        close_long(self,close,date)

    if self.in_position == -1:
        close_short(self,close,date)
