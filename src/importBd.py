from pymongo import MongoClient
import json
from bson import ObjectId

# Conectarse a la base de datos
client = MongoClient("mongodb+srv://mrxalo2000:aRR5KXDyI19fS4or@cluster0.9ty8e2e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test # Cambia "nombre_de_tu_base_de_datos" por el nombre de tu base de datos
collection = db.perros # Cambia "nombre_de_tu_coleccion" por el nombre de tu colección

userCollection = input("Por favor, ingresa el nombre de la colección: ")

collectionChosen = db[userCollection]

# Crear una nueva colección llamada "gatos"
collection_gatos = db.gatos

# Solicitar al usuario que ingrese el nombre del archivo JSON
nombre_archivo = input("Por favor, ingresa el nombre del archivo JSON: ")

# Abrir el archivo JSON proporcionado por el usuario
with open(nombre_archivo, 'r') as archivo:
    datos_perros = json.load(archivo)

    # Eliminar el campo "_id" de los documentos
for documento in datos_perros:
    del documento['_id']

# Insertar los documentos en la nueva colección
resultado = collectionChosen.insert_many(datos_perros)

# Imprimir el número de documentos insertados
print("Se insertaron", len(resultado.inserted_ids), "documentos en la colección 'gatos'.")

