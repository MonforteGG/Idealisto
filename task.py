from database.queries import update_price, get_all_property_codes_and_prices, add_properties_to_db
from search import search_api
from parameters import url
from utils import is_new_property, send_price_changed_message, price_changed, send_message_new_property


def task():
    try:
        # Hacer una llamada a la API de Idealista y almacenar el JSON obtenido
        api_response = search_api(url)

        code_price_dict = get_all_property_codes_and_prices()
        for property_data in api_response['elementList']:
            property_code = int(property_data.get('propertyCode'))
            new_price = property_data.get('price')

            if is_new_property(property_data):
                send_message_new_property(property_data, property_code)
                add_properties_to_db(property_data)
            else:
                if price_changed(property_data, code_price_dict):
                    send_price_changed_message(property_data, code_price_dict)
                    update_price(property_code, new_price)

    except Exception as e:
        print(f"Error en la tarea programada: {e}")