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

########## Diferencia con ==: 

a = [1, 2, 3]
b = [1, 2, 3]  # b es un objeto diferente con el mismo contenido

print(a is b)  # False: No son el mismo objeto
print(a == b)  # True: Los valores son iguales

s
