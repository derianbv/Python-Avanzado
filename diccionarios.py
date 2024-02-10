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

#1. diccionario.clear(): limpia los elementos del diccionario. 


#2. diccionario.copy(): copia el arreglo superficialmente (shallow), los elementos que posean capas de profundidad (Ej: listas (profundidad 2), o listas dentro de listas (profundidad 3) solo serán apuntadores al diccionario original por lo tanto realizar cambios a estos datos en la copia también modificará a los datos el diccionario original.

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



#4. diccionario.get(X, valorSiNoEstáX):
    #sirve para buscar el valor de la llave en un diccionario, si no está esa llave devuelve por defecto None, si se define valorSiNoEstáX entonces al no encontrar el dato retronará valorSiNoEstáX:

#Ejemplo: 

print(nuevoDict.get('uno'))
#vaLoRrR
print(nuevoDict.get(5))
#None
print(nuevoDict.get(5,'no está en el diccionario')) #definiendo el segundo parámetro
#no está en el diccionario



#5. diccionario.items(): devuelve llave:valor del diccionario: en forma de una lista con las parejas de tuplas 
print(eventos.items())
#dict_items([('Evento 1', '2001'), ('Evento 2', '2002'), ('Evento 3', '2003')]), son referencias a los items de la lista para ser modificados(objeto vista)


#6. diccionario.keys(): devuelve un objeto vista de todas las keys. 


#7. diccionario.values(): devuekve un objeto vista de todos los valores de las llaves.



#8. .diccionario.pop(llave):  quita el elemento del diccionario y retorna su valor, si no lo encuentra dispara un error.
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

#1. por cada llave. 
    #lo hago iterando la LISTA que surge de llamar a las llaves del diccionario:
print(dict1.keys())
    #dict_keys([1, 2, 'casa', 'bebé'])


for llave in dict1.keys():
    print(llave)
    
#lo mismo por valor: 
for valor in dict1.values():
    print(valor)
    
 
print('---------------------')

for i in dict1: # sin llamar a item o llave o valor imprime el valor.
    print(i)
    
#en item se puede llamar a llave y valor:
for llave, valor in dict1.items():
    print(f'{llave} : {valor}')

#print():
#1 : uno
#2 : dos
#casa : house
# bebé : baby



#################### Switch como forma de diccionario ###################
#es más eficiente usar un diccionario como switch por la compejidad de las hash table.
def switch_func(value):
    switch = {
        0: "cero",
        1: "uno",
        2: "dos"
    }
    return switch.get(value, "Valor inválido")

print(switch_func(1))  # Imprime "uno"
print(switch_func(0))  # Imprime "cero"
print(switch_func(5))  # Imprime "Valor inválido"







############################### dict comprehension ######################################################
#Puedo crear diccionarios con la notación de dict comprehension:


#Sintaxis: diccionario = {valor( puede ir if) : llave(puede ir if Y ELSE) for valor, llave in otro iterable (if para agregar datos de otro iterable Y ELSE)}

amigos = {'camilo':20,'alba' : 21, 'Nayi':23}

edadEn5años = { valor : 'menor' if llave < 21 else 'mayor' for valor, llave in amigos.items() }
print(edadEn5años)
#{'camilo': 'menor', 'alba': 'mayor', 'Nayi': 'mayor'}



#Basado en un loop: 

loopDict = {i : 'None' for i in range(11) if i % 2 == 0}
print(loopDict)
#{0: 'None', 2: 'None', 4: 'None', 6: 'None', 8: 'None', 10: 'None'}









################################ ChainMap #####################################################################

#Me permite pegar diccionarios (cómo hacer varias veces update()), las llaves repetidas se quedarán en el diccionario final dependiendo del orden en el que le pasé los diccionarios como parámetro (diferente a update()).

#importarlo de la librerira collections

from collections import ChainMap

chainedMap = ChainMap(amigos, dict1, dict2)
print(chainedMap)
#ChainMap({'camilo': 20, 'alba': 21, 'Nayi': 23}, {1: 'uno', 2: 'dos', 'casa': 'house', 'bebé': 'baby'}, {'beso': 'kiss', 'amor': 'love', 1: 'uno', 2: 'dos'})

#RETORNA UN OBJETO DE TIPO ChainMap que tiene los siguientes métodos: 

        # maps: Es una lista ordenada de diccionarios. Esta lista es el único estado almacenado y puede ser modificada para cambiar qué mapeos se buscan1.

        # new_child(m=None, **kwargs): Retorna un nuevo ChainMap que contiene un nuevo mapa seguido de todos los mapas en la instancia actual. Si se especifica m, se convierte en el nuevo mapa al principio de la lista de mapeos; si no se especifica, se usa un diccionario vacío1.

        # parents: Es una propiedad que retorna un nuevo ChainMap que contiene todos los mapas en la instancia actual excepto el primero1.

        # keys(): Muestra todas las claves de todos los diccionarios en ChainMap2.

        # values(): Muestra los valores de todos los diccionarios en ChainMap2.

        # Además de estos, ChainMap soporta todos los métodos usuales de los diccionarios, como get(), items(), update(), etc1.
        
        
        
        
################################ DESEMPAQUETADO DE DICCIONARIOS ##########################################################

#Con un solo azterizco el diccionario retorna las llaves: 
mama = {'nombre':'Erika', 'parentezco':'madre', 'edad': 42}
print(*mama)
#nombre parentezco edad


#Verdadero desempaquetado (**): 
    #Básicamente es como el diccionario pero quitandole los {} 
    # entonces **mama = nombre='Erika', parentezco='madre', edad=42 HACIENDO ENFASIS EN LA LLAVE. (es como pasar la llave pero con información por dentro de la llave (value))
    
        #Que son argumento de palabra clave que sirven para pasarlos a funciones como parámetros en donde se nos pida poner LAS LLAVES (Solo las llaves), NO se pueden impirmir porque print() no acepta asignación. 

def saludarFamilia(nombre,parentezco,edad):
    print(f'{nombre} es el nombre de mi {parentezco} y tiene {edad} años')
    
saludarFamilia(**mama)
#Erika es el nombre de mi madre y tiene 42 años




