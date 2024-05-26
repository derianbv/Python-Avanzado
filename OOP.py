#############################################################3

class Gato: 
    
    #Constuctor 
    def __init__(self) -> None:
        pass
    
    #destructor, cuando un objeto muere triguerea esto 
    def __del__(self): 
        print("me electrocutaste pedrito")
        
nina = Gato()
nina = 4
# "me electrocutaste pedrito" en consola porque asigné otra cosa a la variable nina y el objeto se eliminó



############################# HERENCIA ########################################3

class Padre: 
    
    apellido = "rojas"
    
    #Constuctor 
    def __init__(self) -> None:
        pass
    
    def saludar(self):
        print("Hola soy Rojas")
    

#crear la herencia: 

class Hijo(Padre):
    
    def __init__(self) -> None:
        super().__init__()

#super() llama a su padre     
    def saludar(self):
        super().saludar()
        print("y soy el hijo")
        

     

derian = Hijo()

derian.saludar()

# Hola soy Rojas
# y soy el hijo