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

def hello_world(): #Acá el método Get implicito, 
    return ("<b> Hola mama </b>", 200) #Acá le digo que le pase el codigo 200 si todo bn


@app.route('/index', methods=["GET", "POST"])
def index(): #Esta función responde a las solicitudes de los clientes cuando entren aquí
    if request.method == "GET" return jsonify(status="OK", method="GET"), 200
    if request.method == "POST" return jsonify(status="OK", method="POST"), 200



@app.route("/")
def get_author():
    #res es un objeto tipo response que tendrá muchas funciones tales como response.status_code() para tener el codigo de respuesta o 
    #res.json() para parsear el objeto a un diccionario si la respuesta es un json.
    res = requests.get("https://openlibrary.org/search/authors.JSON?q=Michael Crichton") # Le estoy pidiendo al servidor que se contecte al
    #servidor de la URL y le haga una petición GET y retorna un objeto tipo Response 
    if res.status_code == 200: #si la respuesta es exitosa
        return {"message": res.json()}
    elif res.status_code == 404: #Si la respuesta no es exitosa
        return {"message": "Something went wrong!"}, 404
    else:
        return {"message": "Server error!"}, 500

####################################### Rutas dinámicas ###################################################

@app.route("/book/<string:isbn>") #con string:isbn lo paso a sttring
#<isbn> es un parámetro dinámico de la URL. Esto significa que si un usuario visita /book/12345, 
#el valor "12345" se asignará a la variable isbn dentro de la función.#
def get_author(isbn): #hay que pasarle la var dinámica
    res = requests.get(f"https://openlibrary.org/isbn/{escape(isbn)}.JSON") #Acá hace un llamado a la Api de open library con un GET

    '''
    escape(isbn) se utiliza para asegurarse de que la variable isbn no contenga caracteres que pudieran causar problemas de seguridad o interpretación. 
    Esto es especialmente importante si isbn proviene de una entrada de usuario o de una fuente externa no confiable.
    '''
    if res.status_code == 200:
        return {"message": res.json()} #este json probablemente tiene el libro
    elif res.status_code == 404:
        return {"message": "Something went wrong!"}, 404
    else:
        return {"message": "Server error!"}, 500




##################### ERRORES #######################################


