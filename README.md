# Financial Analysis
## Project Overview
This project focusus on finanical analysis and sentiment relation. The ticker specifically used for the whole project is `AAPL` stock data. The project tries to make a correlation between the closing stock data and the stock news headline released for that day.
## Project Objectives
1. Analyze and calculate the headline length for each headline released.
2. Examine the publishers with the most headlines published.
3. Calculate the sentiment score for each headline in the `AAPL` stock. 
4. Saw the days where most headlines are published.
5. Made a correlation matrix relating the `Close` price, technical indicators and sentiment score. 
6. Plotted some graphs for the technical indicators and the `Close` price.
## Project Challenges
1. **Time:** The limited time given to the project hinders further analysis.
2. **Experience:** The libraries that are mandatory to the project are new and fairly hard.
3. **Data Quality:** Especially the data column contained various types of date making the analysis hard.
## Sentiment Analysis
The code snippet for the sentiment analysis can be shown below.
```python
news_df=news_df[news_df['stock']=='AAPL']
sia=SentimentIntensityAnalyzer()
news_df['sentiment'] = news_df['headline'].apply(lambda x: sia.polarity_scores(text=x)['compound'])
news_df['sentiment_category'] = pd.cut(news_df['sentiment'], bins=[-1, -0.5, -0.0001,0.0001, 0.5, 1], labels=['Very Negative', 'Slightly Negative', 'Neutral', 'Slightly Positive','Very Postive'])
news_df['sentiment_category'].value_counts()
```
## Correlation Analysis 
The code snippet for the correlation analysis is as follows.
```python
merged_data=sentiment.merge(data,left_on='date',right_on='Date')
merged_data['date']=pd.to_datetime(merged_data['date'])
merged_data=merged_data.drop(['Unnamed: 0','Date'],axis=1)
merged_data['pct_close']=merged_data['Close'].pct_change()
merged_data['pct_sentiment']=merged_data['sentiment'].pct_change()
merged_data.dropna(inplace=True)
corr=merged_data[['Close','pct_close','sentiment','pct_sentiment','SMA','RSI','EMA','MACD']].corr()
sns.heatmap(corr,annot=True)
```
