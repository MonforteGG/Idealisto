from database.queries import update_price, get_all_property_codes_and_prices, add_properties_to_db
from search import search_api
from parameters import url
from utils import is_new_property, send_price_changed_message, price_changed, send_message_new_property


def task():
    try:
        # Hacer una llamada a la API de Idealista y almacenar el JSON obtenido
        api_response = search_api(url)

        # Obtener todos los códigos y precios de propiedades de la base de datos
        code_price_dict = get_all_property_codes_and_prices()

        # Iterar sobre cada propiedad en la respuesta de la API
        for property_data in api_response['elementList']:
            property_code = int(property_data.get('propertyCode'))  # Obtener el código de la propiedad
            new_price = property_data.get('price')  # Obtener el nuevo precio de la propiedad

            # Verificar si es una propiedad nueva
            if is_new_property(property_data):
                # Enviar mensaje de nueva propiedad y agregar a la base de datos
                send_message_new_property(property_data, property_code)
                add_properties_to_db(property_data)
            else:
                # Si ya existe en la base de datos, verificar si ha cambiado el precio de la propiedad
                if price_changed(property_data, code_price_dict):
                    # Enviar mensaje de cambio de precio y actualizar el precio en la base de datos
                    send_price_changed_message(property_data, code_price_dict)
                    update_price(property_code, new_price)

    except Exception as e:
        # Capturar cualquier error y mostrar un mensaje de error
        print(f"Error en la tarea programada: {e}")
