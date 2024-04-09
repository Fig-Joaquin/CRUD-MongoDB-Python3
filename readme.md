> [!IMPORTANT]
> **🚀CRUD DESARROLLADO EN PYTHON Y MONGO**

## Sobre el proyecto 📌
Este es un proyecto construído con las tecnologías de Python.
La base de datos utilizada fue por preferencia MongoDB.

## _¿Cuál es el proposito de este proyecto?_ 
Una de los objetivos más importante de este proyecto es la interación de un usuario con una Base de Datos MongoDB a través de Python.

## _Las siguientes funcionalidades desarrolladas en este proyecto son:_ 📌
1. Funciones CRUD. 
2. Función para crear una nueva colección a través de la importación de una Base de Datos MongoDB.
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
2. Tener instalado uno de los 3 servicios MongoDB, tales como MongoDB Compasss, MongoShell o Mongo Community Server para ejecutar la base de datos.
3. Tener instalado el sistema de gestión de paquetes PIP de Python.
4. Ejecutar el programa en un ambiente de desarrollo.
5. Instalar la librería de pymongo para la ejecución correcta del programa.
6. Tener en ejecución MongoDB en el puerto 27017.
7. Ejecutar el programa en la terminal.
8. Seguir los pasos correspondientes de instalación y ejecución señalados en este Readme.

# Consejos ✏️
* Si sigues los pasos y surge algún problema, siempre puedes consultar por ayuda.
* Recuerda instalar los programas requeridos. Si falta alguno puede que no se ejecute el programa.
* En MacOS si surgen problemas con MongoDB, intenta descargar MongoDB Comunity Server. Si no ejecuta con mongod, incluye el path. Ejemplo: _sudo mongod --dbpath=/Users/nombre-del-usuario-de-la-maquina/data/db_

## Instrucciones del programa 📍
1. De primera vista el programa nos motrará un mensaje de bienvenida. Presionar Enter para continuar.
2. El programa nos mostrará el menu el cual tendremos a elección 3 secciones.
- Se debe escribir el nombre de la opción en la terminal para acceder a ella. 
- _Las siguientes opciones son las siguientes_
- [x] import 
* La opción _import_ es para importar un archivo.json el cual debe estar en la carpeta src/json-files para ser reconocido por el programa. Esta opción es útil para importar el respaldo de la base de datos.
1. Al utilizar está opción debemos primero introducir el nombre de la colección que queremos. (se recomienda llamarle: perros)
2. Ahora debemos insertar la colección llamada perrosbd.json
* Si desea salir de esta opción se debe escribir "salir" en la terminal. (Sin las comillas)
- [x] select
* La opción _select_ nos ayuda a escoger una colección dentro de nuestra base de datos, en el caso de que existan varias colecciones.
1. Al utilizar está opción deberemos escoger la colección según el nombre que hemos puesto. En este caso perros.
* Si desea salir de esta opción se debe escribir "salir" en la terminal. (Sin las comillas)
- [x] menu
* La opción _menu_ nos redirigirá a un menú con el CRUD realizado para la base de datos perrosbd.json que se encuentra en la carpeta json-files.
* Para acceder a las funcionalidades del menu, se debe importar el json con la base de datos a través de la opción _import_, además debemos de seleccionar la colección con la cual vamos a trabajar a través de la opción _select_.
1. Al seleccionar esta opción nos redireccionará al menú del CRUD la cual nos mostrará las siguientes opciones:
## Menu del CRUD
En el menu del CRUD tendremos opciones de:
1. Agregar un perro a la base de datos.
* Nos pedirá cada dato del esquema de la base de datos.
2. Mostrar todos los perros registrados.
* Se mostraran todos los perros registrados en la base de datos.
3. Buscar un perro por su nombre.
* Se debe ingresar el nombre de la mascota. Se mostrará el esquema completo de la mascota.
4. Buscar un perro por su dueño.
* Se debe ingresar el nombre del dueño de la mascota. Se mostrará el esquema completo de la mascota.
5. Buscar un perro por su raza.
* Se debe ingresar el nombre de la raza de la mascota. Se mostrará el esquema completo de la mascota.
6. Actualizar la información de un perro.
* Se mostrará la inforamción del esquema, se debe escribir que dato se requiere cambiar. Luego el programa nos pedirá el nuevo dato a ingresar.
7. Eliminar un perro de la base de datos.
* Se pide ingresar el nombre del dueño de la mascota, además se mostrará si el dueño tiene uno o más perros. (Evita mal manejo de la información)
8. Exportar la colección de la base de datos.
(Se exportará la colección actual en la carpeta json-files)
9. Volver al menu principal.
* Vuelve al menu principal.
10. Salir del programa.
* Termina la ejecución del programa.
* _Se debe de ingresar el numero correspondiente a la opción a utilizar_

## Esquema utilizado en la base de datos MongoDB.
* El nombre de la mascota como tipo String: __"name"__
* La edad como tipo int: __"age"__
* La raza de la mascota como tipo String: __"breed"__
* El nombre del dueño de la mascota como tipo String: __"dog_owner"__
## Instalación de los programas requeridos en Windows 💻
1. Instalar Python3
* [Click descarga de Python](https://www.python.org/)
1. Instalar PIP en Windows
```sh
    python get-pip.py
```
1. Instalar ambiente de desarrollo virtualenv
```sh
    pip3 install virtualenv
  ```
1. Instalar MongoDB Compass (Interfaz Gráfica)
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
4. Instalar MongoDB Compass
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
3. Instalar ambiente de desarrollo virtualenv
```sh
    pip3 install virtualenv
  ```
4. Instalar MongoDB Compass (Interfaz Gráfica)
* [Haz click aquí para descargar MongoDB Compass](https://www.mongodb.com/try/download/compass)
- _MongoDB Shell (Opcional)_
* [Haz click aquí para descargar MongoDB Shell](https://www.mongodb.com/try/download/shell)
- _Mongo Comunity Server_
* [Haz click aquí para descargar MongoDB Comunity Server](https://www.mongodb.com/try/download/community)

## Pasos para la correr el programa y ejecución de la base de datos: 🚀
1. Descargar los archivos existentes presentes en el Github.
2. Descomprimir el archivo, si es que no se utilizó git clone.
3. Crear una nueva carpeta y pegar la carpeta src.
5. Instalar el sistema de gestión de paqueres PIP si es que no está instalado.
6. Instalar MongoDB Compass o MongoShell si no está instalado (recordatorio).
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
10. Para la ejecución de la base de datos haremos lo siguiente:
_En el caso de MongoDB Compass_
* Ejecutaremos el programa y nos conectaremos al mongodb://localhost:27017/
* En el caso de MongoDB Shell ejecutaremos mongosh en la terminal. (Se ejecutará en el localhost:27017 por defecto)
* En el caso de MongoDB Community Server iniciaremos el programa en la terminal. (Se ejecutará en el localhost:27017 por defecto)
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


