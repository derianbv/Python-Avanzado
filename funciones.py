############# FUNCIONES LAMBDA ##########################

#Son en pocas palabras funciones concisas, que no necesitan nombre: 
#sirve para entre otras cosas, hacer higher order functions (funciones que reciven y retornan otra función)

#Sintaxis:  (lambda parametros : cuerpo de la función)(parametrosQueQuieroPasar)

#Se pueden asignr a variables y funcionar como las funciones normales: 

primerLambda = lambda x : print(x + 2); 

primerLambda(4)

#para pasar parametros se pone un paréntesis después con el número: 

print((lambda var : var * 4 )(5))

# (lambda var : var * 4 )(5) == miFuncion(5)



############# FUNCIONES MAP ##########################
#Funcion map(): 
#retorna un objeto tipo map

#recibe dos parametros map(funciónParaAplicar,lista), la primera es una función que le voy a aplicar a CADA 
#elemento de la lista (que es el segundo parámetro), es decir que si pongo la función sumarUno a los cuatro numeros distintos de la lista 
# a cada uno le va a aplicar la función, es decir, le sumará uno: 

# Mi función: 
def sumarUno(x:int)->int: 
    return x + 1

#Mi lista: 
lista = [1,2,4,5]

#map: 

print(map(sumarUno,lista))
#esto imprime <map object at 0x000001AF7252A290> porque map retorna un objeto map, hay que pasarlo a lista: 
print(list(map(sumarUno,lista)))
# [2, 3, 5, 6]


#lAMBDA + MAP: ahorra tiempo
#misma función: 

print(list(map((lambda x: x+1), lista)))
#imprime: [2, 3, 5, 6]