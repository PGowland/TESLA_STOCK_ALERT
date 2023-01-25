import requests
from datetime import date, timedelta
from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'your twilio sid'
TWILIO_AUTH_TOKEN = 'your twilio auth'
STOCK = "TSLA"
STOCK_API = 'your stock api'
COMPANY_NAME = "Tesla Inc"
NEWS_API = 'your news api'
today_date = date.today()
yesterday_date = str(today_date - timedelta(days=1))

stock_request = requests.get(f'https://www.alphavantage.co/query?'
                             f'function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={STOCK_API}')
stock_request.raise_for_status()
stock_data = stock_request.json()
stock_open = float(stock_data['Time Series (Daily)'][yesterday_date]['1. open'])
stock_close = float(stock_data['Time Series (Daily)'][yesterday_date]['4. close'])
stock_percentage = ((stock_close - stock_open) / stock_open) * 100
print(stock_percentage)

if stock_percentage >= 5 or stock_percentage <= 5:
    news_request = requests.get(url=f'https://newsapi.org/v2/everything?q={COMPANY_NAME}'
                                    f'&from={yesterday_date}&sortBy=popularity&apiKey={NEWS_API}')
    news_request.raise_for_status()
    news_data = news_request.json()
    top_story_title = news_data['articles'][0]['title']
    top_story_desc = news_data['articles'][0]['description']
    top_story_url = news_data['articles'][0]['url']
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message_text =f"Tesla moved {stock_percentage}%. Here is why:\n{top_story_title}\n{top_story_desc}\n{top_story_url}"
    message = client.messages.create(body=message_text, from_='your virtual num', to="your phone",)

    print(message.sid)

