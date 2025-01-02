################################## Condicionales ################################################

###################### is ###########################
#1. Verifica si dos variables apuntan al mismo espacion en memoria: 

x = 10
y = 10

print(x is y)  # True: Ambos usan la misma referencia en memoria, los numeros pequeños apuntan a un mismo lugar en memoria 

z = 1000
w = 1000

print(z is w)  # True o False, depende de la implementación
