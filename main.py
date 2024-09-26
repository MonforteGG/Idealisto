from dotenv import load_dotenv
# Cargar variables de entorno
load_dotenv()
from threading import Event, Thread
from database.model import Base
from database.conection import engine
from bot import bot
from task import task



# Crear todas las tablas si no están creadas
Base.metadata.create_all(engine)

# Evento para detener el bot
stop_event = Event()

def run_bot():
    try:
        # Iniciar el bot
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Error en el bot: {e}")
    finally:
        if stop_event.is_set():
            print("Bot detenido.")

def run_task():
    try:
        # Ejecutar las tareas programadas
        task()  # Suponiendo que esta función ejecuta alguna tarea larga
    finally:
        # Cuando task termine, detener el bot
        stop_event.set()
        print("Tareas completadas, deteniendo bot...")

if __name__ == "__main__":
    # Iniciar el bot en un hilo separado
    bot_thread = Thread(target=run_bot)
    bot_thread.start()

    # Iniciar task en otro hilo
    task_thread = Thread(target=run_task)
    task_thread.start()

    # Esperar a que task termine
    task_thread.join()

    # Detener el bot cuando task haya finalizado
    stop_event.set()

    # Esperar a que el hilo del bot finalice
    bot_thread.join()

    print("Script finalizado.")