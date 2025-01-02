
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
