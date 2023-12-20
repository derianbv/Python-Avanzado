
################## DATOS ITERABLES ###############################
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
#1.  Números de cualquier tipo. 
# (cambiarlo es como decir que voy a cambiar (la naturaleza de ese color), solo terminaría de cambiar el color a otro pero no estaría cambiando el color original. 
#2. String
#3. Tuplas. 
#. Frozen Sets