import pandas 

#Se utiliza para leer archivos y analizar información 

'''
Gurda los archivos en data frames o tablas, se puede pasar de un diccionario a un data frame con: dataframeeee = pandas.DataFrames(diccionario), las keys van a ser las columbas y 
los values ordenados en listas van a ser los rows, se asignan en orden entonces el valor de la la row 1 ... n debe tener sentido con las las otras columnas.


'''
######################### Métodos ###########################
'''
1. var = pandas.read_csv(archivo ) Leer CSV, retorna en var una tabla con los archivos del csv, similar para excel .real_xlsx()


2. buscar en las tablas: tabla.iloc[n,m]: (0 <= n,m)  n dice que busque en la fila n, y m en la columna m, ejemplo tabla.iloc(2,3) fila 3 columna 4 (porque empieza en 0), también pueden ir
con el título de la columna, Ejemplo: tabla.iloc(2,"año_de_publicacion"): en la colum año de publicación vaya a la 3ra fila
  en estos números se pueden usar rangos, ejemplo: nuevaTabla = tabla.iloc[0:2,0:3] : quiero una tabla que vaya por las dos primeras filas y las tres primeras columnas, en las columnas
  también se pueden usar el nombre de las llaves tabla.iloc[0:2, 'título' : 'año ]




3. tabla.index = [a,b,c]: cambia el index de la tabla de 0,1,3 a a,b,c PERO ahora para entrar a sus datos se pasa de iloc[] -> loc[]
'''
