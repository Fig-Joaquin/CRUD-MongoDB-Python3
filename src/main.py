# -*- coding: utf-8 -*-
import pymongo
import re
import logging

# Configurar el registro de eventos
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Conexión a mongo db
client = pymongo.MongoClient("mongodb+srv://mrxalo2000:aRR5KXDyI19fS4or@cluster0.9ty8e2e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test

# la colección tiene como nombre perros.
collection = db.perros

# Crear un animal en la base de datos.
def create_dog():
    try:
        # Nombre de la mascota
        dog_name = input("Ingrese el nombre del animal: ")
        # Validación
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚ ]+$", dog_name):
            raise ValueError("\nNo se permiten el uso de números en el nombre del animal, solo letras. \n Inténtelo de nuevo.")
        
        # Edad de la mascota
        age = int(input("Ingrese la edad del animal: "))
        # Validación edad
        if age <= 0 or age > 25:
            raise ValueError("La edad introducida está fuera de rango de la edad de un perro")

        # Raza de la mascota
        dog_breed = input("Ingrese la raza del animal : " )
        # Validación de los datos
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚ ]+$", dog_breed):
            raise ValueError("No se permiten el uso de numeros en el nombre de la raza del animal, solo letras.")
        
        # Creación del animal en la base de datos
        dog = {"name": dog_name, "age": age, "breed": dog_breed}
        collection.insert_one(dog)
        print("Los datos han sido guardados con éxito")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Ocurrió un error:", e)

def read_all():
    print("Listado de animales:")
    for dog in collection.find():
        print(dog)

def read_name():
    dog_name = input("Ingrese el nombre del animal: ")
    dog = collection.find_one({"name": dog_name})
    if dog:
        print(dog)
    else:
        print("No se encontró ningún animal con ese nombre.")
        
def read_breed():
    dog_breed = input("Ingrese la raza del animal: ")
    dog = collection.find_one({"breed": dog_breed})
    if dog:
        print(dog)
    else:
        print("No se encontró ningún animal con esa raza.")


def menu():
    while True:
        print("\nSistema CRUD hecho en python con la base de datos mongo.")
        print("1. Agregar una mascota en la Base de Datos")
        print("2. Buscar mascotas en la Base de Datos")
        print("3. Busqueda por nombre")
        print("4. Busqueda por raza")
        print("5. Cambiar el nombre de un perro")
        print("6. Salir del programa")
        option = input("Seleccione una opción: ")

        if option == "1":
            create_dog()
        elif option == "2":
            read_all()
        elif option == "3":
            read_name()
        elif option == "4":
            read_breed()
        elif option == "5":
            update_dog_name()
        elif option == "6":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()