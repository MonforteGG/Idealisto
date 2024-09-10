import requests
import json

from auth import access_token


def search_api(url):
    token = access_token  # Get the personalised token

    headers = {'Content-Type': "application/json",  # Define the search headers
               'Authorization': 'Bearer ' + token}

    content = requests.post(url, headers=headers)  # Return the content from the request

    result = json.loads(content.text)  # Transform the result as a json file

    return result
