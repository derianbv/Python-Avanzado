##################### Listas ##################################################
################################################################################

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

a,b,c,d,e,f = lista2
#esto la descompone y asigna en orden los elementos de la lista a las variables. 
print(a)

#6.2 Manera 2: con el operador "*" si se agrega antes de una lista va a desgrupar a los elementos
#Ejemplos: 

lista3 = [*lista1, *lista2]
print(lista3)
#en este caso los ementos de la lista tres van a hacer los que esten por dentro de la lista1 y lista2.








 ###################################### Métodos de las listas ##############################

#1. Len(): largo lista




#2. lista.index(a): devuelve el indice de la primera aparición de a en la lista

#Se puede colocar un rango de busqueda, en el ejemplo de abajo va del indice 2 al indice 5
#busque de izquierda a deracha, así que si se pone el inicio del rango de búsqueda en el ultimo item, va a salir que el elemento no está en la lista así sí esté 
palabras = ["Yo", "soy", "un", "Yo", "soy", "Pythonista"]

print(palabras.index("soy", 2, 5)) 

#3. pop(): borra y retorna el último elemento de la lista.
#pop(3): borra el elemento en la posición 3 




#4. append(x): mete lo que sea que es x al final de la lista




#5. extend(iterable): puede pegar dos listas: 

lista4 = ['a','b','c']
lista4.extend(lista1)
#['a', 'b', 'c', 1, 2, 3, 4]




#6. insert(i, x): agrega en la posición i el elemento x: 
lista4.insert(2,"ELEMENTO") 
#Acá agrego en el indice 2 (originalemente estaba la c) el string ELEMENTO, esto corre a la "c" a la derecha.
#print() = ['a', 'b', 'ELEMENTO', 'c', 1, 2, 3, 4]

#Qué sucede si le paso un indice fuera de la lista? 

lista4.insert(4444,"ÚLTIMO")
#Lo pone al final de la lista y ya: 
#print() = ['a', 'b', 'ELEMENTO', 'c', 1, 2, 3, 4, 'ÚLTIMO']




#7. remove(x): remueve la primera instancia del elemento que encuentre de izq a derecha
lista4.remove('a')
#['b', 'ELEMENTO', 'c', 1, 2, 3, 4, 'ÚLTIMO']

#remove(x): elimina la primera aparición de x,
#pop(): elimina y retorna el último elemento de x, 
#pop(i): elimina y retorna el elemento en i. 


#8. clear(): elimina todos los elementos de la lista. 




#9. sort(): 

