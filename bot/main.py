import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, CallbackContext, ConversationHandler, filters
from dotenv import load_dotenv
from services.weather_service import get_weather
from services.zodiac_service import get_daily_horoscope
from services.openai_service import analyze_sentiment
from services.counter_service import get_counter, update_counter

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

#Estados de la conversación
CLIMA, HOROSCOPO = range(2)

#Función para el contador
async def count(update: Update, context: CallbackContext) -> None:
    print("Comando /contar recibido")  
    user_id = update.callback_query.from_user.id
    current_count = get_counter(user_id)
    update_counter(user_id, current_count + 1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Contador: {current_count + 1}")

#Función para analizar comentarios
async def analyze_comment(update: Update, context: CallbackContext) -> None:
    user_comment = update.message.text
    print(f"Comentario recibido: {user_comment}")  
    sentiment = await analyze_sentiment(user_comment)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Sentimiento: {sentiment}")

#Función para obtener el horóscopo diario
async def daily_horoscope(update: Update, context: CallbackContext) -> None:
    sign = update.message.text.lower()
    print(f"Signo recibido: {sign}")  
    horoscope = get_daily_horoscope(sign)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=horoscope)
    return ConversationHandler.END

#Función para obtener el clima
async def weather(update: Update, context: CallbackContext) -> None:
    city = update.message.text
    print(f"Ciudad recibida: {city}")  
    weather_info = get_weather(city)
    sentiment = await analyze_sentiment(f"El clima en {city} es {weather_info['description']}")
    response = f"Clima en {city}: {weather_info['temperature']}°C, {weather_info['description']}.\n"
    response += f"Sentimiento: {sentiment}\n"
    if "lluvia" in weather_info['description'].lower():
        response += "Lleva un paraguas. ☔"
    elif "nieve" in weather_info['description'].lower():
        response += "Vístete abrigado. ❄️"
    else:
        response += "¡Que tengas un buen día! 😎"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    return ConversationHandler.END

#Función para comenzar el chat
async def start(update: Update, context: CallbackContext) -> None:
    print("Comando /start recibido")  

    buttons = [
        [InlineKeyboardButton("¡Quiero saber el clima! 🌞", callback_data='clima')],
        [InlineKeyboardButton("¡Quiero contar! 🧮", callback_data='contar')],
        [InlineKeyboardButton("Analizar Comentario 📊", callback_data='analizar_comentario')],
        [InlineKeyboardButton("¡Quiero mi horóscopo diario! 🌟", callback_data='daily_horoscope')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! ¿Qué necesitas? 😊", reply_markup=reply_markup)

#Función para manejar la respuesta de los botones
async def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer(show_alert=False, cache_time=1) 

    if query.data == 'clima':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Dime el nombre de la ciudad para la que quieres conocer el clima:")
        return CLIMA
    elif query.data == 'contar':
        await count(update, context)
    elif query.data == 'analizar_comentario':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Escribe tu comentario para analizar:")
    elif query.data == 'daily_horoscope':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Por favor, dime tu signo zodiacal (por ejemplo, aries, tauro, géminis):")
        return HOROSCOPO

#Función principal
def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(button_handler)],
        states={
            CLIMA: [CallbackQueryHandler(weather)],
            HOROSCOPO: [CallbackQueryHandler(daily_horoscope)],
        },
        fallbacks=[],
        per_message=True
    )
    application.add_handler(conv_handler)

    #Analizar comentario
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze_comment))

    # Iniciar el bot con polling
    application.run_polling()

if __name__ == '__main__':
    main()

