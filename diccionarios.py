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



########## Agregar al diccionario ###########:
#Escribimos una llave que no tengamos en el diccionario y le asinamos un valor: 


dic2 = {'num1':2,
        'edad':45}
dic['miLista'] = [4,4,4,4]
print(dic2)
#{'num1': 2, 'edad': 45}









############################ ORDEN #3#############################:


#Los diccionarios están ordenados POR ORDEN de inserción: 
# NOOO significa que el primer elemento agregado al dicci tenga indicie [0]
#Es imposible ordenar un diccionario por otro tipo de orden como por tamaño del número o largo del string, para hacer eso hay que convertirlo a otro tipo de dato.



# Crear un diccionario con eventos en una línea de tiempo
eventos = {'Evento 1': '2001', 'Evento 2': '2002', 'Evento 3': '2003'}

# Imprimir los eventos en el orden en que ocurrieron
for evento, año in eventos.items():
    print(f'{evento} ocurrió en {año}')

#Evento 1 ocurrió en 2001
#Evento 2 ocurrió en 2002
#Evento 3 ocurrió en 2003
    
print(eventos)
#{'Evento 1': '2001', 'Evento 2': '2002', 'Evento 3': '2003'}
print(eventos)
#{'Evento 1': '2001', 'Evento 2': '2002', 'Evento 3': '2003'}   
#no importa cuantas veces imprimamos, los eventos aparecen en orden de agregados. 



##################################### Métodos ##################################

#1. clear(): limpia los elementos del diccionario. 


#2. copy(): copia el arreglo superficialmente (shallow), los elementos que posean capas de profundidad (Ej: listas (profundidad 2), o listas dentro de listas (profundidad 3) solo serán apuntadores al diccionario original por lo tanto realizar cambios a estos datos en la copia también modificará a los datos el diccionario original.

    #Hacer deep copy (copiar el diccionario y también los datos con más capas de profundidad para que sean independientes por diccionario): 

import copy 
copiaDeep = copy.deepcopy(dic2)




#3. dict.fromkeys(seq, value ):   
    #seq: puede ser cualquier tipo de dato iterable: 
            #1. Listas.
            #2. Tuplas.
            #3. Strings.
            #4. Diccionarios.
            #5. Sets.
            #6. Archivos (se abre un archivo en python, se puede iterar a traves de sus líneas, txt, csv, json)
    #value: puede ser cualquier objeto de python, si no se especifica este valor por defecto se pondrá None.

# el método fromkeys(iterable,valorDefecto) agarra un iterable o secuencia de objetos que posea internamente SOLO objetos invariables (tuplas, numeros, strings o frozenSets ), si posee algo variable interno como una lista se dispará un error: 
#mi_diccionario = dict.fromkeys([[1,2], 'dos', 'tres'], 0) ERROR.
#Luego el valor por defecto puede ser cualquier objeto y se asgnará a todas las llaves del diccionario que estemos creando: 

llaves = ['uno',2,'tres','4']

nuevoDict = dict.fromkeys(llaves,'vaLoRrR')
print(nuevoDict)
#{'uno': 'vaLoRrR', 2: 'vaLoRrR', 'tres': 'vaLoRrR', '4': 'vaLoRrR'}



#4. get(X, valorSiNoEstáX):
    #sirve para buscar el valor de la llave en un diccionario, si no está esa llave devuelve por defecto None, si se define valorSiNoEstáX entonces al no encontrar el dato retronará valorSiNoEstáX:

#Ejemplo: 

print(nuevoDict.get('uno'))
#vaLoRrR
print(nuevoDict.get(5))
#None
print(nuevoDict.get(5,'no está en el diccionario')) #definiendo el segundo parámetro
#no está en el diccionario



#5. items(): devuelve llave:valor del diccionario: 
print(eventos.items())
#dict_items([('Evento 1', '2001'), ('Evento 2', '2002'), ('Evento 3', '2003')]), son referencias a los items de la lista para ser modificados(objeto vista)


#6. keys(): devuelve un objeto vista de todas las keys. 


#7. values(): devuekve un objeto vista de todos los valores de las llaves.



#8. pop(llave):  quita el elemento del diccionario y retorna su valor, si no lo encuentra dispara un error.
    #pop(llave,d): d = valor que podemos poner para que se imprima si no encuentra la llave. 
    


#9. popitem() (no toma parámetros): elimina y retorna el último item ingresado, retorna clave y valor, si el dict está vacio dispara un error. 



#10. setdefault(llave, d): este método va a buscar en el diccionario la llave que le pasemos y retronará su valor si lo encuentra. Si la llave no se encuentra en el diccionario la creará y le pondrá el valor que hayamos definido para d, si d no está definido entonces le pondrá None.



numeros = {1:'uno', 2:'dos', 3:'tres'}
print(numeros.setdefault(2)) #busco una llave que ya está y me retorna su valor.
#print() = dos

print(numeros.setdefault(4,'cuatro'))
#cuatro
print(numeros)
#{1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro'}   actualizó el dict





#11. update(otroIterable ordenado (llave,valor) o dict): si hay llaves repetidas en ambos diccionarios, el dccionario actualizando se quedará con las llaves del segundo diccionario y no con su propia llave repetida. 

dict1 = {1:'uno',2:'dos'}
dict2 = {'beso':'kiss', 'amor':'love'}

dict2.update(dict1)
print(dict2)
#{'beso': 'kiss', 'amor': 'love', 1: 'uno', 2: 'dos'}


#Pueden ser diferentes datos para extender pero que esten ordenados en PARES:

listaPair = [['casa','house'],['bebé','baby']] #con listas (se puede con tuplas)
dict1.update(listaPair)
print(dict1) 
#{1: 'uno', 2: 'dos', 'casa': 'house', 'bebé': 'baby'}




#################### iterar #############################
#Puedo iterar con un FOR EACH por cada valor, llave o item llamando al objeto vista del diccionario, cuando lo hago por item puedo asignar dos variables de iteración:

