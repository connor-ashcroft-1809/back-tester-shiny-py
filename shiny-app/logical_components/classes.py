import pandas as pd
from logical_components.func.simulate_trading import simulate_trading_
from logical_components.func.dochian_channel import generate_signals_dochian_channel_strat


class BaseStrategy:
    def __init__(self, data, initial_equity):
        self.data = data.copy()
        self.initial_equity = initial_equity
        self.equity = self.initial_equity
        self.open = 0
        self.close = 0
        self.open_date = ""
        self.close_date = ""
        self.in_position = 0
        self.trading_history = []


    def generate_signals(self):
        raise NotImplementedError("Implement this method in subclasses")
    
    def simulate_trading(self):
        # 1. Generate buy/sell signals (abstract method, implemented in subclasses)
        self.generate_signals()
        simulate_trading_(self)

class dochian_channel(BaseStrategy):
    def generate_signals(self):
        self.data = generate_signals_dochian_channel_strat(self.data)