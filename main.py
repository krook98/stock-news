import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_STOCK = os.environ.get('API_KEY_STOCK')
API_KEY_NEWS = os.environ.get('API_KEY_NEWS')
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': API_KEY_STOCK
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

yesterday_closing_price = data_list[0]['4. close']
before_yesterday_closing_price = data_list[1]['4. close']

difference = abs(float(yesterday_closing_price) - float(before_yesterday_closing_price))
up_or_down = None
if difference > 0:
    up_or_down = '🔺'
else:
    up_or_down = '🔻'

percentage_difference = round(difference/float(yesterday_closing_price) * 100, 2)

if percentage_difference > 2:
    news_params = {
        'apikey': API_KEY_NEWS,
        'qInTitle': COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    data = news_response.json()['articles']
    three_articles = data[:3]

    account_sid = os.environ.get("account_sid")
    auth_token = os.environ.get("auth_token")

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    for article in three_articles:

        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: {up_or_down}{percentage_difference}%\nHeadline: {article['title']}Brief: {article['description']}",
            from_=os.environ.get('NOTIFICATION_NUMBER'),
            to=PHONE_NUMBER
        )
