############################## TUPLAS #########################################

#Agrupación de datos INVARIABLE E INMUTABLE.
#basicamente con las listas y su manejo pero sin los métodos de las litas.
#Tiene de métodos de indentación positiva o negativa 

#Puede agrupar diferentes tipos de datos: 

miPrimeraTupla = (1, 'raul', False)

#posee indentación y slicing. 

print(miPrimeraTupla[:0:-1])
#(False, 'raul')



#Cambios en tuplo: a priorí no sería deseable realizar cambios en una tupla sin embargo si en verdad deseamos cambiar los datos de la tupla podemos transformala a una lista, realizar cambios y luego volverla a tupla: 

listaTupla = list(miPrimeraTupla)
listaTupla.append("CambiéLaTupla")
miPrimeraTupla = tuple(listaTupla)
print(miPrimeraTupla)
#(1, 'raul', False, 'CambiéLaTupla')



########################## desempaquetar ######################################
#SE PUEDE REALIZAR CON ASTERÍSCO:
tupla0 = (0,0,2)
listaDeTupla = [*tupla0]
print(listaDeTupla)
#[0, 0, 2]  puse la tupla dentro de [] y los desempaqueté, es decir los valores quedarón desagrupados de la tupla y dentro de la lista

# Crear una tupla
frutas = ("manzana", "banana", "cereza")

# Desempaquetar la tupla
verde, amarillo, rojo = frutas
#se puede asignar lo qué está por dentro de una tupla al mismo número de variables afuera igual que un una lista


tupla1=(1,2,3,4,5,6,7)
uno,dos, *resto = tupla1 #Al añadir asterísco le estoy diciendo a esa variable que tome el resto de cosas dentro de la tupla, se guardarán en una lista.
print(resto)
#[3, 4, 5, 6, 7]


############################### concatenación #######################################
#se puede concatenar tuplas.

tupla2 = ((1,2),'b')
tupla3 = tupla1 + tupla2
print(tupla3)




#repetición de tuplas: 
tuplaRep = (0,1)
print(tuplaRep*4)
#(0, 1, 0, 1, 0, 1, 0, 1)







######################### MÉTODOS ######################################
#1. .count(x): devuelve la cantidad de veces que x se encuentra en la tupla. 


#2. index(x) devuelve el indice en la tupla de x. 

#puedo aplicarle id(tupla), len(tupla), in tupla, etc.




