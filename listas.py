##################### Listas ##################################################


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



