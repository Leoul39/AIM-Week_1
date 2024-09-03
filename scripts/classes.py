import pandas as pd
import matplotlib.pyplot as plt
import talib as ta
import numpy as np


#def Read_Raw_Data():
 #   return pd.read_csv('C:/Users/abenet/Desktop/data/raw_analyst_ratings.csv')



class DataAnalyzer:
    def __init__(self,ticker,start,end):
        self.ticker=ticker
        self.start=start
        self.end=end
    def news_data(self):
        df=pd.read_csv('C:/Users/abenet/Desktop/data/raw_analyst_ratings.csv')
        df['date']=pd.to_datetime(df['date'],errors='coerce',utc=True)
        df=df[(df['date']<=self.end)&(df['date']>=self.start)]
        df=df[df['stock']==self.ticker]
        return df
    
class FinancialAnalyzer:
    def __init__(self,ticker,start,end):
        self.ticker=ticker
        self.start=start
        self.end=end
    def ticker_data(self):
        location='C:/Users/abenet/Desktop/data/yfinance_data/'+self.ticker+'_historical_data.csv'
        df=pd.read_csv(location)
        df=df[(df['Date']<=self.end)&(df['Date']>=self.start)]
        return df
    def technical_indicators(self, df):
        df['SMA'] = ta.SMA(np.array(df['Close']))
        df['RSI'] = ta.RSI(df['Close'], timeperiod=14)
        df['EMA'] = ta.EMA(df['Close'], timeperiod=20)
        macd, macd_signal, _ = ta.MACD(df['Close'])
        df['MACD'] = macd
        df['MACD_Signal'] = macd_signal
        return df
    def plot_sma(self, data):
        fig,ax=plt.subplots(2,figsize=(20,6))
        ax[0].plot(data['date'],data['Close'])
        ax[0].set_title('Closing Price')
        ax[1].plot(data['date'],data['SMA'])
        ax[1].set_title('Simple Moving Average over time ')
        plt.tight_layout()
        plt.legend()
        plt.show()


    def plot_rsi(self, data):
        fig,ax=plt.subplots(2,figsize=(20,6))
        ax[0].plot(data['date'],data['Close'])
        ax[0].set_title('Closing Price')
        ax[1].plot(data['date'],data['RSI'])
        ax[1].set_title('Relative Strength Index over time ')
        plt.tight_layout()
        plt.legend()
        plt.show()

    def plot_ema(self, data):
        fig,ax=plt.subplots(2,figsize=(20,6))
        ax[0].plot(data['date'],data['Close'])
        ax[0].set_title('Closing Price')
        ax[1].plot(data['date'],data['EMA'])
        ax[1].set_title('Exponential Moving Average over time ')
        plt.tight_layout()
        plt.legend()
        plt.show()


    def plot_macd(self, data):
        fig,ax=plt.subplots(2,figsize=(20,6))
        ax[0].plot(data['date'],data['Close'])
        ax[0].set_title('Closing Price')
        ax[1].plot(data['date'],data['MACD'],label='MACD')
        ax[1].plot(data['date'],data['MACD_Signal'],label='MACD Signal line')
        ax[1].set_title('Moving Average Convergence Divergence over time ')
        plt.tight_layout()
        plt.legend()
        plt.show()

        


        

