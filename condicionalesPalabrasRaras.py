


################################## Condicionales ################################################

###################### is ###########################
'''
- is	La identidad del objeto	| a is b → True si a y b son el mismo objeto.
- ==	Los valores (igualdad)	| a == b → True si los valores son iguales.
'''

#1. Verifica si dos variables apuntan al mismo espacion en memoria, esencialmente si dos objetos son el mismo: 

x = 10
y = 10

print(x is y)  # True: Ambos usan la misma referencia en memoria, los numeros pequeños apuntan a un mismo lugar en memoria 

z = 1000
w = 1000

print(z is w)  # True o False, depende de la implementación

#También para las clases-------------------------------------------------------------------: 

class MyClass:
    pass

obj1 = MyClass()
obj2 = obj1 #
obj3 = MyClass()

print(obj1 is obj2)  # True: Mismo objeto
print(obj1 is obj3)  # False: Diferentes instancias

########## Diferencia con ==: --------------------------------------

a = [1, 2, 3]
b = [1, 2, 3]  # b es un objeto diferente con el mismo contenido

print(a is b)  # False: No son el mismo objeto
print(a == b)  # True: Los valores son iguales

################## igual para la negación: ---------------------------

a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)  # True: No son el mismo objeto en memoria
print(a != b)      # False: Sus valores son iguales



#################################################### with ######################################################:
#Cierra el archivo automáticamente:

with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
# No necesitas cerrar el archivo manualmente


#################################################### and or in not ######################################################:
a = 0
b = 5
print(a and b)  # 0: `and` retorna el primer valor "falso".
print(a or b)   # 5: `or` retorna el primer valor "verdadero".
print(not a)    # True: `not` invierte la verdad lógica.


##################################### verificar el tipo de dato de una variable ###################################3

x = 42
print(isinstance(x, int))  # True: x es un entero
print(isinstance(x, str))  # False: x no es una cadena

#También se puede con clases (o modelos de django): 

from django.contrib.auth.models import User

# Crear un usuario (simulación)
user = User(username="testuser")

# Verificar si `user` es una instancia del modelo `User`
print(isinstance(user, User))  # True





##################################### Ellipsis ######################################################

# Es un objeto y puede ser evaluable (diferente a pass que no puede ser evaluable (Ej: print(pass) = error, print(...) = Ellipsis), pass solo se puede usar en condicionales o bucles: 
# EPP: Es un placeholder que busca mostrar que el objeto está pendiente: 

estructura = [1, 2, ..., 4, 5]

for elemento in estructura:
    if elemento is ...:
        print("Elemento pendiente")
    else:
        print(f"Elemento: {elemento}")

'''
Elemento: 1
Elemento: 2
Elemento pendiente
Elemento: 4
Elemento: 5
'''
####### Placeholder para indicat que hay que hacerlo después: 

class MiClase:
    def metodo_pendiente(self):
        ...  # Indicativo de implementación futura

    def metodo_realizado(self):
        print("Este método ya está implementado")

obj = MiClase()
obj.metodo_realizado()  # Imprime: Este método ya está implementado




###################### del ######################################## 
#Borra a apuntadore (variables) de objetos en memoria, si ya no hay más apuntadores a dicho objeto el recolector de basura borra dicha memoria. 


1 Ejemplo. #borrar un atributo de una clase

class MiClase:
    def __init__(self):
        self.atributo = "valor"

obj = MiClase()
print(obj.atributo)  # Imprime: valor

del obj.atributo  # Elimina el atributo "atributo"
# print(obj.atributo)  # AttributeError: 'MiClase' object has no attribute 'atributo'

#---------------------------------


mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
del mi_diccionario['b']  # Elimina la clave 'b'
print(mi_diccionario)  # {'a': 1, 'c': 3}


#-------------------------------------

mi_lista = [1, 2, 3, 4, 5]
del mi_lista[1:3]  # Elimina los elementos en los índices 1 y 2 (2 y 3)
print(mi_lista)  # [1, 4, 5]


#-------------------------------------

x = 10
print(x)  # Imprime: 10

del x  # Elimina la variable x

# print(x)  # NameError: name 'x' is not defined







############################### Asserts ######################################
#Más que todo para pruebas de código, se usa para hacer que se dispare un mensaje si el comparativo no es verdadero:
assert <condición>, <mensaje opcional>


#Ejemplos: 

x = 10
assert x > 5  # No pasa nada porque la condición es verdadera
assert x < 5, "x no es menor que 5"  # Lanza AssertionError con el mensaje
#OUT: AssertionError: x no es menor que 5


#---------------------------------------------

def dividir(a, b):
    assert b != 0, "El divisor no puede ser cero"
    return a / b

print(dividir(10, 2))  # 5.0
print(dividir(10, 0))  # AssertionError: El divisor no puede ser cero



#################################################### yield #################################################

'''
#EPP: AHORRA MEMORIA
#Crea una función Generadora, ahorra memoria al ir solo creando lo que necesito, a diferencia de una lista que se debe guardar de una en la memorai: 


Cuando usas yield, la función no pierde su estado entre llamadas como lo haría con un return. En lugar de ejecutarse desde el principio cada vez que se invoca, una función con yield se pausa en el último yield y recuerda:

-Dónde estaba en el código (la posición exacta después del último yield).
-Los valores de las variables locales (su "estado interno").
Esto es posible gracias al objeto generador que crea yield. Este objeto lleva el control de lo que ya se ha generado y de lo que queda por generar.
'''

def contador():
    n = 1
    while n <= 3:
        yield n
        n += 1

gen = contador()  # Crea el generador
print(next(gen))  # 1 (se pausa en `yield n`)
print(next(gen))  # 2 (continúa desde `n += 1`)
print(next(gen))  # 3 (continúa y se pausa nuevamente)
# print(next(gen))  # StopIteration (ya no hay más valores)


#------------ numeros infinitos:

def numeros_infinito():
    n = 0
    while True:
        yield n
        n += 1

gen = numeros_infinito()
print(next(gen))  # 0
print(next(gen))  # 1

#Con una lista, esto sería imposible porque necesitarías almacenamiento infinito.


############################################ Global - non Local ##############################3

# 1. Global, llama a variables por fuera de un contexto: 

x = 10
def cambiar():
    global x
    x = 20

cambiar()
print(x)  # 20

#------------ también puede crear variables por fuera de una función sin return: 

def crear_global():
    global nueva_var  # Declaramos una nueva variable global
    nueva_var = "Soy global"

crear_global()
print(nueva_var)  # "Soy global"


# 2. nonlocal llama a una variable que este en el contexto de una función padre: 


def funcion_externa():
    x = 10  # Variable del ámbito de `funcion_externa`

    def funcion_interna():
        nonlocal x  # Declaramos que queremos modificar `x` del ámbito externo
        x = 20  # Modificamos `x`

    funcion_interna()
    print(x)  # 20

funcion_externa()
