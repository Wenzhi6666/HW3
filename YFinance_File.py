import numpy as np
import yfinance as yf
import pandas as pd

def YahooData2returns(YahooData):
    prices = YahooData['Adj Close'].values  
    returns = prices[1:] / prices[:-1] - 1  
    return returns
    
    # Yahoo Data = raw downloaded data from Yahoo Finance using yfinance
    # returns = % returns of 'Adj Close' as a data vector (not a data frame)
    
    '''
    # Practice data for unit test
    d = {   'Open': [100, 102, 101, 103],
        'High': [105, 104, 103, 105],
        'Low': [98, 100, 99, 101],
        'Close': [101, 103, 102, 104],
        'Adj Close': [101, 103, 102, 104],
        'Volume': [1000, 1200, 900, 1100]}

    index = pd.to_datetime(['2023-10-26', '2023-10-27', '2023-10-28', '2023-10-29'])
    tempdata = pd.DataFrame(d, index=index)
    

    returns = np.array([ 0.01980198, -0.00970874,  0.01960784])
    return returns
    '''
    

