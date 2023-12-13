from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Paises(Base):
    

    __tablename__="mapa"

    Pais = Column(Integer, primary_key= True)
    Datos = Column(Integer)
    latitud = Column(Float)
    longitud = Column(Float)
 
