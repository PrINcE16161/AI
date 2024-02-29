import requests
from ss import *

api_address= "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=" + key2
json_data=requests.get(api_address).json()

def temp():
    temprature= round(json_data["main"]["temp"]-298,1)
    return temprature

def des():
    description= json_data["weather"][0]["description"]
    return description