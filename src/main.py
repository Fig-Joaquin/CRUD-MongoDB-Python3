#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libreries
import pymongo
import re
import logging
import time
import platform
import os
import sys

# Constants
# Validation names
VALID_NAME = re.compile("^[a-zA-ZáéíóúÁÉÍÓÚ ]+$")
INTRO_TIME = "Presione Enter para continuar..."

# Configurar el registro de eventos
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Conexión a mongo db
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.test
collection = None
collection_chosen = None
# la colección tiene como nombre perros.
collection = collection_chosen
# Limpiar pantalla
def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
# Elección de colección
def select_collection():
    global collection
    global collection_chosen
    
    while True:
        # Obtener y desplegar las colecciones disponibles
        collections = db.list_collection_names()
        print("\nColecciones disponibles:\n")
        if collections:
            print("Colecciones disponibles en la base de datos:")
            for col in collections:
                print(col)
        else:
            print("No hay colecciones disponibles en la base de datos.")
        # Solicitar al usuario que ingrese el nombre de la colección
        collection_user = input("\nPor favor, ingresa el nombre de la colección: \n:")
        
        # Verificar si la colección ingresada por el usuario está en la lista de colecciones disponibles
        if collection_user in collections:
            # Colección elegida por el usuario
            collection_chosen = db[collection_user]
            print ("\nSe ha seleccionado correctamente la colección de: ", collection_chosen.name)
            input(INTRO_TIME)
            collection = collection_chosen
            return collection_chosen
        else:
            clear_screen()
            print("¡La colección ingresada no es válida!. Por favor, intenta de nuevo.")
        if collection_user.lower() == "salir":
            break

# Crear un animal en la base de datos.
def create_dog():
    try:
        # Nombre de la mascota
        dog_name = input("Ingrese el nombre de la mascota: ").lower()
        # Validación
        if not re.match(VALID_NAME, dog_name):
            raise ValueError("\nNo se permiten el uso de números en el nombre del perro, solo letras. \n Inténtelo de nuevo.")
        
        # Nombre del dueño de la mascota
        dog_owner = input("Ingrese el nombre del dueño: ").lower()
        # Validación
        if not re.match(VALID_NAME, dog_owner):
            raise ValueError("\nNo se permiten el uso de números en el nombre del dueño de la mascota, solo letras. \n Inténtelo de nuevo.")
        
        # Edad de la mascota
        age = int(input("Ingrese la edad del animal: "))
        # Validación edad
        if age <= 0 or age > 25:
            raise ValueError("La edad introducida está fuera de rango de la edad de un perro")

        # Raza de la mascota
        dog_breed = input("Ingrese la raza del perro : " ).lower()
        # Validación de los datos
        if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚ ]+$", dog_breed):
            raise ValueError("No se permiten el uso de numeros en el nombre de la raza del animal, solo letras.")
        
        # Creación del animal en la base de datos
        dog = {"name": dog_name, "age": age, "breed": dog_breed, "dog_owner": dog_owner}
        collection.insert_one(dog)
        print("Los datos han sido guardados con éxito")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Ocurrió un error:", e)
# Mostrar todas las mascotas
def read_all():
    clear_screen()
    animals = list(collection.find())
    if not animals:
        print("No hay animales en la base de datos.")
    else:
        print("Listado de animales:")
        for dog in animals:
            print(dog)
# Buscar mascota por su nombre
def read_name():
    clear_screen()
    print("Busqueda por su nombre")
    dog_name = input("Ingrese el nombre del animal: ")
    dog = collection.find_one({"name": dog_name})
    if dog:
        print(dog)
    else:
        print("No se encontró ningún animal con ese nombre.")
# Buscar mascota por su dueño
def read_dog_owner():
    clear_screen()
    print("Busqueda por su dueño")
    dog_owner = input("Ingrese el nombre del dueño: ").lower()
    print(dog_owner)
    dog = collection.find_one({"dog_owner": dog_owner})
    if dog:
        print(dog)
    else:
        print("No se encontró ningún dueño con ese nombre.")
# Buscar mascota por su raza
def read_breed():
    clear_screen()
    print("Busqueda por su raza")
    dog_breed = input("Ingrese la raza del animal: ").lower()
    dog = collection.find_one({"breed": dog_breed})
    if dog:
        print(dog)
    else:
        print("No se encontró ningún animal con esa raza.")
# Actualización de datos de una mascota
def update_dog_data():
    clear_screen()
    print("Actualizar datos de una mascota")
    dog_name = input("Ingrese el nombre del perro que desea modificar: ").lower()
    dog_owner = input("Ingrese el nombre del dueño de la mascota: ").lower()
    dog = collection.find_one({"name": dog_name, "dog_owner": dog_owner})
    if dog:
        print("Se ha encontrado el siguiente perro:")
        print(dog)
        field_to_update = input("Ingrese el nombre del campo que desea modificar (name, age, breed, dog_owner): ").lower()
        if field_to_update in ["name", "age", "breed", "dog_owner"]:
            new_value = input(f"Ingrese el nuevo valor para '{field_to_update}': ").lower()
            update_result = collection.update_one({"name": dog_name}, {"$set": {field_to_update: new_value}})
            if update_result.modified_count > 0:
                print("El campo se ha actualizado exitosamente.")
            else:
                print("No se realizó ninguna actualización.")
        else:
            print("Campo inválido. Por favor, ingrese un campo válido.")
    else:
        print("No se encontró ningún perro con ese nombre.")
# Eliminar una mascota
def delete_dog():
    clear_screen()
    print("Eliminar una mascota")
    dog_owner = input("Ingrese el nombre del dueño del perro que desea eliminar: ").lower()
    dogs_found = list(collection.find({"dog_owner": dog_owner}))  # Convertir el cursor a una lista
    # Verificar si se encontraron perros con el dueño proporcionado
    if len(dogs_found) > 0:
        print("Perros del dueño:")
        for dog in dogs_found:
            print("- Nombre de la mascota:", dog.get("name"))
    else:
        print("No se encontró ningún perro con el dueño proporcionado:", dog_owner)
    dog_name = input("Ingrese el nombre de la mascota a eliminar: ").lower()
    dog = collection.find_one({"name": dog_name, "dog_owner": dog_owner})
    if dog:
        print("Se ha encontrado el siguiente perro:")
        print(dog)
        confirmacion = input("¿Está seguro de que desea eliminar este perro? (s/n): ")
        if confirmacion.lower() == "s":
            collection.delete_one({"name": dog_name})
            print("El perro ha sido eliminado exitosamente.")
        else:
            print("Eliminación cancelada.")
    else:
        print("No se encontró ningún perro con ese nombre.")
# Función para ejecutar el archivo importBd.py
def import_database():
    
    try:
        print("Importación de una colección en la base de datos.\n")
        print("Para salir del programa, escribir: salir")
        exec(open("importBd.py").read())
        clear_screen()
    except FileNotFoundError:
        print("El archivo importBd.py no se encontró en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error al ejecutar el archivo importBd.py:", e)
    # Importe de la colección de usuario
    
# Función para ejecutar el archivo exportBd.py
def export_database():

    try:
        exec(open("exportBd.py").read())
    except FileNotFoundError:
        print("El archivo importBd.py no se encontró en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error al ejecutar el archivo importBd.py:", e)
# Opciones del main menu
def option_menu(option): 
    if option == "1":
        create_dog()
    elif option == "2":
        read_all()
        input(INTRO_TIME)
        clear_screen()
    elif option == "3":
        read_dog_owner()
        input(INTRO_TIME)
        clear_screen()
    elif option == "4":
        read_name()
        input(INTRO_TIME)
        clear_screen()
    elif option == "5":
        read_breed()
        input(INTRO_TIME)
        clear_screen()
    elif option == "6":
        update_dog_data()
        input(INTRO_TIME)
        clear_screen()
    elif option == "7":
        delete_dog()
        input(INTRO_TIME)
        clear_screen()
    elif option == "8":
        export_database()
        clear_screen()
    elif option == "9":
        return False
    elif option == "10":
        sys.exit(0)
    else:
        print("Opción no válida. Inténtelo de nuevo.")
# Intro menu
def intro_menu():

    print("\nSistema CRUD hecho en Python3 con la base de datos Mongo.\n")
    input(INTRO_TIME)
    clear_screen()
    print("Escriba el comando que desea ejecutar:\n")
    print(" Lista de comandos")
    print(": import (Importar una colección a la base de datos)")
    print(": select (Seleccionar una colección de la base de datos)")
    print(": menu (Para entrar al menu)\n")
# Texto del menu de opciones
def text_menu():
    
    print("                Main menu")
    print("1. Agregar una perro")
    print("2. Mostrar todos los perros registados")
    print("3. Buscar un perro por su dueño")
    print("4. Buscar un perro por su nombre")
    print("5. Buscar un perro por su raza")
    print("6. Actualizar la cartola de un perro")
    print("7. Eliminar un perro")
    print("8. Exportar la colección desde un archivo JSON")
    print("9. Volver atras")
    print("10. Salir del programa")
# Texto de seleccion de la colección
def text_collection():
    print("Por favor, seleccione una colección de la base de datos.\n Si desea volver atrás, escribir: (salir)")

def menu_collection():
    clear_screen()
    if collection is None:
        input("¡No se ha seleccionado una colección! Debes elegir una colección para utilizar esta sección.\n Presione dos veces Enter para continuar...")
        return False
    elif collection != None:
        print("Se está trabajando en la colección: ", collection.name)
# Ejecución del menu
def menu():
    while True:
        clear_screen()
        intro_menu()
        answer_user= input("Ingrese el comando:\n ").lower()
        if answer_user.lower() == "import":
            clear_screen()
            import_database()
        elif answer_user.lower() == "menu":
            while True:
                menu_collection()
                if menu_collection() == False:
                    break
                text_menu()
                option = input("Seleccione una opción: ") 
                option_menu(option)
                if option == "9":
                    break
        elif answer_user == "select":
            clear_screen()
            text_collection()
            select_collection() 
# Ejecución del programa
if __name__ == "__main__":
    menu()