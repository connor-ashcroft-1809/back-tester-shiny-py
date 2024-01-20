import pandas as pd
import pandas_ta as ta

def add_indicator(df):
    df[['dcl', 'dcm', 'dcu']] = df.ta.donchian(lower_length = 10, upper_length = 10)
    df.columns = list(df.columns.str.lower())
    df = df.set_index('date')
    df.index = pd.to_datetime(df.index)
    return df


def generate_signals(row):
    if row['high'] >= row['dcu']:
        return "buy"
    
    elif row['low'] <= row['dcl']:
        return "sell"
    
    else:
        return "hold"
    

def generate_signals_dochian_channel_strat(df):
    df = add_indicator(df)
    df['signal'] = df.apply(generate_signals,axis=1)
    return df


