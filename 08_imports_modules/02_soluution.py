import requests


def get_weather(city):
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    data = response.json()
    return data["current_condition"][0]


city = "New York"
temperature = get_weather(city)
temperature
city = "Ahmedabad"
temperature = get_weather(city)
temperature
