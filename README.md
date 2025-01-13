# bot_pruebatecnica

DeltoBot 

En este proyecto he realizado un bot a través de BotFather desde Telegram, en conjunto con lenguaje Python. Tiene varios botones con distintas funcionalidades, dentro de ellos podemos encontrar el clima para una ciudad en específico, analizar el sentimiento de un comentario, un contador que es creciente cada vez que lo seleccionamos, y por último, conocer nuestro horóscopo diario. 

Funcionalidad libre:

Decidí implementar el botón para horóscopo diario porque me pareció interesante, ya que es un elemento que puede mejorar la experiencia del usuario siendo una búsqueda popular, divertida y personalizada. Puede contribuir para brindar inspiración sobre su día al usuario, como también generar interacciones diarias en el uso del bot.

A su vez, utilizando React tendremos una aplicación web que nos mostrará una breve descripción del clima, de una ciudad en específico. 

Instalación del BOT:

1. Clonar repositorio:
- git clone https://github.com/romitamosiunas/bot_pruebatecnica.git
- cd bot

2. Instalar dependencias:
- pip install -r requirements.txt

3. Crear archivo .env y colocar dentro:
- OPENWEATHER_API_KEY= tu clave API de OpenWeather
- OPENAI_API_KEY= tu clave API de OpenAI

4. Ejecutar BOT: 
- python main.py

5. Ingresar al BOT: 
- http://t.me/rominatamosiunas_bot
- insertar '/start'


Instalación React:

1. Seleccionar carpeta:
- cd bot-dashboard

2. Instalar dependencias:
- npm install

3. Crear archivo .env y colocar dentro:
- REACT_APP_OPENWEATHER_API_KEY= tu clave API de OpenWeather

4. Ejecutar aplicación:
- npm start



