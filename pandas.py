import pandas 

#Se utiliza para leer archivos y analizar información 

''' 

################# Data Frames ####################################################################################################################################################
#Hay que instalarlo con pip. 


Gurda los archivos en data frames o tablas (bidimensionales) , se puede pasar de un diccionario a un data frame con: dataframeeee = pandas.DataFrames(diccionario), las keys van a ser las columbas y 
los values ordenados en listas van a ser los rows, se asignan en orden entonces el valor de la la row 1 ... n debe tener sentido con las las otras columnas.

### Acceso a cierta columna: 

    tabla['Name'] = similar al SELECT Name from tabla, puedo usarlo para varias tablas a la vez: df[['Department','Salary','ID']]

	Name	
0	Rose	
1	John	
2	Jane	
3	Mary	

Asignarla a una variable: 

columnaNueva = tabla[['Name']]: debe hacerse con doble parentesis porque si se hace con uno se devuelve es una Serie encambio. 
	


######################### Métodos ###########################

1. var = pandas.read_csv(archivo ) Leer CSV, retorna en var una tabla con los archivos del csv, similar para excel .real_xlsx()


2. buscar en las tablas: tabla.iloc[n,m]: (0 <= n,m)  n dice que busque en la fila n, y m en la columna m, ejemplo tabla.iloc(2,3) fila 3 columna 4 (porque empieza en 0), también pueden ir
con el título de la columna, Ejemplo: tabla.iloc(2,"año_de_publicacion"): en la colum año de publicación vaya a la 3ra fila
  en estos números se pueden usar rangos, ejemplo: nuevaTabla = tabla.iloc[0:2,0:3] : quiero una tabla que vaya por las dos primeras filas y las tres primeras columnas, en las columnas
  también se pueden usar el nombre de las llaves tabla.iloc[0:2, 'título' : 'año ] también se puede con las filas. 




3. tabla.index = [a,b,c]: cambia el index de la tabla de 0,1,3 a a,b,c PERO ahora para entrar a sus datos se pasa de iloc[] -> loc[]


4. tabla.unique(): exactamente igual que linux o sql, quita valores repetidos. 

5.tabla.head(): devuelve las primeras 5 columnas. 

###### Guardar #############

tabla.to_csv('nombre_archivo')






########################## Comparadores lógicos #####################

Esto me va a generar una columna de booleanos, si pasa es true y sino es false 
tabla[ 'año' > 2002 ] 




##################################################### Series #######################################################################################

Es la manera de Pandas de guardar Vectores unidimencionales para poder aplicarles funciones Pandas 
'''
