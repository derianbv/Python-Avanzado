################################ Slicing ###############################
#Se permite para estos tipos de datos entre otros: 
#1. Listas, tuplas
#2. Strings 
#3. Arreglos de numPy 
#4. Clases personalizadas que incluyan el método mágico: __getitem__ 



#Sintaxis lista[inicio de intervalo(incluye): fin de int (pared:excluye) : pasos (solo enteros)]
    #inicio: si no se pone nada se asume que es 0: [:n:m] = [0:n:m]
    #fin: si no se pone nada se asume que es el largo del arreglo: [n::m] = [n:len(arreglo):m]
    #pasos: si no se pone nada se asume que va a pasos de a 1: [n:m:] = [n:m:1]

lista = [0,1,2,3,4,5,6,7,8,9]
print(lista[0:3])
#[0, 1, 2]

#En reversa ("-1" representa el último elemento de un arreglo): 
print(lista[::-1])
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(lista[::-2])
#[9, 7, 5, 3, 1]


#(-n puede reprensentar el numero de elemento contando de derecha a izquierda (reverted) empezando por el -1):
#Quiero imprimir del 9 a 6: 
print(lista[:-5:-1]) #le pedí que vaya en reversa con el -1 y que llegue hasta la posición -5 sin incluirlo. 
#[9, 8, 7, 6]





######################### MODIFICAR ARREGLOS CON SLICING ####################################

#Es posible agarrar intervalos de arreglos y modificarlos con slicing, ejemplo: 
lista = [1,1,2,2]
lista[:2] = [4,4]

print(lista)
#[4, 4, 2, 2]



#Segundo ejemplo, quiero que toda la matriz de abajo tenga 0's unicamente.
binarios = [1,0,1,0,1,0,1,1,1,1]

#ceros: 
binarios[:6:2] = [0] * binarios[:6:2].count(1)
print(binarios)
#[0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

#en este intervalo (0-6] en un paso de a dos (distancia de cada 1) cambia cada indice por [0]*cantidad de unos (count(1)) en el intervalo, o sea: [0,0,0], esta propiedad de las listas se llama repetición.

#cambiar la ultima parte por 0's (1,1,1,1 -> 0,0,0,0). 


binarios[6:] = [0]*binarios[6:].count(1)
print(binarios)
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



################################ slicing en sub listas ###################################
lista2D = [1,2,3,[4,5,6,7,8,9]]
print(lista2D[3][::-2])
#[9, 7, 5]



################################# shallow copy #####################################
copiaSuperficial = lista2D[:] #se copian los datos de una dimensión

segundaRef = lista2D #esto no es una copia sino poner un segundo nombre a la misma lista en memoria.






