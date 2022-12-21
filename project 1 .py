import datetime
import pandas_datareader as pdr
import numpy as np
import pandas as pd
import web
import yfinance as yf
import datetime as dt
#Primary Objective: complete all the steps below and return the risk analysis
# #against the S&P500 (SPY), Russell 2000 (IWM), and the Dow Jones Industrial
#
#
import pandas as pd # Importing Pandas library for data cleaning and m
import yfinance as yf # Importing our stock parameters using yahoo finance
import datetime as dt
import numpy as np
import seaborn as sns
 # Setting tickers according to the 7 chosen stocks against:
#S&P500 (SPY)
#Russell2000 (IWM)
 # Dow Jones Industrial Average (DIA)
start = dt.datetime(2012, 10, 10)
#
ticker_list = ['NVDA', 'AMZN', 'MRNA', 'TSLA', 'ADBE', 'META', 'GME']
ticker_list2 = ['NVDA', 'AMZN', 'MRNA', 'TSLA', 'ADBE', 'META', 'GME', '^GSPC', '^RUT', '^DJI']
temp_list = [1, 2, 3, 4, 5, 6, 7]
p_weight = [(1/7), (1/7), (1/7), (1/7), (1/7), (1/7), (1/7)]
tickersize = len(ticker_list)
tempsize = len(temp_list)
data = yf.download(ticker_list, start = '2022-07-10', end = '2022-10-10')
data_ticker = yf.Ticker("NVDA")
Close = data.Close

log_returns = np.log(Close/Close.shift())
log_returns = log_returns.std()
volatility = log_returns*252**.5

data12mo = yf.download(ticker_list2, start = '2021-10-10', end = '2022-10-10')
datamol = yf.download(ticker_list, start = '2021-10-10', end = '2022-10-10')
data12mo = data12mo['Adj Close']
log_returns2 = np.log(data12mo/data12mo.shift())
cov = log_returns2.cov()
var = log_returns2['^GSPC'].var()
var2 = log_returns2['^RUT'].var()
var3 = log_returns2['^DJI'].var()
BETA1 = cov.loc['^GSPC']/var
BETA2 = cov.loc['^RUT']/var
BETA3 = cov.loc['^DJI']/var

#----------------------------------------------------------------------------------------------

SPY_Dat = pdr.DataReader('SPY', 'yahoo', datetime.date(2007,1,1),datetime.date(2022,1,1))

#We are going to use a trailing 252 trading day window
window = 252

#Calculate the max drawdown in the past window days for each day in the series.
#Use min_periods=1 if you want to let the first 252 days data have an expanding window
Roll_Max = datamol['Adj Close'].rolling(window, min_periods=1).max()
#drawdown0 = datamol['Adj Close']/Roll_Max - 1.0

#Next we calculate the minimum (negative) daily drawdown in that window.
#Again, use min_periods=1 if you want to allow the expanding window
#maxdrawdown0 = drawdown0.rolling(window, min_periods=1).min()
#--------------------------------------------------------------------------------------------

#drawdown = sum(drawdown0)/len(drawdown0)
#maxdrawdown = sum(maxdrawdown0)/len(maxdrawdown0)

data10yr = yf.download(ticker_list, start = '2012-10-10', end = '2022-10-10')

total_return = np.sum(np.log(data10yr/data10yr.shift()))

meta = yf.Ticker ("META")
aapl = yf.Ticker("AAPL")
googl = yf.Ticker("GOOGL")
tsla = yf.Ticker("TSLA")
nvda = yf.Ticker("NVDA")
amzn = yf.Ticker("AMZN")

meta_summary = meta.info
#listThis is a sample Python script.

#Press Shift+F10 to execute it or replace it with your code.
#Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
