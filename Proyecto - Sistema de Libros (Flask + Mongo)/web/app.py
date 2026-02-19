from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import os

app = Flask(__name__) #creamos instancia de Flask
app.secret_key = "clave_secreta_para_flash_messages" 

#Configuracion de Mongo
MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME", "admin") #Obtenemos el usuario y la contraseña de las variables de entorno, si no existen, usamos valores por defecto
MONGO_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "secreto") #El host y el puerto los definimos en el docker-compose, por eso usamos "db" y el puerto 27017
client = MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASS}@db:27017/") #nos conectamos a MongoDB usando las credenciales y la dirección del contenedor de la base de datos definida en docker-compose.
#Fin Configuracion de Mongo

db = client['libros_db'] #creamos la base de datos
libros = db['libros'] #creamos la coleccion

@app.route('/')
def index():
    # traemos los datos de MongoDB
    lista_libros = list(libros.find())
    # volvemos al menu y mostramos los libros
    return render_template('index.html', libros=lista_libros)

@app.route('/agregar', methods=['POST'])
def agregar():
    # 1. Capturar datos y limpiar espacios en blanco
    id_libro = request.form.get('id', '').strip()
    titulo = request.form.get('titulo', '').strip()
    paginas = request.form.get('paginas', '').strip()
    editorial = request.form.get('editorial', '').strip()
    isbn = request.form.get('isbn', '').strip()
    costo = request.form.get('costo', '').strip()

    #2. creamos el nuevo libro 
    nuevo_libro = {
        "_id": request.form.get('id'), 
        "titulo": request.form.get('titulo'),
        "paginas": request.form.get('paginas'), 
        "editorial": request.form.get('editorial'),
        "isbn": request.form.get('isbn'),
        "costo": request.form.get('costo')
    }

    # 3. Validacion de campos vacíos
    if not all([id_libro, titulo, paginas, editorial, isbn, costo]):
        flash("Error: Todos los campos son obligatorios y no pueden estar vacíos.")
        return redirect(url_for('index'))

    # 4. Validacion de tipos de datos (Numeros)
    try:
        paginas_int = int(paginas)
        costo_float = float(costo)
        if paginas_int < 0 or costo_float < 0:
            raise ValueError("Los números no pueden ser negativos.")
    except ValueError:
        flash("Error: 'Páginas' debe ser un número entero y 'Costo' debe ser un número válido.")
        return redirect(url_for('index'))

    # 5.Verificar id duplicados
    if libros.find_one({"_id": nuevo_libro["_id"]}):
        flash(f"Error: El ID '{nuevo_libro['_id']}' ya existe.")
        return redirect(url_for('index'))
   
    # Verificar ISBN duplicados
    if libros.find_one({"isbn": nuevo_libro["isbn"]}):
        flash(f"Error: El ISBN '{nuevo_libro['isbn']}' está duplicado.")
        return redirect(url_for('index'))
    
    # Insertamos el libro en la base de datos
    libros.insert_one(nuevo_libro)
    flash("Libro agregado exitosamente.")  
    return redirect(url_for('index'))

@app.route('/eliminar/<id_libro>', methods=['POST'])
def eliminar(id_libro):
    if libros.find_one({"_id": id_libro}):
        libros.delete_one({"_id": id_libro})
        flash("Libro eliminado exitosamente.")
    else:
        flash("El libro no existe.")
 
    return redirect(url_for('index'))

@app.route("/editar/<id>") 
def editar(id):
    libro = libros.find_one({"_id": id})
    return render_template("editar.html", libro=libro)

@app.route("/actualizar/<id>", methods=["POST"])
def actualizar(id):
    # 1. Capturamos y limpiamos datos
    titulo = request.form.get("titulo", "").strip()
    paginas = request.form.get("paginas", "").strip()
    editorial = request.form.get("editorial", "").strip()
    isbn = request.form.get("isbn", "").strip()
    costo = request.form.get("costo", "").strip()

    # 2. Validacion de campos vacios
    if not all([titulo, paginas, editorial, isbn, costo]):
        flash("Error: No se admiten campos vacíos al editar.")
        return redirect(url_for('editar', id=id))
    
    # 3. Validacion de duplicados (ISBN)
    # Buscamos si existe otro libro (diferente ID) con el mismo ISBN
    libro_existente = libros.find_one({"isbn": isbn, "_id": {"$ne": id}})
    if libro_existente:
        flash(f"Error: El ISBN '{isbn}' ya está registrado en otro libro.")
        return redirect(url_for('editar', id=id))
   
    # 4. Validacion numerica
    try:
        paginas_int = int(paginas)
        costo_float = float(costo)
    except ValueError:
        flash("Error: Ingrese valores numéricos válidos.")
        return redirect(url_for('editar', id=id))

    # 5. Actualizacion
    libros.update_one(  
        {"_id": id},
        {"$set": {
            "titulo": titulo,
            "paginas": int(paginas),
            "editorial": editorial,
            "isbn": isbn,
            "costo": float(costo)
        }} 
    )
    flash("Libro actualizado correctamente")
    return redirect(url_for('index'))

"""
@app.route('/editar/<id_libro>', methods=['POST'])
def editar(id_libro):
    #verificamos que el libro a modificar exista
    if not libros.find_one({"_id": id_libro}):
        flash("Libro no encontrado.")
        return redirect(url_for('index')) #volvemos al menu
    else: #el libro existe, entonces capturamos los datos
        libro_actualizado = {
            "titulo": request.form.get('titulo'),
            "cant_paginas": request.form.get('cant_paginas'),
            "editorial": request.form.get('editorial'),
            "isbn": request.form.get('isbn'),
            "costo": request.form.get('costo')
        }
        libros.update_one({"_id": id_libro}, {"$set": libro_actualizado})
        flash("Libro actualizado exitosamente.")
        return redirect(url_for('index')) #volvemos al menu
"""


"""
#pidiendo el id para buscar el libro
@app.route('/buscar/<id_libro>', methods=['GET'])
def buscar(id_libro):
    libro = libros.find_one({"_id": id_libro})
    if libro: #si encontramos el libro, lo mostramos y volvemos al menu
        return render_template('index.html', libros=[libro])
    flash("Libro no encontrado.") #si llegamos aca, no se encontro el libro
    return redirect(url_for('index')) #y volvemos al menu
"""
#buscar libro por titulo
@app.route("/buscar", methods=['GET'])
def buscar():
    titulo = request.args.get("titulo")   
    resultados = libros.find({"titulo": {"$regex": titulo, "$options": "i"}}) #busqueda mas flexible, y la opcipn "i" hace q no sea keysensitive
    
    return render_template("index.html", libros=resultados)





if __name__ == '__main__':
    # ejecutamos la app en el puerto 80 del contenedor
    app.run(host='0.0.0.0', port=80, debug=True)

