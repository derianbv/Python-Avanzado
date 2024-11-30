import pandas 

#Se utiliza para leer archivos y analizar información 

'''
Gurda los archivos en data frames o tablas, se puede pasar de un diccionario a un data frame con: dataframeeee = pandas.DataFrames(diccionario), las keys van a ser las columbas y 
los values ordenados en listas van a ser los rows, se asignan en orden entonces el valor de la la row 1 ... n debe tener sentido con las las otras columnas.


'''
######################### Métodos ###########################
'''
1. var = pandas.read_csv(archivo ) Leer CSV, retorna en var una tabla con los archivos del csv, similar para excel .real_xlsx()
2. buscar en las tablas: tabla.iloc[n,m]: (0 <= n,m)  n dice que busque en la fila n, y m en la columna m, ejemplo tabla.iloc(2,3) fila 2 columna 3

'''
