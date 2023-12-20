################################## diccionarios #################################

#Se crea un espacio en memoria que posee referencias a las claves y a los valores


#Se maneja con una tabla hash:

    #Se maneja hash por su eficiencia, ya que el diccionario NO tiene indexación, solo se agrega una llave y la manera más rapida de llegar a él en el conjunto de datos del diccionario es con el número que genera la hash table f(x).

        #La complejidad de la búsqueda, insercción y eliminación es O(1) por la función hash que consigue de una la ubicación del elemento.

            #En el peor de los casos dos llaves generarán el mismo numero hash y se crean entonces las coliciones, en el peor de los casos la complejidad será 0(n) porque debe iterar sobre la lista de items en esa posición de la hash.


#Los diccionarios SON MUTABLES.


#Sintaxis:

#miDic = {clave : valor, clave2, valor2}
    
    #clave: debe ser un valor INMUTABLE de python (tuplas, números, strings, frozenSets) debido a que al aplicar la función hash si el valor cambiara ya no se podría acceder a su indice dentro de la tabla. Se necesita que sea siempre el mismo.  NO SE PUDE REPETIR LA LLAVE EN EL DICCIONARIO POR LO MISMO.

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



############# Acceso al Diccionario ############: 
#Cuando accedo a la llave en verdad estoy accedindo al valor por medio de su indice, pero en este caso el indice es la llave (porque no hay indexación con números ya que el diccionario no es secuencial), Lista acceso: lista[0] = 'jose', dicc['nombre'] = jose.  

#Sintaxis: diccionario[llave]

print(dic[(3,3)])
#mama
print( dic['casa'] )
#Av 34, puedo cambiar este valor si así lo deseo:

dic['casa'] = 'Calle 146'
print(dic['casa'])
#Calle 146










#########333 Los diccionarios están ordenados POR ORDEN de inserción: 

# NOOO significa que el primer elemento agregado al dicci tenga indicie [0]
# Crear un diccionario con eventos en una línea de tiempo
eventos = {'Evento 1': '2001', 'Evento 2': '2002', 'Evento 3': '2003'}

# Imprimir los eventos en el orden en que ocurrieron
for evento, año in eventos.items():
    print(f'{evento} ocurrió en {año}')

#Evento 1 ocurrió en 2001
#Evento 2 ocurrió en 2002
#Evento 3 ocurrió en 2003