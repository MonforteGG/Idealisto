from sqlalchemy import DECIMAL, Column, Integer, String, Numeric, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True, autoincrement=True)
    advertising_id = Column(Integer, nullable=False)
    title = Column(String(255))
    description = Column(Text, nullable=True)
    url = Column(Text)
    size = Column(Numeric(10, 2))
    price = Column(Numeric(10, 2))
    price_by_area = Column(DECIMAL(10, 2))
    property_type = Column(String(50), nullable=True)
    status = Column(String(50), nullable=True)
    floor = Column(String(10), nullable=True)
    rooms = Column(Integer, nullable=True)
    bathrooms = Column(Integer, nullable=True)
    province = Column(String(100), nullable=True)
    municipality = Column(String(100), nullable=True)
    address = Column(Text, nullable=True)
    latitude = Column(DECIMAL(10, 8), nullable=True)
    longitude = Column(DECIMAL(11, 8), nullable=True)



