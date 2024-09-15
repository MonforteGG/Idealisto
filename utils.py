import os
from database.queries import calculate_average_price_per_squared_meter, get_all_property_codes_and_prices
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


def advertising_message(property_data):
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


def price_change_message(property_data, code_price_dict):
    property_code = int(property_data.get('propertyCode'))

    new_price = float(property_data.get('price'))
    old_price = float(code_price_dict[property_code])

    price_diff = abs(new_price - old_price)
    price_diff_percentage = abs(round((new_price - old_price) / old_price * 100, 2))

    higher_message = f"🔺 ¡Atención! El precio de esta vivienda ha AUMENTADO un {price_diff_percentage}% 📈 (💶 {price_diff}€):"

    lower_message = f"🔻 ¡Oportunidad! El precio de esta vivienda ha DISMINUIDO un {price_diff_percentage}% 📉 (💶 {price_diff}€):"

    if new_price > old_price:
        return higher_message
    elif new_price < old_price:
        return lower_message


def price_changed(property_data, code_price_dict):
    property_code = int(property_data.get('propertyCode'))

    new_price = float(property_data.get('price'))
    old_price = float(code_price_dict[property_code])

    return new_price != old_price


def send_price_changed_message(property_data, code_price_dict):
    first_message = price_change_message(property_data, code_price_dict)
    second_message = advertising_message(property_data)
    send_message_to_group(os.getenv('TELEGRAM_GROUP_ID'), first_message)
    send_message_to_group(os.getenv('TELEGRAM_GROUP_ID'), second_message)


def is_new_property(property_data):
    # Obtener todos los property_codes y precios existentes en la base de datos
    code_price_dict = get_all_property_codes_and_prices()
    existing_property_codes = set(code_price_dict.keys())  # Optimizar la búsqueda con un set

    # Obtiene el property_code del anuncio
    property_code = int(property_data.get('propertyCode'))

    if property_code not in existing_property_codes:
        return True
    else:
        print(f"La propiedad con código {property_code} ya existe en la base de datos")


def send_message_new_property(property_data, property_code):

    try:
        message = advertising_message(property_data)
        send_message_to_group(os.getenv('TELEGRAM_GROUP_ID'), message)
        print(f"Propiedad con código {property_code} fue enviada por Telegram correctamente.")
    except Exception as e:
        print(f"Error al enviar a Telegram la propiedad con código {property_code}: {e}")


