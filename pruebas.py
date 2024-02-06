lista = [0,1,2,3,4,5,6,7,8,9]
print(lista[0:3])
#[0, 1, 2]

#En reversa ("-1" representa el último elemento de un arreglo): 
print(lista[::-1])
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(lista[::-2])
#[9, 7, 5, 3, 1]


#(-n puede reprensentar el numero de elemento contando de derecha a izquierda (reverted) empezando por el -1):
#Quiero imprimir del 9 a 6: 
print(lista[-2:-5:-1]) #le pedí que vaya en reversa con el -1 y que llegue hasta la posición -5 sin incluirlo. 
                                                             