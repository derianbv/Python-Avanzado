##################### Listas ##################################################
################################################################################


############ En memoria ####################################
#pasos en memoria para creación de lista: 


#0.  pongamos el ejemplo de la creación de esta lista en python: lista = [1,2,3,4]

#1. se crean los espacios de memoria para 1, para 2, para 3 y para 4. 
    # cada espacio es de este tipo: [type | value | id ], id es la dirección en memoria ram del objeto y es lo que retornaria la el método id(). 


lista = [1,2,3,4]
for i in lista:
    print(f"[{type(i)} | {i} | {id(i)}]")

#en consola se imprime: 
    
#[<class 'int'> | 1 | 140732167756352]
#[<class 'int'> | 2 | 140732167756384]
#[<class 'int'> | 3 | 140732167756416]
#[<class 'int'> | 4 | 140732167756448]


#2. Después se crea un objeto tipo lista en la memoria y sus valores internos son solo referencias (o punteros) a los números de la lista usando su id()


print(f"[{type(lista)} | {lista} | {id(lista)} | {[id(i) for i in lista]}]")
for i in lista:
    print(f"[{type(i)} | {i} | {id(i)}]")



#[<class 'list'> | [1, 2, 3, 4] | 140732167756352 | id de elementos internos: [140732167756384, 140732167756416, 140732167756448, 140732167756480]]
#[<class 'int'> | 1 | 140732167756384]
#[<class 'int'> | 2 | 140732167756416]
#[<class 'int'> | 3 | 140732167756448]
#[<class 'int'> | 4 | 140732167756480]

#y estos números internos coinciden con las id de cada número.
    



#3. por último se crea el espacio de memoria para la variable "lista" de este modo:
# [type: variable:list | 140732167756352 | 1407321677564342 ] 
# valor de la variable está la referencia al id de la lista en memoria. 

################################################################






# Características de las listas: #####################################3

# 1. Listas: arreglo dinámico, se implementan por medio de arreglos estáticos que al llenarse se duplica su tamaño.    
# 2. Es de la clase "Lista"
# 3. Es mutable. 


lista1:list = [1,2,3,4]

#4. Se pueden meter todo tipo de datos a la lista: 
 
lista2 = [True, False, lista1, 32, 43.2, 'Hola']

#5. Se puede acceder a los elementos desde el final de la lista con los números negativos: 
# en este caso ya no iniciarían en -0 sino en -1

print(lista2[-1])
#retorna 'Hola'



#6. Desempaquetar las listas: se pueden desagrupar los elementos de una lista desempaqutandola de dos maneras:

#6.1 Manera 1: asignando una cantidad de variables igual a la cantidad de elementos de la lista: 

a,b,*c = lista2 #si tiene asterisco va a agarrar lo que sobre
#esto la descompone y asigna en orden los elementos de la lista a las variables. 
print(c)
#SOLO SE PUEDE TENER UNA VARIABLE CON ASTERISCO




#si el "*" se pone en la variable del medio, ésta tomará los valores del medio, en el ejemplo uno y tres tomarán los valores de las puntas:
uno, *dos, tres = [1,2,3,4,5,6,7]
print(dos)
#[2, 3, 4, 5, 6]


uno, *dos, tres, cuatro = [1,2,3,4,5,6,7]
print(dos)
#[2, 3, 4, 5] las ultimas dos variables (tres, cuatro) = 6,7 y uno = 1, por lo tanto imprime ls valores restantes

*uno, dos, tres, cuatro = [1,2,3,4,5,6,7]
print(uno)
#[1,2,3,4]



#6.2 Manera 2: con el operador "*" si se agrega antes de una lista va a desgrupar a los elementos
#Ejemplos: 

lista3 = [*lista1, *lista2]
print(lista3)
#en este caso los elementos de la lista tres van a hacer los que esten por dentro de la lista1 y lista2.






 ###################################### Métodos de las listas ##############################

#1. len(lista): largo de la lista




#2. lista.index(a,inicio,final): devuelve el indice de la primera aparición de a en la lista

#Se puede colocar un rango de busqueda, en el ejemplo de abajo va del indice 2 al indice 5 (por defecto no se piden)
#busque de izquierda a deracha, así que si se pone el inicio del rango de búsqueda en el ultimo item, va a salir que el elemento no está en la lista así sí esté 
retorna la primera isntacia que encuentre de este item 
palabras = ["Yo", "soy", "un", "Yo", "soy", "Pythonista"]

print(palabras.index("soy", 2, 5)) 

#3. lista.pop(): borra y retorna el último elemento de la lista.
# lista.pop(3): borra el elemento en la posición 3 




#4. lista.append(x): mete lo que sea que es x al final de la lista. Retorna None




#5. lista.extend(iterable): puede pegar dos listas: 

lista4 = ['a','b','c']
lista4.extend(lista1)
#['a', 'b', 'c', 1, 2, 3, 4]




#6. lista.insert(i, x): agrega en la posición i el elemento x: 
lista4.insert(2,"ELEMENTO") 
#Acá agrego en el indice 2 (originalemente estaba la c) el string ELEMENTO, esto corre a la "c" a la derecha.
#print() = ['a', 'b', 'ELEMENTO', 'c', 1, 2, 3, 4]

#Qué sucede si le paso un indice fuera de la lista? 

lista4.insert(4444,"ÚLTIMO")
#Lo pone al final de la lista y ya: 
#print() = ['a', 'b', 'ELEMENTO', 'c', 1, 2, 3, 4, 'ÚLTIMO']




#7. lista.remove(x): remueve la primera instancia del elemento que encuentre de izq a derecha
lista4.remove('a')
#['b', 'ELEMENTO', 'c', 1, 2, 3, 4, 'ÚLTIMO']

#---------- comparación ---------------
#lista.remove(x): elimina la primera aparición de x,
#lista.pop(): elimina y retorna el último elemento de x, 
#lista.pop(i): elimina y retorna el elemento en i. 


#8. lista.clear(): elimina todos los elementos de la lista. 




#9. lista.sort(key,reverse): NO DEVUELVE LA LISTA ORDENADA, SOLO LA ORDENA Y DEVUELVE NONE.
#Funciona con Timsort internamente
#Ordena ascendentemente una lista en python 
# recibe dos parámetros lista.sort(key: función con la que ordenar, reverse = true or false: pasarlo a orden descendente
#Key puede ir con: 
    # key = lambda
    # key = f(x)
    # key = len 


# lista1 = [4,2,6,1,445,0]

# #print(lista1.sort())
# #print(lista1)
# #[0, 1, 4, 5, 6, 445]


#Mapea a la list entera con esta funcion y luego dependiendo del resultado crea la lista 
# def fun1(x:int): 
#     return (x**2 - x*2)

# lista1.sort(key=fun1)
# print(lista1)
# [1, 2, 0, 4, 6, 445]

#Info más detallada en el archivo funciones.py en la parte de sorted()



#10. lista.reverse() revierte la lista, retorna none



#11. lista.count(x) cuenta la cantidad de veces que se encuentra x en la lista, retorna un entero.



#12. lista.copy() crea una copia en la memoria de una lista (Shallow Copy)


#string.split(",": es un delimitador que queremos ecoger, por defecto es un espacio vacio " ") convierte a una lista con valores separados por espacio

#Shallow quiere decir que copia y CREA elementos nuevos cuando solo tienen una capa de profundidad, eje: 1,True, "mamá", 32. 

copiaLista = lista4.copy()
print(f"Espacio en memoria de copiaLista: {id(copiaLista)} != {id(lista4)} :espacio en mem de lista4")
#print = Espacio en memoria de copiaLista: 1333750318464 != 1333750318528 :espacio en memoria de lista4
#mas info de id en el archivo funciones y metodos en la parte de id()

#Sin embargo, al realizar copia a un arreglo que tenga más capas de profundidad, es decir que posea objetos que por dentro posean objetos, estos objetos internos no se CREAN nuevos en memoria sino que se realiza una referencia en el segundo arreglo a los elementos del arreglo copiado. Ejemplo: 

dict = {'nombre':'Lucia'}

lista3D = [1,2,3,[4,[5,6]], dict] #el elemento lista3D[3] es una lista también que tiene una lista interna [4,[5,6]]. 
copia3D = lista3D.copy()

print(f'lista3D: {lista3D}, id: {id(lista3D)} || copia3D: {copia3D}, id: {id(copia3D)}')
#print = lista3D: [1, 2, 3, [4, 5]], id: 2659303676224 || copia3D: [1, 2, 3, [4, 5]], id: 2659303676288
#tienen diferente id o sea espacio en memoria, pero veamos el id del elemento en la posición tres de ambas listas: 

print(f'{id(lista3D[3])} == {id(copia3D[3])}')
# 1362830542720 == 1362830542720 es el mismo, entonces al realizar cambios en esa lista interna de la copia se reflejarán en la lista inicial: 

copia3D[3][1].append("CASPER") #copia
print(lista3D)#original 
#[1, 2, 3, [4, [5, 6, 'CASPER']], {'nombre': 'Lucia'}] se ve el cambio de copia3D en la original lista3D. 
#Esto mismo sucede con estructuras que posean datos internos como diccionarios, listas, tuplas, etc.
#para evitar eso se debe realizar una DEEP copy con el módulo copy (deepcopy):

import copy

DeepLista3D = copy.deepcopy(lista3D)
#copia todos los niveles de profundidad: una lista dentro de una lista, dentro de una lista ... etc.
#ahora sí esta copia no modifica a la lista original. 

DeepLista3D[3][1].append("SOLO APAREZCO EN LA COPIA")

print(f'{lista3D} \n {DeepLista3D}')
# [1, 2, 3, [4, [5, 6, 'CASPER']], {'nombre': 'Lucia'}] 
# [1, 2, 3, [4, [5, 6, 'CASPER', 'SOLO APAREZCO EN LA COPIA']], {'nombre': 'Lucia'}] 

#del(lista[0]) borra el item de la lista en la posicion 0 

#Igualar listas. 

listaA = [1,2,3,4]
listaB = listaA 
#Ambas apuntarás al mismo espacio en memoria y cambios se veran reflejados en ambas listas 

##################### Repetición y concatenación #####################################


#1. Concatenación: 
    #solo se puede hacer entre el mismo tipo de datos!!!!!: 

listaConcatenada = lista1 + lista2 #une las listas


#2. Repetición. 
    #Solo se puede hacer multiplicando con positivos, no con números con decimales, si se hace por un número negativo, el arreglo saldrá vacío: 

peque = [1,2]
grande = peque*4
print(grande)
#[1, 2, 1, 2, 1, 2, 1, 2]

vacio = peque * -1
print(vacio)
#[]




############################# Slicing #############################################
#Ver el archivo de slicing.py 




########################### list-comprehention #####################################

#Sirven para crear listas con base a otras sin tener que usar append(), por lo tanto se realiza más rápido.
#también se pueden crear listas con ranges sin necesidad de otra lista.


#Sintaxis: entre parentesis porque es una lista: [ elemento for i in lista1 condición(opcional) ]
#ejemplo: 

lista1 = [23,4,54,78,21,3,4,0,95]


#sitaxis básica para copiar de uno a otro:
listaMenores = [i for i in lista1]
print(listaMenores)
#[23, 4, 54, 78, 21, 3, 4, 0, 95]



#voy a crear una lista con numeros pequeños basada en lista1: 
listaMenores = [i for i in lista1 if i < 10]    
print(listaMenores)
#[4, 3, 4, 0]

#puedo también modificar la i: 

modi = [i**2 for i in lista1 if i < 10]
print(modi)
#[16, 9, 16, 0]




#List con range, numeros del 1 al 14:

numeros = [i+1 for i in range(14)]
print(numeros)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


#se pueden anidar for:
#en este ejemplo se hace una rama por cada x hasta 3 ramas, y luego con cada rama salen tres para 3. 
#si el par de numeros sumados es par se incluye en la lista de pares.
pares = [(x,y) for x in range(3) for y in range(3) if (x+y)%2==0]
print(pares)
#[(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]



#ejemplo creación de matriz:

matriz = [[i+1,i+2,i+3] for i in range(3)]
print(matriz)
