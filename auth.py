import os
from dotenv import load_dotenv

import requests
import base64


# Loading .env file
load_dotenv()


# First we need the client secret and api key

apikey =  os.getenv('IDEALISTA_API_KEY')
client_secret =  os.getenv('IDEALISTA_CLIENT_SECRET')

# above you replace for the Api Key and client code you received

# Concatenating the credentials into one variable(string)

credentials = f"{apikey}:{client_secret}"

# After we need to encode the api key and client secret
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# url which we will request the token

token_url = "https://api.idealista.com/oauth/token"

# determine the data

data = {"grant_type": "client_credentials",
        "scope": "read"}

# headers

headers = {"Authorization": f"Basic {encoded_credentials}", "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

# getting response

response = requests.post(token_url, data=data, headers=headers)

# checking status

if response.status_code == 200:
    # Parse the JSON response
    token_data = response.json()

    access_token = token_data["access_token"]

    # Print access token and other details
    print("Access Token:", token_data["access_token"])
    print("Token Type:", token_data["token_type"])
    print("Expires In (seconds):", token_data["expires_in"])
    print("Scope:", token_data["scope"])
else:
    print("Error:", response.status_code, response.text)