from operator import itemgetter, attrgetter
############# FUNCIONES LAMBDA ##########################

#Solo son de una linea
#Son en pocas palabras funciones concisas, que no necesitan nombre: 
#sirve para entre otras cosas, hacer higher order functions (funciones que reciven y retornan otra función)

#Sintaxis:  (lambda parametros : cuerpo de la función)(parametrosQueQuieroPasar)

#Se pueden asignr a variables y funcionar como las funciones normales: 

primerLambda = lambda x : print(x + 2); 

primerLambda(4)

#para pasar parametros se pone un paréntesis después con el número: 

print((lambda var : var * 4 )(5))

# (lambda var : var * 4 )(5) == miFuncion(5)






### High oder functions ### 
# reciben y retornan fucniones, ejemplo map() o filter() o reduce(s)
 
    



############# FUNCIONES MAP ##########################
#Funcion map(): 
#retorna un objeto tipo map

#recibe dos parametros map(funciónParaAplicar,lista), la primera es una función que le voy a aplicar a CADA 
#elemento de la lista (que es el segundo parámetro), es decir que si pongo la función sumarUno a los cuatro numeros distintos de la lista 
# a cada uno le va a aplicar la función, es decir, le sumará uno: 

# Mi función: 
def sumarUno(x:int)->int: 
    return x + 1

#Mi lista: 
lista = [1,2,4,5]

#map: 

print(map(sumarUno,lista))
#esto imprime <map object at 0x000001AF7252A290> porque map retorna un objeto map, hay que pasarlo a lista: 
print(list(map(sumarUno,lista)))
# [2, 3, 5, 6]


#lAMBDA + MAP: ahorra tiempo
#misma función: 

print(list(map((lambda x: x+1), lista)))
#imprime: [2, 3, 5, 6]




######################### Sorted() ########################################

#parámetros:
#sorted(iterable, key=callable, reverse=True)

#Key puede ir con: 
    # key = lambda
    # key = f(x)
    # key = len 

print("------------------")
lista = [1,2,3,4,5,6,7,8,9]

print(sorted(lista, key=lambda x: x%2))
#el resultado de los pares será 0 y por eso los ordenará primero: 
#print = [2, 4, 6, 8, 1, 3, 5, 7, 9]



#Se pueden ordenar dependiendo del valor de algún atributos de un objeto usando una lambda
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[1]))
#[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]




#También se puede accediedno a los atributos de una clase.

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

ListaDeEstudiantes  = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(ListaDeEstudiantes, key=lambda student: student.age) 

#esta lambda se puede utilizar de modo de getter, agarra el student y el retorno es student.age


#También se puede hacer con el módulo Operator y sus funciones itemgetter o attrgetter: 


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted(student_tuples, key=itemgetter(2))
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
#esto toma el objeto de indice 2 en el objeto y lo ordena. 

sorted(ListaDeEstudiantes, key=attrgetter('age'))
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
#este método toma el atributo age en el objeto student y lo ordena      



#También se pueden utilizar funciones mágicas, get item toma el value, get attribute es la llave.
students = ['dave', 'john', 'jane']
newgrades = {'john': 'F', 'jane':'A', 'dave': 'C'}
sorted(students, key=newgrades.__getitem__)
#['jane', 'dave', 'john']




######################### id() ########################################
#Me da un identificador del objeto en cuestion, que es su dirección en memoria. 
#puede dar una dirección de memoria diferente asiganada al objeto cada vez que se usa. 

#recibe todo tipo de objeto. 

#Uso: sirve para COMPARARA, se mira si dos objetos diferentes ocupan el mismo espacio de memoria.
#Ejemplo: 
a = [1,2,3] #a
b = a