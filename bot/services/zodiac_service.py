import requests

#Función para obtener el horoscopo
def get_daily_horoscope(sign: str) -> str:
    url = f"https://www.horoscopo.eu/horoscopo-diario/{sign}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "No se pudo obtener el horóscopo diario."
