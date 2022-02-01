# General info
Get SMS notification when your favourite stock company's price changes.

### API Used
I send SMS notifications with Twilio API (https://www.twilio.com/)
Stock news are taken with News API (https://newsapi.org/v2/everything)
Stock prices are tracked with Alpha Vantage API, TIME_SERIES_DAILY (https://www.alphavantage.co/documentation/)


### Technology
Python 3.9.10  
I run the code as a scheduled task on PythonAnywhere (https://www.pythonanywhere.com)

### Setup
To run this project you might need your own API keys. Twilio and OpenWeather accounts are neccessary.    
requests, twilio and os Python libraries are required

### Launch
Firstly, you need to add your own API keys, phone number and notification number from Twilio. You set environment variables in terminal with:  <br/><br/>
`export 'YOUR_ENV_VAR_NAME'=value`  <br/><br/>
Then you can access it in code with:  <br/><br/>
`os.environ.get('YOU_ENV_VAR_NAME')`  <br/><br/>
Run app with:  <br/><br/>
`python3 main.py` 
