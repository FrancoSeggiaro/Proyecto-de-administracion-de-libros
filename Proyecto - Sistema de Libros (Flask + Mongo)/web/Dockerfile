#usamos una imagen base que soporte python y apache 
FROM python:3.9-slim

#instalamos apache y depencias del sistema
     
# Instalamos apache y el modulo wsgi para python 3
RUN apt-get update && apt-get install -y \
    apache2 \
    libapache2-mod-wsgi-py3 \
    && rm -rf /var/lib/apt/lists/*

#directorio de trabajo #no se si esta bien 
WORKDIR /app 

#copiamos requerimientos (linea13) y los instalamos (linea14)
COPY requirements.txt .  
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt
# "--no-cache-dir" es para evitar que pip guarde los archivos temporales, ya que luego del build
# estos archivos no seran necesarios ya que contamos con la imagen.

#Copiamos el codigo de la aplicacion al contenedor
COPY . .

# Configuracion de Apache para servir la aplicación Flask
COPY ./flask_app.conf /etc/apache2/sites-available/000-default.conf

# Permisos para que Apache pueda leer la app
RUN chown -R www-data:www-data /app && chmod -R 755 /app

#exponemos el puerto de apache
EXPOSE 80

#iniciamos la aplicacion 
# 6. Iniciamos Apache en primer plano
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

#Foreground le ordena a Apache que se ejecute en primer plano y mantiene el contenedor activo.
