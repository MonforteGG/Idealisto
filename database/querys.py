from sqlalchemy import func
from database.conection import session
from database.model import Property


def get_all_property_codes_and_prices():
    with session:
        # Realizar la consulta para obtener todos los property_code con sus respectivos precios
        existing_properties = session.query(Property.advertising_id, Property.price).all()

        # Convertir el resultado a un diccionario
        property_dict = {code: price for code, price in existing_properties}

        return property_dict


def calculate_average_price_per_squared_meter():
    with session:
        # Calcular el precio promedio por área
        average_price_by_area = session.query(func.avg(Property.price_by_area)).filter(
            Property.price_by_area is not None).scalar()

        return average_price_by_area


def update_price(property_code, new_price):
    with session:
        try:
            # Actualizar el precio de la propiedad con el código dado
            session.query(Property).filter(Property.advertising_id == property_code).update({"price": new_price})

            # Confirmar los cambios en la base de datos
            session.commit()
            print(f"Precio actualizado para la propiedad con código {property_code}. Nuevo precio: {new_price}€")
        except Exception as e:
            # Si algo sale mal, hacer rollback
            session.rollback()
            print(f"Error al actualizar el precio de la propiedad con código {property_code}: {e}")


def add_properties_to_db(property_data):
    with session:
        try:
            property_obj = Property(
                advertising_id=property_data.get('propertyCode'),
                title=property_data.get('suggestedTexts', {}).get('title'),
                description=property_data.get('description'),
                url=property_data.get('url'),
                size=property_data.get('size'),
                price=property_data.get('price'),
                price_by_area=property_data.get('priceByArea'),
                property_type=property_data.get('propertyType'),
                status=property_data.get('status'),
                floor=property_data.get('floor'),
                rooms=property_data.get('rooms'),
                bathrooms=property_data.get('bathrooms'),
                province=property_data.get('province'),
                municipality=property_data.get('municipality'),
                address=property_data.get('address'),
                latitude=property_data.get('latitude'),
                longitude=property_data.get('longitude'),
            )
            session.add(property_obj)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error al agregar a la base de datos: {e}")