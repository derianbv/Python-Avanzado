################################# Kwards ############################################### :p 
'''
--------------------------------Tipos de parámetros para paserla a una f(x) ---------------------------------
Se definen por la manera en la que se pasan en la función al momento de invocarla


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
2. Con nombre: no importa el orde en que se pasen ya que se definen por su nombre, como el caso de arriba func(b=2,a=1), acá le paso los datos al contario pero python es capas de saber a cual me refiero por el nombre.
3. Con valor por defecto: Puedo setear valores por defecto en las funciones, si ese dato no se lo paso no da error porque ya tiene un por defecto: def func(a, b=10) es valido llamarla con: func(1) o func(1, 20)
4. Posicional solamente: con "/" todos los parametros que están antes solo pueden ser pasados posicionalmente al llamar la función, es decir que si se pone func(a=3) esto dará error. 
5. Con nombre solamente:	 con "*" todos los parametros que están después solo pueden ser pasados con su nombre al llamar la función, es decir que si se pone func(3) esto dará error, tiene que ser func(a=3)
6. Posicionales variables:  seteando la func con f(*palbraLaQueSea), !!!exclusivamente un "*" le digo que me reciba parametros posicionales UNICAMENTE, no parametros de nombre, y los guardará dentro de la función
en una tupla llamada palabraLaQueSea, sin el *.
Ejemplo: 
'''
def suma(*numeros): 
  print(numeros)
  print(sum(numeros))
#----------------------------
suma(1,2) 
#OUT:
#(1, 2)
#3
suma(4,4,4,4,4,4) 
#(4, 4, 4, 4, 4, 4)
#24

'''
7. Con nombre variables: seteando la func con f(**platano) voy a agarrar UNICAMENTE todos los parametros con nombre y los guardaré en diccionario llamado platano
Ejemplo:
'''

def crearDiccPersona(**platano): 
  print(platano) 


crearDiccPersona(nombre='Santi', caco=True)
#OUT:
#{'nombre': 'Santi', 'caco': True}

crearDiccPersona(nombre='derian', estudiante=True, notas=(4.5,5), edad=22 )
#{'nombre': 'derian', 'estudiante': True, 'notas': (4.5, 5), 'edad': 22}


#Finalmente, estos dos se pueden combinar: 

def crearTuplaDicc(primerParam, *posicionales,**nombrados):
  print(f'soy el primer parametro: {primerParam}')
  print(f'Somos todos los otros parametros que van después: {posicionales}')
  print(f'Soy un diccionario con las var nombradas: {nombrados}')
crearTuplaDicc('gato', 3, 'dia', False, None, mama='feliz', año=2024)

