# Rest API is a internet API 
################################### EPP #################################################
# Son dos piezas de software que hablan entre sí - como un traductor
'''
Son librerias que hay que descargar por pip 

# Hay dos actores: yo (cliente) y un servidor (endpoint), nos mensajeamos por medio de HTTP messages con json insertado
Los mensajes HTTP contienen: 

--------Response Start Line ------------------------ 
El CÓDIGO  de la request, lo qué le pido y para el server: 
el resultado de la request OK or FAIL  
-----------Responde Header------------------------ HEAD
Meta info 
---------Response body---------------------------- BODY 
El archivo o mercancía que estaba pidiendo

Get: le pido el HTML.index de la pagina.  
Server me responde con OK 200 y me manda el HTML en el body del mensaje http


 
############ Headers ##################
Los headers (diccionario o json) son como enviar una nota a un compañero del salon, no siempre le voy a decir lo mismo pero ahí le digo lo que el compañero 
quiere escuchar en cada solicitud por ejemplo, la paso una nota a una API que quiere saber cuales son mis tokens.


import requests

headers = {
    "Authorization": "Bearer token123",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "MiCliente/1.0"
}

Ejemplos de headers = 



Host	Especifica el dominio del servidor. Obligatorio en HTTP/1.1.
Content-Type	Indica el tipo de contenido enviado (como application/json o text/html).
User-Agent	Identifica al cliente que realiza la solicitud (por ejemplo, navegador, aplicación).
Accept	Indica los tipos de contenido que el cliente puede procesar (application/json, text/html).
Authorization	Proporciona credenciales para autenticación (como tokens o credenciales básicas).
Cache-Control	Controla el comportamiento de almacenamiento en caché. 
Content-Length	Indica la longitud del cuerpo de la solicitud en bytes.
Cookie	Envia cookies al servidor para mantener sesiones o preferencias del usuario.
Referer	Indica la URL desde la que se realizó la solicitud.
Connection	Controla si se reutiliza la conexión (por ejemplo, keep-alive).



################## Códigos #######################
-Prefijos indican la clase (1,2,3,4,5)
1XX: Todo está yendo bien. 
2XX: Exito 
3XX: refered
4XX: Failed
5XX: Server error. 


########################### REST - API ####################################

Partes de la dirección web: 

Scheme:  El protocolo por el que se van a enviar los archivos: http://
+
Internet adress or Base URL: www.gitlab.com
+
Route: /home

########## HTTP #### Métodos ###########:
1. Get: obtiene info de un server
2. Post: sube info al server 
3. Put: Actualiza ya info en el server 
4. Delete: borra info del server 



Libreria: import request ############# request ############# Library 

la manera de obtener un server es 
respuesta = request.get(youtube.com)
server.request.body -> relacionado con el body de un mensaje HTTP



################## Queries #############################

(http://youtube.com/)+(get)+(?)+(Name=Jose & ID=123
?: Es el inicio de la query
&: Separa parámetros 

ESTO ES CUANDO QUIERO PEDIRLE ALGO EN ESPECÍFICO A LA PÁGINA: 
Ejemplo: http://youtube/get

Ejemplo: 
url = "http//youtube.com"
VarQueQuiero = {'nombre':'jose','id':'4444'}
respuesta = request.get(url,params=VarQueQuiero)
Para post es igual: http//youtube.com/post

para obtener el html de un request get: 
  respuesta.text

Respuesta (respuesta = request.get(url)) tiene el toda la info del mensaje HTTP entre los mensajes con el server :), si no
le pongo params entonces se la pido toda !!!!!!!!!!!!!!!!!!!!
ejemplos: respues.status_code = 200 -> es un atributo, no un método
respuesta.header = metadatos de la pagina. 



Hay dos tipos de API: REST y SOAP


############################### HTTP REQUESTS #################################

Diferencia entre GET y POST

GET: SOLO DE VISITA

Se utiliza para recuperar datos del servidor.
Es una solicitud idempotente: no debe modificar datos en el servidor.
Se usa cuando el usuario simplemente quiere ver información (por ejemplo, listar cursos).


POST: ALTERAR AL SERVER, PASARLE COSAS O CAMBIAR LOGICA 

Se utiliza para enviar datos al servidor y realizar cambios, como actualizar o crear datos.
No es idempotente: cada vez que haces una solicitud POST, puede cambiar algo (en este caso, aumentar el contador un inscripciones).




######################## POST ##################################################################

En post se pueden incluir los siguientes parametros en la función: url, data (o json, son lo mismo solo que uno lo pasa a json), headers que son metadata, timeout que es si el server se 
demora, allow redirects, etc. 

response = requests.post(
    url="https://api.ejemplo.com/endpoint",
    data={"nombre": "Juan", "edad": 30}, #Info que le puedo pasar al server 
    headers={
        "Authorization": "Bearer token123",
        "Content-Type": "application/json"
    },
    timeout=10,
    allow_redirects=True
)


################################# GET ##################################################3
Sirve para pedirle cosas al server, entonces yo le paso unas cosas por parametros en la url como un diccionario,
luego el server recibe estas solicitudes y debe crear un return que le devuelva los datos que el cx busque si sus datos coinciden con confirmaciones 
en la lógica del backend. 

Cliente:----------------------------------------------------------------------------------

import requests #Sirve para hacer solicitudes a un server. 

url = "http://localhost:5000/productos"
params = {"categoria": "electronica"}

response = requests.get(url, params=params) #Aca le hago una solicitud de que el server trigueree la funcion GET que tenga seteada para esta url, sea cual sea.
#get() recibe como parametro params que es basicamente pasar datos por url que el server puede luego recuperar y verificar, si todo es exitoso con estos datos, me 
#deberia dar una respuesta.

print(response.json()) 

Servidor Flask:-----------------------------------------------------------------------------

@app.route('/productos', methods=['GET'])
def listar_productos():
    categoria = request.args.get("categoria") #sirve para agarrar lo que envió el cx en una solicitud, get es porque es un diccionario y estoy agarrando el valor de la 
    #llave categoria.
    productos = [
        {"id": 1, "nombre": "Televisor", "categoria": "electronica"},
        {"id": 2, "nombre": "Lavadora", "categoria": "electrodomesticos"}
    ]
    # Filtrar productos por categoría
    filtrados = [p for p in productos if p["categoria"] == categoria]
    return jsonify(filtrados)

'''

############################################ OBJETOS TIPO RESPONSE ######################################################:

#Un ejemplo de cómo podría ser esta clase implementada por dentro: 

class Response:
    def __init__(self):
        self.status_code = None  # Código de estado HTTP (por ejemplo, 200, 404, 500)
        self.headers = {}        # Diccionario con los encabezados de la respuesta
        self.text = ""           # Cuerpo de la respuesta como texto
        self.content = b""       # Cuerpo de la respuesta en bytes
        self.url = ""            # URL final después de redirecciones
        self.cookies = {}        # Cookies enviadas por el servidor
        self.history = []        # Lista de objetos Response de redirecciones
        self.reason = ""         # Razón del código de estado (por ejemplo, "OK" para 200)
        self.elapsed = None      # Tiempo de la solicitud como timedelta
        self.request = None      # Objeto Request asociado a esta respuesta

    def json(self):
        """
        Convierte el cuerpo de la respuesta a un objeto Python si es JSON válido.
        """
        import json
        try:
            return json.loads(self.text)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}")

    def raise_for_status(self):
        """
        Lanza una excepción si el código de estado HTTP indica un error.
        """
        if 400 <= self.status_code < 600:
            raise HTTPError(f"{self.status_code} Error: {self.reason} for URL: {self.url}")

    @property
    def ok(self):
        """
        Devuelve True si el código de estado HTTP es un éxito (200-299).
        """
        return 200 <= self.status_code < 300

    @property
    def is_redirect(self):
        """
        Devuelve True si la respuesta es una redirección.
        """
        return self.status_code in (301, 302, 303, 307, 308)

    @property
    def is_permanent_redirect(self):
        """
        Devuelve True si la respuesta es una redirección permanente.
        """
        return self.status_code in (301, 308)

    def __str__(self):
        """
        Representación en cadena para facilitar el debugging.
        """
        return f"<Response [{self.status_code}]>"

# Excepción personalizada para manejar errores HTTP
class HTTPError(Exception):
    pass




