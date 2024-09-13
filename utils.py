import os
from database.querys import calculate_average_price_per_squared_meter, get_all_property_codes, add_properties_to_db
from bot import send_message_to_group


def compare_price_per_squared_meter(property_data):
    # Obtener el precio por metro cuadrado de la propiedad
    price_per_squared_meter = float(property_data.get('priceByArea'))

    # Calcular la media del precio por metro cuadrado de la zona
    average_price_per_squared_meter = float(calculate_average_price_per_squared_meter())

    # Calcular la diferencia en porcentaje
    difference_percentage = round(
        (price_per_squared_meter - average_price_per_squared_meter) / average_price_per_squared_meter * 100, 2)

    if difference_percentage >= 0:
        return (
            f"📈 El precio por m² es de <i>{price_per_squared_meter}</i>€, un <i>{difference_percentage}</i>% <b>SUPERIOR</b> a la media de la zona (<i>{average_price_per_squared_meter}</i>€)")
    else:
        return (
            f"📉 El precio por m² es de <i>{price_per_squared_meter}</i>€, un <i>{abs(difference_percentage)}</i>% <b>INFERIOR</b> a la media de la zona (<i>{average_price_per_squared_meter}</i>€)")


def advertising_message (property_data):
    # Obtener la comparación del precio por metro cuadrado
    comparison = compare_price_per_squared_meter(property_data)

    # Construir el mensaje de telegram
    message = (
        f"📋 <b>Título</b>: <i>{property_data.get('suggestedTexts', {}).get('title', 'No disponible')}</i>\n"
        f"📐 <b>Tamaño</b>: <i>{property_data.get('size', 'No disponible')}</i> m²\n"
        f"🚪 <b>Habitaciones</b>: <i>{property_data.get('rooms', 'No disponible')}</i>\n"
        f"🚿 <b>Baños</b>: <i>{property_data.get('bathrooms', 'No disponible')}</i>\n"
        f"💶 <b>Precio</b>: <i>{property_data.get('price', 'No disponible')}</i> €\n"
        f"📊 <b>Precio por m²</b>: <i>{property_data.get('priceByArea', 'No disponible')}</i> €/m²\n"
        f"{comparison}\n\n"
        f"🔗 <a href=\"{property_data.get('url', '#')}\"><b>Ver propiedad</b></a>"
    )

    return message


def is_new_property(properties_json):
    # Obtener todos los property_codes existentes en la base de datos
    existing_property_codes = get_all_property_codes()
    print("Eston son los codigos que ya tenemos en la base de datos:")
    print(existing_property_codes)

    for property_data in properties_json['elementList']:
        property_code = int(property_data.get('propertyCode'))

        # Solo agrega la propiedad si no está ya en la base de datos
        if property_code not in existing_property_codes:
            try:
                add_properties_to_db(property_data)
                print(f"Propiedad con código {property_code} agregada correctamente.")
            except Exception as e:
                print(f"Error al agregar la propiedad con código {property_code}: {e}")

            try:
                message = advertising_message(property_data)
                send_message_to_group(os.getenv('TELEGRAM_GROUP_ID'), message)
                print(f"Propiedad con código {property_code} fue enviada por Telegram correctamente.")

            except Exception as e:
                print(f"Error al enviar a Telegram la propiedad con código {property_code}: {e}")
        else:
            print(f"La propiedad con código {property_code} ya existe en la base de datos")

