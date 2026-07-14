import requests
from bs4 import BeautifulSoup
from database import SessionLocal
import models

def ejecutar_scraping():
    # URL de Magic Kingdom 
    url = "https://queue-times.com/es/parks/6/queue_times"
    
    # Es muy importante el 'headers'. Muchos sitios bloquean a los robots.
    # Esto le dice al sitio que somos un navegador real.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Buscamos todas las etiquetas <a> que tienen la clase 'panel-block'
    atracciones_items = soup.find_all('a', class_='panel-block')
    
    db = SessionLocal()
    
    for item in atracciones_items:
        nombre_tag = item.find('span', class_='has-text-weight-normal')
        tiempo_tag = item.find('span', style=lambda value: value and 'float: right' in value)
        
        if nombre_tag and tiempo_tag:
            nombre_text = nombre_tag.text.strip()
            tiempo_text = tiempo_tag.text.strip()
            
            # 1. Buscamos si la atracción ya existe por su nombre
            atrac_existente = db.query(models.Atraccion).filter(models.Atraccion.nombre == nombre_text).first()
            
            if atrac_existente:
                # Si existe, solo actualizamos el tiempo de espera
                atrac_existente.tiempo_espera = tiempo_text
                print(f"Actualizado: {nombre_text} -> {tiempo_text}")
            else:
                # Si no existe, creamos una nueva
                nueva_atrac = models.Atraccion(nombre=nombre_text, parque="Magic Kingdom", tiempo_espera=tiempo_text)
                db.add(nueva_atrac)
                print(f"Agregado: {nombre_text} -> {tiempo_text}")
    
    db.commit()
    db.close()
    print("¡Scraping completado con éxito!")
    
    db.commit()
    db.close()
    print("¡Proceso terminado!")

if __name__ == "__main__":
    ejecutar_scraping()