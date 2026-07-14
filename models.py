from sqlalchemy import Column, Integer, String
from database import Base

class Atraccion(Base):
    __tablename__ = "atracciones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    parque = Column(String)
    tiempo_espera = Column(String)