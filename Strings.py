############################## Strings ################################

#Las strings son un tipo de datos inmutables e iterables (subscriptibles)

str1 = 'Hola mamá'
#str[0] = 'g' saca error, es INMUTABLE

#El primer digito de atrás en adelante es = -len(str) 
len(str1) 
#9
print(str1[-9])
#H

# Ver más de esto en slicing.py 

######: Formatear  -------------------------------------------------------------------------------------

MongoClient('mongodb://%s:%s@127.0.0.1' % ('mongouser', 'password')) 
#Acá tenemos un string que tiene dos wild cards que cambiamos con %,
#eso es quivalente a: 

MongoClient('mongodb://{}:{}@127.0.0.1'.format('mongouser', 'password'))

######:  Scape sequences (\): -------------------------------------------------------------------------------------

#Carácteres especiales que modifican la manera en la que se muestran los strings
#Salto de línea: \n 
#Tab: \t 
#Usar "\" en el texto: \\ o agregar una r al lado del texto para cancelar estas scaped sequnces. Ej: r"Hola \ mundo" como raw

#Métodos ----------------------------------------------------------------------------------------------------------
#Strings have sequenced methods y metodos para texto": ejemplo: .find(),.replace(),.split(): divide todo en un arreglo. 
#!!!!!!11 cuando le aplico un método a una string me resulta en una string diferente

#1.Format: agarra un string interpolation para poner .format(va1...varn) en sus place holder.

name = "John"
age = 50
print("My name is {} and I am {} years old.".format(name, age))
#"My name is John and I am 50 years old."

#2. str.upper(): todo a mayus

### String interpolation (f-string)--------------------------------------------------------------------------

name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

########################### Regular expresion------------------------------------------------------------------------
#Modulos de python "import r" que mejora las opciones de búsqueda en textos: 
###:  ejemplo: \d detecta un numero del 0-9

import re

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890" #el texto donde voy a buscar
match = re.search(pattern, text) # el patron que voy a buscar

#if match devuelve objeto match. sino, devuelve none
if match:
    print("Phone number found:", match.group())
else:
    print("No match")

############################################ Join ###########################################################

lista = ["1","2","3"]
print("".join(lista))
#OUT: 123


lista = ["1","2","3"]
print("--------".join(lista))
#1--------2--------3

Básicamente, pega elementos de una lista (tienen que ser strings estos elementos sí o sí) y los separa por lo que haya en "".join
