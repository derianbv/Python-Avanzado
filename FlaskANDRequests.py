#Es una libreria liviana para realizar páginas web. 

######################## Set up linux ####################### 
# 1. Instalación: pip install "Flask==2.2.2"
#es bueno instalar una versión fija de flask como la 2.2.2 para asegurar que una nueva versión no rompa la app. 

#2. creo el archivo server, en donde voy a inicializar la app como abajo, cuando yo la ejecute, dicho archivo se va a convertir en un
# server. Para ejecutarlo, en linux: flask --app server --debug run    (server es porque el archivo se llama server.py), esto hace que 
#esa pestaña del terminal corra el servidor 

################# YO SOY EL SERVIDORRRRRRR Y TENGO QUE APRENDER A MANEJAR CUSTOMERS ##########################

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

############################### GET POST #########################
def hello_world(): #Acá el método Get implicito, 
    return ("<b> Hola mama </b>", 200) #Acá le digo que le pase el codigo 200 si todo bn


@app.route('/index', methods=["GET", "POST"])
def index(): #Esta función responde a las solicitudes de los clientes cuando entren aquí
    if request.method == "GET" return jsonify(status="OK", method="GET"), 200 #Todo lo que se muestra en una pagina tiene que ser 
    #pedido por el usuario por medio de un método GET 
    if request.method == "POST" return jsonify(status="OK", method="POST"), 200
'''
En el html también hay que indicarle algo para POST y algo para GET:  

<!-- For POST -->
<form method="POST" action="/data">
    <!-- Your input fields here -->
    <input type="submit" value="Submit">
</form>
<!-- For GET -->
<a href="/data">Fetch data</a>

'''


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
        return {"message": "Something went wrong!"}, 404 #SIEMPRE RETORNAR ASÍ: return {str},int
    else:
        return {"message": "Server error!"}, 500




##################### ERRORES AND QUERIES #######################################
'''
Puedo setear como manejar los errores de mi código
Miremos este ejemplo: 
'''

from flask import request
#Es request de flask y no request de la libreria requests 
@app.route('/')
def search_response():
    query = request.args.get("q") #Esta linea agarra los parametros enviados por la url, en este caso busca SE USA PARA RECIBIR LOS DATOS QUE UN CUSTOMER PODRÍA ENVIAR, NO PARA ENVIAR NINGUNA
    #SOLICITUD AL SERVER, PORQUE EN ESTE CASO, YO SOY EL SERVER. 
    # a "q", ejemplo youtube.com/?q="hola", entonces query guardará a "hola" en un diccionario, si no hay devuelve none

    if not query: #es como decir if !query, o, si query es falso: 
        return {"error_message": "Input parameter missing"}, 422

    # fetch the resource from the database
    resource = fetch_from_database(query) # busca en la base de datos el valor de q, no es función de requests

    if resource:
        return {"message": resource}
    else:
        return {"error_message": "Resource not found"}, 404

'''

#Ahora puedo usar Linux para hacer gets a mi servidor y mostar esos mensajes: 

FALTA DE QUERY ------------------------

(Linux) curl -X GET -i http://localhost:5000

HTTP/1.1 422 UNPROCESSABLE ENTITY
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Thu, 12 Jan 2023 19:45:04 GMT
Content-Type: application/json
Content-Length: 44
Connection: close

{"error_message":"Input parameter missing"}
#devueve if not query ya que en la url debe haber un "q"= algo

------ QUERY NO EXISTENTE ----------------
    
curl -X GET -i http://localhost:5000/nonexistent_route

HTTP/1.1 404 NOT FOUND
Server: Werkzeug/2.2.3 Python/3.11.8
Date: Thu, 21 Mar 2024 15:18:55 GMT
Content-Type: application/json
Content-Length: 34
Connection: close

{"error_message":"API not found"}
# trigerea el else

---- QUERY EXITOSA ------------------------


(Linux) curl -X GET -i http://localhost:5000?q=Resource777

HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Thu, 12 Jan 2023 19:45:26 GMT
Content-Type: application/json
Content-Length: 26
Connection: close

{"message":"Resource777"}
#La respuesta de if resource


Los datos que se pasan por URL pueden ser dados porque alguien los escribio directamente en la url o el html tiene un forms con el método Get.

<form action="/buscar" method="get">
  <input type="text" name="q">
  <button type="submit">Buscar</button>
</form>


'''

######################## RENDERIZARRRRRRRRRRRRRRRRRRR ##########################################
from flask import Flask, render_template, request
app = Flask("My first Application")

@app.route('/sample')
def getSampleHtml():
    return render_template('sample.html') #en esta vista rederizo el html sample.html

@app.route('/user/<username>', methods=['GET'])
def greetUser(username): ########## a esta vista le estoy pasando al html la variable que agarro de la url (usarname)
    return render_template("result.html", username=username)

@app.route('/user', methods=['GET'])
def greetUserBasedOnReq():
    username = request.args.get("username")
    return render_template("result.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)




############### ################### FUNCIONES#######################################################
'''
1. Obtener datos que el clinte a subido con un POST 

<form method="POST" action="/login">
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit" value="Submit">
</form>
'''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username'] #pido lo que salga en el input del html 
    password = request.form['password'] #pido lo que puse en password 



'''
2. Redirigir: 
'''
from flask import redirect

@app.route('/admin')
def admin():
    return redirect('/login') #digamos que el usuario quizo entrar a admin pero su usuario esta incorrecto. 
#o puede ser redirigido a con una funcion que encuentra la url dandole el nomnre de la función: 
    return redirect(url_for('login')) #Url for busca a la función log in y la remplaza por su ruta 



############### Ejemplo de CRUD ########################


# Import necessary libraries from Flask
from flask import Flask, redirect, request, render_template, url_for
# Instantiate Flask application
app = Flask(__name__)
# Sample data representing transactions
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
# Read operation: Route to list all transactions
@app.route("/")
def get_transactions():
    # Render the transactions list template and pass the transactions data
    return render_template("transactions.html", transactions=transactions)
# Create operation: Route to display and process add transaction form
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == 'POST':
        # Extract form data to create a new transaction object
        transaction = {
            'id': len(transactions) + 1,         # Generate a new ID based on the current length of the transactions list
            'date': request.form['date'],        # Get the 'date' field value from the form
            'amount': float(request.form['amount']) # Get the 'amount' field value from the form and convert it to a float
        }
        # Append the new transaction to the transactions list
        transactions.append(transaction)
        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for("get_transactions"))
    # Render the form template to display the add transaction form if the request method is GET
    return render_template("form.html")
# Update operation: Route to display and process edit transaction form
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        # Extract the updated values from the form fields
        date = request.form['date']
        amount = float(request.form['amount'])
        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date       # Update the 'date' field of the transaction
                transaction['amount'] = amount   # Update the 'amount' field of the transaction
                break                            # Exit the loop once the transaction is found and updated
        # Redirect to the transactions list page after updating the transaction
        return redirect(url_for("get_transactions"))
    # Find the transaction with the matching ID and render the edit form if the request method is GET
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)
# Delete operation: Route to delete a transaction
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)  # Remove the transaction from the transactions list
            break                            # Exit the loop once the transaction is found and removed
    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for("get_transactions"))
# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)







############################# POST ####################################
