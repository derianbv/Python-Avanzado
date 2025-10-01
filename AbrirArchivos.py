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

Se pueden concatenar: 

Ejemplo: 

with open ('archivo1.txt', "r") as arch1 
  with open ("archivo2.txt", "w") as arch2


WITH en Python - Resumen

¿Qué hace?
Ejecuta código de INICIO al entrar y de LIMPIEZA al salir, automáticamente.

Caso 1: Archivos (el más común)
with open("archivo.txt") as f:
    contenido = f.read()
# Se cierra solo, incluso si hay error

Caso 2: Spans/Telemetría
with tracer.start_as_current_span("operacion"):
    hacer_algo()
# Se finaliza solo y registra duración

Otros usos comunes:
- Locks (bloqueos de concurrencia)
- Conexiones a base de datos
- Transacciones
- Cualquier cosa que necesite setup/cleanup

¿Cómo funciona?
Cualquier objeto con métodos __enter__ y __exit__ puede usar 'with'

Regla simple:
with = "Haz algo al entrar, haz algo al salir, sin que yo lo olvide"

Beneficio principal:
Garantiza limpieza incluso si hay errores
(no más archivos abiertos o recursos sin liberar)


    #################### Métodos #################################3

    1. string1 = archivo.read(n): sin la n guarda todo los qué esté en el archivo de txt en una string, con n avanzará un puntero hasta n y guardará todo lo que recorra 
    2. archivo.closed = true or false, muestra si está cerrado 
    3. archivo.readline(n) = retorna cada línea en un espcacio de un arreglo, funciona igual que .read(n) pero el máximo es el final de le línea, límite que read() sí pasa, si uso más de un readline() entonces iré retornando uno a uno la info de cada línea
    4. archivo.seek(n) = mueve el puntoero al n+1 byte 

    #### Write #####
    
  tienes que estar me modo open(ruta, "w")
    archivo.write(texto) sobre escribe el archivo agregando "texto" en el archivo. Cada vez que se hace se sobre escribe
    para solo poder hacer appends se puede hacer con open(ruta, "a")
    
    
  '''
