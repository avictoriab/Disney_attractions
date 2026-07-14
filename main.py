from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Creamos la aplicación FastAPI
app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para ver todas las atracciones
@app.get("/atracciones")
def leer_atracciones(db: Session = Depends(get_db)):
    atracciones = db.query(models.Atraccion).all()
    return {"atracciones": atracciones}