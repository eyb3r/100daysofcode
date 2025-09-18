from os import environ as evar
import requests
from datetime import *
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api_auth = '8ccfba0c1518c4b84c1a8c094810007412257cc3'
news_api_auth = '944d0c06f5df4892a3afb26b91ae5ad7'
print(stock_api_auth)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# let's calculate the starting date for our comparison.
# I take a day before yesterday and check if it's a working day(holidays not supported)
# if yes, I subtract another day or two, depending if thats SAT or SUN.
minus2_day = datetime.today() - timedelta(days=2)
if minus2_day.weekday() >= 5:
    minus2_day -= timedelta(days=minus2_day.weekday()-4)
start_date = minus2_day.strftime('%Y-%m-%d')

url = f'https://api.tiingo.com/tiingo/daily/{STOCK}/prices?startDate={start_date}&token={stock_api_auth}'
print(url)
if not stock_api_auth:
    response = requests.get(url=url)
    stock_data = response.json()
    try:
        minus2_data, minus1_data = stock_data[0], stock_data[1]
    except IndexError:
        print('no data for second day, holiday most likely')
    print(stock_data)

    if minus2_data['close'] <= 0.95 * minus1_data['close']:
        print('get news')
    else:
        print(minus2_data['close']/minus1_data['close'])
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_request = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&sortBy=published_at&searchin=title&language=en&apiKey={news_api_auth}'
news_feed = requests.get(url=news_request)
print(news_feed.json()['articles'][:4])
# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

