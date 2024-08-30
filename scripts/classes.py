import pandas as pd
import plotly.express as px
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
    def plot_macd(self, df):
        fig = px.line(df, x=df.index, y=['MACD', 'MACD_Signal'], title='Moving Average Convergence Divergence')
        fig.show()
        


        

