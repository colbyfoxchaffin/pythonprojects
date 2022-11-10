"""
In this finance data project I focus on exploratory data analysis of stock prices. Please be aware that this project is just a means to practice data visualization and pandas skills, it is not meant to be a robust financial analysis or be taken as financial advice.

Author: Colby Chaffin
"""

#Imports
from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
from matplotlib import inline

"""Using pandas datareader, get the stock information for the following banks:
    - Bank of America
    - CitiGroup
    - Goldman Sachs
    - JPMorgan Chase
"""
start = datetime.datetime(2006,1,1)
end = datetime.datetime(2016,1,1)

# Bank of America
BAC = data.DataReader("BAC", 'google', start, end)

# CitiGroup
C = data.DataReader("C", 'google', start, end)

# Goldman Sachs
GS = data.DataReader("GS", 'google', start, end)

# JPMorgan Chase
JPM = data.DataReader("JPM", 'google', start, end)

# Morgan Stanley
MS = data.DataReader("MS", 'google', start, end)

# Wells Fargo
WFC = data.DataReader("WFC", 'google', start, end)