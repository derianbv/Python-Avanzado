##################################### Dunder or magic methods ##############################################
##################### Double Underscore methods __f(x)__ ######################################
#son como los constructores de Java. 
import math

#Definen el comportamiento de las cuestiones básicas de simbología de una clase. 
#Ejemplo, los aritméticos: __add__ cambia el comportamiento del símbolo '+', __mul__ de '*', en general el comportamiento de las
#funciones de Math, ejemplo sum(vector1, vector2): 

#Ejemplo un espacio vectorial: 

class vectorEspacioVectorial: 

#cada vector va a constar de un x y ya 
    def __init__(self,x):
        self.x = x

        
#voy a definir la suma de vectores (+) como la potenciación de uno con el otro, el primero elevado al segundo. 
    def __add__(self, OtroVector):
        return (self.x ** OtroVector.x)
    

#__repr__ es similar al constructor toString de java, define la salida de la clase al usar print.  
    def __repr__(self) -> str:
        return f"{self.x}"
    



v1 = vectorEspacioVectorial(2) 
v2 = vectorEspacioVectorial(3)

v3 = v1 + v2
print(v3)
#print 8 porque 2^3 = 8 :). 


#se pueden también definir el comportamineto de otras cosas del lenguaje:
#__mul__ para la multiplicación, __pow__ potenciación, __and__ para el operador &, __eq__ para ==, __ne__ para != etc. 
 
#__init__ método constructor de un objeto. 

#Se puede 
