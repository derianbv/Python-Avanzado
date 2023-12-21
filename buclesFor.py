############ FOR LOOPS ############

#FOR EACH con valores ordenados por pares (como en los diccionarios): 
dict = {1:'uno',2:'dos',3:'tres'}

#puedo generar un for each elemento de un conjunto de datos (cada elemento consta de una pareja) que traiga ambos datos:

for llave, valor in dict.items():
    print(f'{llave},{valor}')

# 1,uno
# 2,dos
# 3,tres 

#FOR EACH DE AGRUPACIÓN DE TRES O MÁS DATOS.
 
#tengo una lista que agrupa tríos de datos (en tuplas, puede ser en listas igual): 
personas = [('Raul',24,'Madrir'), ('Luisa',14,'Florida'),('Melissa',22,'Zurich')]

#puedo llamar esos datos (3 o +) usando la misma cantidad de variables en el for (los nombres de las variables los escojo arbitrariamente): 

for nombre,edad,ubicacion in personas: #llamo a tres variables
    print(f'Hola me llamo {nombre}. Tengo {edad} años y vivo en {ubicacion}.')

# Hola me llamo Raul. Tengo 24 años y vivo en Madrir.
# Hola me llamo Luisa. Tengo 14 años y vivo en Florida.
# Hola me llamo Melissa. Tengo 22 años y vivo en Zurich.



