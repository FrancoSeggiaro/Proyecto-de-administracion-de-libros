TRABAJO PRÁCTICO FINAL 2026 - SISTEMAS OPERATIVOS: Docker & Docker Compose.  

Aplicación Web CRUD con Flask + MongoDB. 

Integrantes: 

- Franco Spizzirri. 
- Franco Seggiaro. 


Descripción del proyecto: 

La aplicación consiste en un sistema web desarrollado en Python, utilizando Flask, que permite realizar operaciones CRUD sobre una base de datos MongoDB. 

Los datos que se gestionaron corresponden a libros con los siguientes campos: 

- id (único)
- título
- cantidad de páginas
- editorial
- ISBN
- costo en USD

El sistema se compone de dos contenedores: 

1) El Servicio Web: 

	- Utilizamos Apache + Flask. 
	- Ejecutamos la aplicación web. 
	- Se conecta a MongoDB mediante red interna Docker. 

2) El Servicio Base de Datos: 
	
	- Utilizamos la imagen oficial de MongoDB. 
	- Usamos volumen para la persistencia de datos. 

Esto permite que los datos no se pierdan al detener o reiniciar los contenedores.
Ambos servicios se comunican mediante una red definida en Docker-compose. 


Previamente tuvimos que: 


- Instalar Docker. 
- Tener Docker Compose habilitado. 
- Tener Docker Desktop activo (en nuestro caso ya que utilizamos linux). 

Se pueden verificar todos estos datos con el comando docker ps. 


INSTRUCCIONES DE DESPLIEGUE. 

1) Se debe ubicar en la carpeta del proyecto donde se encuentra el archivo "docker-compose.yml". 
2) Luego, ejecutar: docker compose up --build. 
3) Esperar a que los contenedores se creen e inicien. 
4) Acceder desde el navegador a: http://localhost:8080

Funcionalidades: 

- Alta de libro (Create). 
- Visualización de libros (Read). 
- Modificación de libro (Update). 
- Eliminación de libro (Delete). 
- Validación de ID único. 
. Persistencia de datos mediante volumen Docker. 

(esto mg como lo planteo la IA, pero no c que tanto va a estar bueno dejar los comandos asi q te lo dejo comentado tamb para q despues lo veas). 

Para detener los contenedores:
 
   docker stop $(docker ps -q)
    
Para eliminar contenedores (sin borrar datos del volumen):

    docker compose down

Para eliminar todo incluyendo volúmenes:

    docker compose down -v


Se realizaron pruebas de:

- Creación de libros.
- Intento de creación con ID duplicado.
- Edición de registros.
- Eliminación de registros.
- Persistencia tras reiniciar contenedores.


ARQUITECTURA			(esto no creo que lo dejemos, pero estaria bueno si le podemos meter un cuadrito aca. Tipo con esta estructura pero mejor hecho, yo despues veo de hacerlo si te parece). 

Navegador
     ↓
Contenedor Web (Apache + Flask)
     ↓
Red Docker interna
     ↓
Contenedor MongoDB
     ↓
Volumen Docker (persistencia)
