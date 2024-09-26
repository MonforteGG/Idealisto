import requests
import json

from auth import access_token


def search_api(url):
    token = access_token  # Obtener el token personalizado

    headers = {'Content-Type': "application/json",  # Definir los encabezados de búsqueda
               'Authorization': 'Bearer ' + token}

    content = requests.post(url, headers=headers)  # Retornar el contenido de la solicitud

    result = json.loads(content.text)  # Transformar el resultado en un archivo JSON

    return result
