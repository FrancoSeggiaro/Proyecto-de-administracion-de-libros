import sys
import site
import os

# 1. Agregamos el directorio de la aplicación al path
sys.path.insert(0, "/app")

# 2. Agregamos el path de las librerías del sistema donde pip instala todo
# Esto es vital para corregir el ModuleNotFoundError
sys.path.append('/usr/local/lib/python3.9/site-packages')

from app import app as application