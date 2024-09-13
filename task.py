from search import search_api
from parameters import url
from utils import is_new_property


def task():
    try:
        # Hacer una llamada a la API de Idealista y almacenar el JSON obtenido
        api_response = search_api(url)
        # Almacenar los nuevos anuncios en la BDD y mandarlos al grupo de Telegram
        is_new_property(api_response)
    except Exception as e:
        print(f"Error en la tarea programada: {e}")