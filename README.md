# reto_python_SQL
Reto de Desarrollo Backend - Python - SQL

Este es el reto de python donde se deben crear varios endpoints

Se encuentra dividido en dos servicios uno que es para la parte de chistes y el otro para la parte matematica. 

Para poder ejecutar el proyecto debe ir al archivo de development.py que se encuentra en la carpeta config, y en el mismo realiar la configuracion de la base de datos.
Debera completar las siguientes claves:

 * USER_DB = 'USER_DB'
 * PASS_DB = 'PASS_DB'
 * HOST_DB = 'HOST_DB'
 * PORT_DB = PORT_DB (por defecto viene seteado como 3306)
 * NAME_DB = 'NAME_DB'

Una vez realizado el seteo de la base de datos, debe ingresar en la carpeta del proyecto y crear un entorno virtual mediante el comando:

 ```terminal
python3 -m venv venv
```
Cuando ya tenga el entorno virtual creado activelo mediante el siguiente comando:

 ```terminal
 source nom_virtual_env/bin/activate
```
Con el ambiente virtual activo puede ejecutar el archivo de requirements.txt para instalar las librerias utilizadas por el proyecto.

 ```terminal
 pip install -r /path/to/requirements.txt
```

Finalmente puede ejecutar el programa mediante el comando 

 ```terminal
 python3 main.py
```

Cuando se encuentre corriendo el programa se realizara la creacion de las tablas en la base de datos
y luego de eso podra ejecutar los endpoints para trabajar con el proyecto.
Para conocer los endopints consulte la documentacion de swagger ientras corre el proyecto, en el browser dirijase a la direccion http://127.0.0.1:5000 si no ha hecho modificaciones en esa IP y PORT deberia estar corriendo el proyecto.