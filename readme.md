> [!IMPORTANT]
> **🚀CRUD DESARROLLADO EN PYTHON Y MONGO**

## Sobre el proyecto 📌
Este es un proyecto construído con las tecnologías de Python.
La base de datos utilizada fue por preferencia MongoDB.

## _¿Cuál es el proposito de este proyecto?_ 
Una de los objetivos más importante de este proyecto es la interación de un usuario con una Base de Datos MongoDB.

## _Las siguientes funcionalidades desarrolladas en este proyecto son:_ 📌
1. Funciones CRUD. 
2. Función crear una nueva colección a través de la importación de una Base de Datos MongoDB.
3. Función de exportar una colección en la Base de Datos mongoDB.
4. Función selección de colección en la Base de Datos MongoDB.

## _¿Qué es un CRUD?_
Un CRUD en la base de datos se refiere a funcionalidades de:
* Create: Crear un documento en la base de datos.
* Read: Leer un documento de la base de datos.
* Update: Actualizar un documento de la base de datos.
* Delete: Eliminar un documento de la base de datos.

## Requisitos ❗

1. Tener instalado una versión de Python superior a las 3.0 para ejecutar el programa.
2. Tener instalado MongoDB Compasss o MongoShell para ejecutar la Base de Datos.
3. Tener instalado el sistema de gestión de paquetes PIP de Python.
3. Instalar la librería de pymongo para la ejecución correcta del programa.
4. Seguir los pasos de instalación señalados en este Readme.

## Instalación de los programas requeridos en Windows 💻
1. Instalar PIP en Windows
```sh
    python get-pip.py
```
2. Instalar ambiente de desarrollo virtualenv
```sh
    pip3 install virtualenv
  ```
3. Instalar librería pymongo
```sh 
    pip install pymongo
```
4. Instalar MongoDB Compass (Interfaz Gráfica)
* [Click aquí para acceder al link de descarga](https://www.mongodb.com/try/download/compass)
- _MongoDB Shell (Opcional)_
* [Haz click aquí para descargar MongoDB Shell](https://www.mongodb.com/try/download/shell)


## Instalación de los programas requeridos en linux 💻
1. Instalar Python3 a través de la terminal.
```sh
sudo apt update
sudo apt install python3
```
_Verificar si está instalado correctamente._
```sh
python3 --version
```
2. Instalar PIP en linux
```sh
    sudo apt update
    sudo apt install python3-pip
  ```
3. Instalar ambiente de desarrollo virtualenv
```sh
    pip3 install virtualenv
  ```
4. Instalar librería pymongo
```sh 
    pip install pymongo
```
5. Instalar MongoDB Compass
_Se debe de descargar en el link que se encuentra al final de esta página_
* Para instalar el paquete descargado:
```sh
sudo dpkg -i mongodb-compass-version.deb

```
## Instalación de los programas requeridos en MacOS 🖥️
1. Instalar Homebrew en caso de no tenerlo instalado
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```
2. Instalar Python3 y PIP
```sh 
brew install python

```
_Verificar la instalación:_
```sh 
python3 --version

```
4. Instalar ambiente de desarrollo virtualenv
```sh
    pip3 install virtualenv
  ```
5. Instalar librería pymongo
```sh 
    pip install pymongo
```
6. Instalar MongoDB Compass (Interfaz Gráfica)
* [Haz click aquí para descargar MongoDB Compass](https://www.mongodb.com/try/download/compass)
- _MongoDB Shell (Opcional)_
* [Haz click aquí para descargar MongoDB Shell](https://www.mongodb.com/try/download/shell)

## Pasos ejecutar el programa: 🚀
1. Descargar los archivos src existentes presentes en el Github.
2. Descomprimir el archivo, si es que no se utilizó git clone.
3. Crear una nueva carpeta y pegar la carpeta src.
5. Instalar el sistema de gestión de paqueres PIP.
6. Instalar MongoDB Compass o MongoShell.
7. Instalar un ambiente de desarrollo virtual para Python en la carpeta creada en la terminal.
```sh
   python3 -m venv proyecto
  ```
8. Abrir el ambiente de desarrollo virtual para Python en la terminal.
* Windows:
```sh 
proyecto\Scripts\activate
```
* Linux y MacOS
```sh
source proyecto/bin/activate
```
9. Instalar pymongo en la terminal.
```sh
pip install pymongo
```
10. Abrir el MongoDB Compass y conectarse al localhost:27017 o en el caso del MongoDB Shell, ejecutarlo en la terminal.
11. Una vez iniciado el ambiente de desarollo, instalado el pymongo y ejecutando la base de datos en localhost podremos iniciar el programa.
12. Para iniciar el programa en la terminal ejecutamos:
* MacOS
```sh  
python3 main.py
```
* Windows y Linux
```sh
python main.py
```


