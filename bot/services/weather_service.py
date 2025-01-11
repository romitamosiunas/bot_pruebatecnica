import requests
import os

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

#Obtener el clima
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != 200:
        return {"description": "Ciudad no encontrada", "temperature": "N/A"}
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    return {"temperature": temperature, "description": description}










