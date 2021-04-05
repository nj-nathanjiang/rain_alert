import requests
from twilio.rest import Client

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 0 # Latitude
MY_LON = 0 # Longitude
api_key = "my_open_weather_data_api_key"
account_sid = "my_account_sid_for_twilio"
auth_token = "my_authoration_token_for_twilio"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(API_ENDPOINT, params=parameters)
response.raise_for_status()

response = response.json()

list_of_weathers = []
bring_umbrella = False

for i in range(0, 11):
    if response["hourly"][i]["weather"][0]["id"] < 700:
        bring_umbrella = True

if bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an umbrella.",
                from_='+18305005082', # My twilio phone number
                to="") # My Phone Number

    print(message.status)
