###########3################### Strings ################################

#Las strings son un tipo de datos inmutables e iterables (subscriptibles)

str1 = 'Hola mamá'
#str[0] = 'g' saca error, es INMUTABLE

#El primer digito de atrás en adelante es = -len(str) 
len(str1) 
#9
print(str1[-9])
#H

# Ver más de esto en slicing.py 


######:  Scape sequences (\): -------------------------------------------------------------------------------------

#Carácteres especiales que modifican la manera en la que se muestran los strings
#Salto de línea: \n 
#Tab: \t 
#Usar "\" en el texto: \\ o agregar una r al lado del texto para cancelar estas scaped sequnces. Ej: r"Hola \ mundo" como raw

#Métodos ----------------------------------------------------------------------------------------------------------
#Strings have sequenced methods y metodos para texto"

#1.Format: agarra un string interpolation para poner .format(va1...varn) en sus place holder.

name = "John"
age = 50
print("My name is {} and I am {} years old.".format(name, age))
#"My name is John and I am 50 years old."

### String interpolation (f-string)--------------------------------------------------------------------------

name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

