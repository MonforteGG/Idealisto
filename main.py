from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

import schedule
import time


from database.model import Base
from database.conection import engine
from bot import bot
from task import task



# Crear todas las tablas si no están creadas
Base.metadata.create_all(engine)

# Programar las tareas
schedule.every().day.at("09:00").do(task)
schedule.every().day.at("15:00").do(task)
schedule.every().day.at("20:00").do(task)


# Ejecutar el bot y las tareas programadas
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(10)  # Esperar 10 segundos antes de volver a comprobar


if __name__ == "__main__":
    from threading import Thread

    # Ejecutar el bot en un hilo separado
    bot_thread = Thread(target=bot.infinity_polling)
    bot_thread.start()

    # Ejecutar el programador de tareas en el hilo principal
    run_schedule()
