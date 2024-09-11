from search import search_api
from parameters import url

from database.querys import is_new_property
from database.model import Base
from database.conection import engine


# Crear todas las tablas si no están creadas
Base.metadata.create_all(engine)

# Hacer una llamada a la API de Idealista y almacenar el JSON obtenido
text = search_api(url)

# Almacena los nuevos anuncios en la BDD
is_new_property(text)


