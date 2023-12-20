############################## ASIGNACIÓN ########################################



#Es posible asignarle a una variable varias otras variables con el operador or: 
var1,var2,var3 = False, True, False 

tomoLaVerdadera = var1 or var2 or var3 
print(tomoLaVerdadera)
#True


#en este caso es posible notar que va a tomar el valor de la primera variable que sea verdadera o no nula.

num1,num2,num3,num4 = 0,0,-20,4
tomoNumTrue = num1 or num2 or num3
print(tomoNumTrue)
#-20

#En este caso, toma al cero como falso y números enteros(sin el 0) como verdaderos.

#tomará como falso o verdadero los siguientes valores: 
######## TRUTHY o FALSY ##############3
#1. Truthy (valores que toma como verdadero aparte del True): 
    #Cualquier cadena, lista, conjunto, diccionario, tupla o rango que no esté vacío.
    #Cualquier número distinto de cero.

#2. Falsy (Valores que toma como falso aparte del False): 
    #Cualquier cadena, lista, conjunto, diccionario, tupla o rango que esté vacío.
    #El 0. 
    #None


*uno, dos, tres, cuatro = [1,2,3,4,5,6,7]
print('________________________')
print(uno)