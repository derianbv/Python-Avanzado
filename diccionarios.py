################################## diccionarios #################################

#Se crea un espacio en memoria que posee referencias a las claves y a los valores


#Se maneja con una tabla hash:

    #Se maneja hash por su eficiencia, ya que el diccionario NO tiene indexación, solo se agrega una llave y la manera más rapida de llegar a él en el conjunto de datos del diccionario es con el número que genera la hash table f(x).

        #La complejidad de la búsqueda, inserción y eliminación es O(1) por la función hash que consigue de una la ubicación del elemento.

            #En el peor de los casos dos llaves generarán el mismo numero hash y se crean entonces las coliciones, en el peor de los casos la complejidad será 0(n) porque debe iterar sobre la lista de items en esa posición de la hash.



#Sintaxis:

#miDic = {clave : valor, clave2, valor2}
    
    #clave: debe ser un valor INMUTABLE de python (tuplas, números, strings, frozenSets) debido a que al aplicar la función hash si el valor cambiara ya no se podría acceder a su indice dentro de la tabla. Se necesita que sea siempre el mismo.  NO SE PUDE REPETIR LA LLAVE POR LO MISMO.

    #Valor: cualquier objeto de Python. 

#Ejemplo: 

direccion = 'Av 34'
cons = "String no es variable"
lista = []

dic = {
    1 : 1,
    2 : {2 : '2d'},
    (3,3) : 'mama',
    'casa': direccion,
    cons : 3
}

 ######### Acceso a la lista #########: 

