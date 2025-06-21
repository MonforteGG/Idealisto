import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Nueva URL para usar archivo SQLite local
DATABASE_URL = "sqlite:///idealisto.db"  # crea el archivo en la raíz del proyecto

# Crear el engine de conexión
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()





