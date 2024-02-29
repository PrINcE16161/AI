import requests

url="https://official-joke-api.appspot.com/jokes/random"
json_data=requests.get(url).json()

aru=["",""]
aru[0]=json_data["setup"]
aru[1]=json_data["punchline"]

def joke() -> object:
    return aru
