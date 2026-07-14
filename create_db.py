from database import engine, Base
import models

# Esto crea el archivo atracciones.db automáticamente
Base.metadata.create_all(bind=engine)
print("¡Base de datos creada con éxito!")