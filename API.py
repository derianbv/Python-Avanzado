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

'''


