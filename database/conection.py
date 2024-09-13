import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Cadena de conexión a MySQL en Azure

server = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')


DATABASE_URL = f"mysql+mysqlconnector://{username}:{password}@{server}/{database}"

# Crear el engine de conexión
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()




