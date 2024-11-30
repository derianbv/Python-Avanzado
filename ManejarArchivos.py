  '''
################################ Leer archivos #############################################
Podemos abrir archivos con la función archivo = open(path relativo, mode), mode puede ser puede ser los tipos de linux, read, write,  binario, esto va a abrir un objeti tipo File

Ejemplo: 
  archivo = open(path relativo, "r")
  Ahora podemos sacar metodos de este archivo Ej: archivo.name(), archivo.mode() 
  #   El archivo siempre hay que cerrarlo: 

  archivo.close() !!!!  Si no se cierra es como un fantasma que está gastando me moria y obstaculiza el buffer. = estorba. 

  Para evitar tener que cerrarlo explicitamente se usa With: 

  with open('archivo.txt', 'w') as archivo:
    archivo.write('Hola, mundo!')  # El archivo se cierra automáticamente.



    #################### Métodos #################################3

    1. string1 = archivo.read(n): sin la n guarda todo los qué esté en el archivo de txt en una string, con n avanzará un puntero hasta n y guardará todo lo que recorra 
    2. archivo.closed = true or false, muestra si está cerrado 
    3. archivo.readline() = retorna cada línea en un espcacio de un arreglo. 
    
    
  '''
