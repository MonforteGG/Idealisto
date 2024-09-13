from sqlalchemy import func
from database.conection import session
from database.model import Property



def get_all_property_codes():
    # Realizar la consulta para obtener todos los property_code
    property_codes = session.query(Property.advertising_id).all()

    # Convertir los resultados a un conjunto de valores únicos
    property_codes_set = set(code[0] for code in property_codes)

    return property_codes_set


def calculate_average_price_per_squared_meter():
    average_price_by_area = session.query(func.avg(Property.price_by_area)).filter(
        Property.price_by_area is not None).scalar()

    return average_price_by_area


def add_properties_to_db(property_data):
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
        print(f"Error al agregar la propiedad: {e}")
