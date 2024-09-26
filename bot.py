import telebot
import os


# Inicializar el bot de Telegram
bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))

welcome_text = (
    "Hola, soy el bot de <b>Idealisto</b>. Cada vez que aparezca un nuevo anuncio de una vivienda "
    "cerca de la <b>Avenida Llanes</b> en <b>Sevilla</b> (radio inferior a 900 metros) "
    "en la plataforma inmobiliaria <b>Idealista</b> con un precio <b>inferior a 190.000€</b>, mandaré un mensaje "
    "con las principales características del inmueble."
)


@bot.message_handler(commands=['health', 'online'])
def send_welcome(message):
    bot.reply_to(message, "Estoy funcionando correctamente!", parse_mode= "HTML")


def send_message_to_group(group_id, message_text):
    try:
        bot.send_message(group_id, message_text, parse_mode="HTML")
        print(f"Mensaje enviado al grupo: {message_text}")
    except Exception as e:
        print(f"Error al enviar el mensaje al grupo: {e}")