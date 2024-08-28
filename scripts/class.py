import pandas as pd

#def Read_Raw_Data():
 #   return pd.read_csv('C:/Users/abenet/Desktop/data/raw_analyst_ratings.csv')



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
    def news_data(self):
        df=pd.read_csv('C:/Users/abenet/Desktop/data/raw_analyst_ratings.csv')
        df=df[(df['date']<=self.end)&(df['date']>=self.start)]
        df=df[df['stock']==self.ticker]
        return df
        

