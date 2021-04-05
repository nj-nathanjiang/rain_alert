import requests
from twilio.rest import Client

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 34.181390
MY_LON = -118.782680
api_key = "50ed715298431c237e859993d7e7b032"
account_sid = "AC7dc2131f6366e61be76f09fb43215cb7"
auth_token = "c7ead93dcf2371c129a652f4cda3db01"

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
                from_='+18305005082',
                to="+18054051545")

    print(message.status)
