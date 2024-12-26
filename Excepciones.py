############################################ Manejo de excepciones ############################################################3
#Es como decirle a python que si llega a haber un error de ejecución que lo pase, solo maneja errores de lógica y no de sintasis. 

def divir_por_cero(a,b): 
  return a/b #perfectamente escrito

divir_por_cero(1/0) 

'''
Me suelta el error:  

Traceback (most recent call last):
  File "/tmp/main.py", line 2, in <module>
    import user_code
  File "/tmp/user_code.py", line 4, in <module>
    divir_por_cero(1/0) 
                   ~^~
ZeroDivisionError: division by zero

'''
#Ahora, esperando algun error de ejecución lo puedo pasar con uno o varios except: 

def division(a,b): 
  try: 
    return a/b 
  except ZeroDivisionError: #Como hay error hace este bloque y no el de arriba, esta es una de los errores predeterminados de python 
    print('Eso está mal')
    return (ZeroDivisionError) 
  finally: #este es un codigo que le digo, hazte sí o si siempre con finally, así el except tenga un return 
    print('yo no me ecutaré porque el except me saca de la función')

division(1,0) #Así este mal por logica, el código va a hacer una excepsion, pueden ser más de una. 


print("El codigo finalizo sin errores que me detuvieran")

'''
Eso está mal
yo no me ecutaré porque el except me saca de la función
El codigo finalizo sin errores que me detuvieran

[Execution complete with exit code 0]
'''

################################ Raise y Clase Exception #######################################################################################


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero, this is imposible")  # El raise sirve para prever errores de logica creando mi codigo, acá le setee, si alguien trata de poner un cero que el programa raise un error de una 
    return a / b

