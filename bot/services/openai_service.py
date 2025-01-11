import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

#Función analizar sentimiento
async def analyze_sentiment(text):
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente que analiza el sentimiento de los textos."},
            {"role": "user", "content": text}
        ],
        max_tokens=50
    )
    sentiment = response.choices[0].message['content'].strip()
    return sentiment

#Función de respuesta
async def generate_response(text):
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente que genera respuestas."},
            {"role": "user", "content": text}
        ],
        max_tokens=50
    )
    return response.choices[0].message['content'].strip()
















