import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

API_KEY = os.getenv("API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

weather_params = {
    "lat":12.971599,
    "lon":77.594566,
    "appid":API_KEY,
    "cnt": 4,
    "units": "metric",
}


response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = (response.json())
#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    #print("Ohh Dear Bring an Umbrella.")
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain Today. Remember to bring an ☂️",
        from_="+19129785502",
        to="+917019095847",
    )
    print(message.status)


