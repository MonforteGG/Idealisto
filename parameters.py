# Detallando los parámetros

base_url = 'https://api.idealista.com/3.5/'  # URL base de búsqueda
country = 'es'  # País de búsqueda (es, it, pt)
language = 'es'  # Idioma de búsqueda (es, it, pt, en, ca)
max_items = '50'  # Máximo de elementos por solicitud, el máximo establecido por Idealista es 50
operation = 'sale'  # Tipo de operación (sale, rent)
property_type = 'homes'  # Tipo de propiedad (homes, offices, premises, garages, bedrooms)
order = 'publicationDate'  # Orden de los listados, consultar documentación para ver todas las opciones disponibles
center = '37.404762,-5.973923'  # Coordenadas del centro de la búsqueda
distance = '900'  # Distancia máxima desde el centro
sort = 'desc'  # Cómo ordenar los elementos encontrados
maxprice = '190000'  # Precio máximo de los listados

# Creando la URL con los parámetros que deseo

def define_search_url():
    url = (base_url +
           country +
           '/search?operation=' + operation +
           '&maxItems=' + max_items +
           '&order=' + order +
           '&center=' + center +
           '&distance=' + distance +
           '&propertyType=' + property_type +
           '&sort=' + sort +
           '&numPage=%s' +
           '&maxPrice=' + maxprice +
           '&language=' + language)
    return url


url = define_search_url()
