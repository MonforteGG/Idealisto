import os
from dotenv import load_dotenv

import requests
import base64


# Cargando el archivo .env
load_dotenv()

apikey = os.getenv('IDEALISTA_API_KEY')
client_secret = os.getenv('IDEALISTA_CLIENT_SECRET')

# Concatenando las credenciales en una sola variable (string)
credentials = f"{apikey}:{client_secret}"

# Luego necesitamos codificar la API key y el client secret
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# URL a la cual haremos la solicitud para obtener el token
token_url = "https://api.idealista.com/oauth/token"

# Definir los datos
data = {"grant_type": "client_credentials",
        "scope": "read"}

# Encabezados
headers = {"Authorization": f"Basic {encoded_credentials}", "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

# Obteniendo la respuesta
response = requests.post(token_url, data=data, headers=headers)

# Verificando el estado
if response.status_code == 200:
    # Parsear la respuesta JSON
    token_data = response.json()

    access_token = token_data["access_token"]

    # Imprimir el token de acceso y otros detalles
    print("Access Token:", token_data["access_token"])
    print("Tipo de Token:", token_data["token_type"])
    print("Expira en (segundos):", token_data["expires_in"])
    print("Alcance:", token_data["scope"])
else:
    print("Error:", response.status_code, response.text)
