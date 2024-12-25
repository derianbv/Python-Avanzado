##########################################  Paquetes ############################################################
'''
PROYECTO ESTRUCTURA:

proyecto/
    main.py
    utils/
        __init__.py
        calculadora.py
        conversor.py

Inicialmente, para volver una carpeta un paquete y poder llamarlo en otros, se debe usar __init__.py en esa carpeta:

# EN EL ARCHIVO: __init__.py:
#Suponiendo que hay una carpeta Utils que tiene a los archivos calculadora y conversor.py, que estas tienen funciones sumar e celcius a farenheit respectivamente: 

from .calculadora import sumar
from .conversor import celsius_a_fahrenheit

# Ahora puedo llamarlas en otro el archivo main.py: 

from utils import sumar, celsius_a_fahrenheit

print(sumar(3, 5))                   
print(celsius_a_fahrenheit(25))      


######################################## MOVERSER POR CARPETA #########################################3

############ Padres: 

1. Con las rutas relativas (caparta actual) yo puedo moverme a mis padres así: 

proyecto/
    main.py
    paquete/
        __init__.py
        modulo1.py
        subpaquete/
            __init__.py
            modulo2.py


#  para llamar una funcion que este en modulo 1 en mi archivo modulo 2, debo hacer lo siguiente: (paquete/subpaquete/modulo2.py)
from ..modulo1 import una_funcion 

que es lo mimso que: 

from proyecto/paquete/modulo1.py

y así hasta el infinito, ... = tre padres, .... = cuatro padres, teninedo en cuenta la carpeta actual. 









########################################## SYS #########################################################

import sys 

#Me da acceso a cosas internas del interpretador de python.

por ejemplo, sys.path es una lista en dónde python busca modulos cuando se usa import:

[
    '/home/user/proyecto',          # Ruta actual del script
    '/usr/lib/python3.11',          # Directorios estándar de Python
    '/usr/lib/python3.11/lib-dynload',
    '/home/user/.local/lib/python3.11/site-packages'
]

para agregar un lugar nuevo donde buscar: 

sys.path.append('/home/user/mi_carpeta_personal')

print(sys.executable) : esto saca cual es el interprete de python3 
'''


###################################### RUTAS ############################### 
'''
Absoluta y relativa. 

1. Absoluta: 
-No sirve para portabilidad, depende de cada sistema, hay librerias como OS para manejarlas. 
Empieza desde la raíz del sistema operativo: 

Window (Empieza desde C:\\): 
ruta_absoluta = "C:\\Usuarios\\usuario\\proyecto\\archivo.txt"

Linux (Empieza desde /): 
ruta_absoluta = "/home/usuario/proyecto/archivo.txt"

2. Relativa: 
Siempre se está desde la carpeta actual. 

/proyecto/
    main.py
    data/
        archivo.txt

Desde main.py, para acceder a archivo.txt la ruta_relativa es = "data/archivo.txt"
'''






