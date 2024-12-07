#Es una libreria liviana para realizar páginas web. 

#Importación: 
from flask import Flask #Flas está en mayúscula porque es una clase
app = Flask(__name__) #Acá se utiliza el cosntructor de flask y se le pasa name 
@app.route('/')
def hello_world():
    return "<b> Hola mama </b>"
