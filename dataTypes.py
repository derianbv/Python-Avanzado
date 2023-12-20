
################## DATOS ITERABLES o subscriptables [] ###############################
#1. Listas.
#2. Tuplas.
#3. Strings.
#4. Diccionarios.
#5. Sets.
#6. Archivos (se abre un archivo en python, se puede iterar a traves de sus líneas, txt, csv, json)



################################ Callables ####################################
#1. F(x), lambda.
#2. métodos.
#3. Clases.
#Existe un método para saber si algo es callable, ejemplo: 
print(callable(lambda x: x+1))
#True





##################### Repetición y concatenación #####################################

lista1 = [1,2,3]
lista2 = [4,5,6]
#1. Concatenación: 
    #solo se puede hacer entre el mismo tipo de datos!!!!!: 

listaConcatenada = lista1 + lista2 #une las listas
#[1,2,3,4,5,6]

#2. Repetición. 
    #Solo se puede hacer multiplicando con positivos, no con números con decimales, si se hace por un número negativo, el arreglo saldrá vacío: 

peque = [1,2]
grande = peque*4
print(grande)
#[1, 2, 1, 2, 1, 2, 1, 2]

vacio = peque * -1
print(vacio)
#[]







############################# Datos Inmutables ##########################################
#1.  Números de cualquier tipo: es porque al asignar una variable con algún número de -5 a 255 (por su uso frencuente) lo que hace el programa es asigarle de entrada un espacio de memoria a estos número, por lo tanto, al crear una var x = 5, o n = 5, lo que se hace es apuntar todas las variables a ese espacio que contiene el 5 por tema de eficiencia, cuando se crea un número fuera de ese rango ahí sí se crea un nuevo espacio en memoria para ese número, cuando la variable "modifica el número" lo que se hace en realidad es que se crea un núevo espacio en memoria para el núevo número más que cambiar el espacio de memoría que ya existia. (si ese espacio que ya existía no es utilizado por otros apuntadores se desecha por el recolector de basura)

#2. String: No puedo cambiar ningun indice str[0] = 'm' ERROR
#3. Tuplas. 
#. Frozen Sets