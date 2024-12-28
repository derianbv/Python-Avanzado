################################# Kwards ############################################### :p 
'''
--------------------------------Tipos de parámetros------------:



Tipo de Parámetro	      | Ejemplo de Definición	|  Ejemplo de Llamada
------------------------|-----------------------|-----------------------
-Posicional	            |def func(a, b):	      |   func(1, 2)
-Con nombre	            |def func(a, b):	      |func(a=1, b=2)
-Con valor por defecto	|def func(a, b=10):	    |func(1) o func(1, 20)
-Posicional solamente	  |def func(a, b, /):	    |func(1, 2)
-Con nombre solamente	  |def func(*, a, b):	    |func(a=1, b=2)
-Posicionales variables	|def func(*args):	      |func(1, 2, 3)
-Con nombre variables	  |def func(**kwargs):	  |func(a=1, b=2)


1. posicional: importa el orden, en def func(a, b) si le paso func(1, 2) entonces a=1, b=2 
