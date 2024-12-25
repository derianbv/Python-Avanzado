##########################################  RUTAS ############################################################
'''
1. Ruta relativa (en relación con la carpeta actual) 
Se basa en un sitema que se establece con la carpeta actual, es decir, para acceder a algo que este en la misma carpeta, por ejemplo: 

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
