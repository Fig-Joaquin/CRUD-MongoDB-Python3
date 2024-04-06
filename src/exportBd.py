from pymongo import MongoClient
import json
from bson import ObjectId
import os

# Conectarse a la base de datos
client = MongoClient("mongodb+srv://mrxalo2000:aRR5KXDyI19fS4or@cluster0.9ty8e2e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test # Cambia "nombre_de_tu_base_de_datos" por el nombre de tu base de datos
collection = db.perros # Cambia "nombre_de_tu_coleccion" por el nombre de tu colección

# Solicitar al usuario que ingrese el nombre de la colección
userCollection = input("Por favor, ingresa el nombre de la colección: ")
# Colección elegida por el usuario
collectionChosen = db[userCollection]

# Obtener todos los documentos de la colección y convertirlos a una lista
documentos = list(collectionChosen.find())

# Solicitar al usuario que ingrese el nombre del archivo JSON
nombre_archivo = input("Por favor, ingresa el nombre del archivo JSON: \n Ejemplo: nombre.json: \n")

# Obtener la ruta de la carpeta donde quieres guardar el archivo
carpeta = 'json-files'  # Nombre de la carpeta donde quieres guardar los archivos

# Crear la carpeta si no existe
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

# Especificar la ruta completa del archivo dentro de la carpeta json-files
ruta_archivo = os.path.join(carpeta, nombre_archivo)


# Convertir los ObjectId a cadenas
for doc in documentos:
    doc['_id'] = str(doc['_id'])

# Escribir los documentos en un archivo JSON en la carpeta especificada
with open(ruta_archivo, 'w') as archivo:
    json.dump(documentos, archivo, default=str)

print('La exportación se realizó correctamente. El archivo se encuentra en:', ruta_archivo)