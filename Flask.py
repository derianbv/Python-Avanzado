#Es una libreria liviana para realizar páginas web. 

######################## Set up linux ####################### 
# 1. Instalación: pip install "Flask==2.2.2"
#es bueno instalar una versión fija de flask como la 2.2.2 para asegurar que una nueva versión no rompa la app. 

#2. creo el archivo server, en donde voy a inicializar la app como abajo, cuando yo la ejecute, dicho archivo se va a convertir en un
# server. Para ejecutarlo, en linux: flask --app server --debug run    (server es porque el archivo se llama server.py)


#Importación: 
from flask import Flask #Flas está en mayúscula porque es una clase
app = Flask(__name__) #Acá se utiliza el cosntructor de flask y se le pasa __name__, que es la variable especial de python que le ayuda 
# a identificar el contexto en dónde se está inicializando, si __name__ = __main__ es porque se ejecuta este archivo directamente. 

#app es una instancia de la clase Flask, en realidad representa la aplicación web. Cuando lo ejecuto !!! La página se vuelve un servidor 
#que va a empezar a responder peticiones de clientes (por medio de mensajes HTTP) 


@app.route('/') #Esto es un decorador de Python (@), "/" significa que es la ruta inicial de la aplicación. 
#Este decorador me dice, cuando el customer quiera entrar a la ruta / (es decir, envía un get a /), la respuesta que va a tener si es exitoso
# será la función debajo, en este caso hello_world(). Si falla la solicitud no se trigerea la función. 

'''
Los decoradores @ sirven ecencialmente para agregarles cosas a la función que está por debajo, en este caso @app.route() es una función 
que agarra como parámetro otra función, la que está abajo, y la cambia. Esto se hace para realizar cambios en funciones sin 
alterar su código base. 

Para nuestro ejemplo básico, @app.route() agarrá a la función def hello_world() y la utiliza como parámetro en alguna de todas las cosas
que hace internamente, lo que resulta es que en la ruta ('/') se va a ejecutar hello_world(). Si no se puciera el decorador @app.route()
antes, esta función solo sería una función más en el archivo. 
'''

def hello_world():
    return "<b> Hola mama </b>"
