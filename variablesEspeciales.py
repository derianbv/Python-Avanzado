'''
A la hora de ejecutar un archivo en python el compilador realiza una seria de acciónes previo a la ejecución. 
Una de las cosas que realiza es la asignación a las variable especiales tales como __name__, dichas variables especiales ayudan a Python a 
entender el *contexto* del código: 

###### ___name___ #######
Esta variable ayuda a determinar si el archivo fue ejecutado directamente o exportado: 
  Inicialmente, si ejecuto cualquier archivo, esta variable especial se asgnará a main, es decir, __name__ = __main__, es pocas palabras, 
  estoy diciendole a python que estoy ejecutando lo que tengo dentro del archivo actual.

  Por otro lado, si importo otro archivo, __name__ va a ser igual al nombre de ese archivo.

  En lo práctico podemos realizar funciones que solo se realicen si ejecúto el archivo pero no cuando se exporta:

'''
if __name__ == '__main__': 
      # Este bloque de código solo se ejecuta si el archivo se corre directamente.
    # Por ejemplo, pruebas de código que no se ejecute al importar el archivo.
  print("Estoy corriendo miArchivo.py directamente")

#Pero si importo miArchivo desde otro archivo, no se imprimirá nada, porque __name__ no será "__main__", sino "miArchivo".
