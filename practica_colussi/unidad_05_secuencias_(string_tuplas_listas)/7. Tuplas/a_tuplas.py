# Una tupla es (elemento, elemeneto, elemento), formalmente tupla = elemento, elemento, elemento
# (elemento) no es una tupla, (elemento,) sí es una tupla.

# Iteración sobre tuplas:
def imprimeValoresTupla(tupla):
    for elemento in tupla:
        print(elemento)

# ImprimeValoresTupla((2, 4, 6))
# 2
# 4
# 6

# Version recursiva de la funcion ImprimeValoresTupla(tupla):
def imprimeValoresTuplaRec(tupla):
    if tupla != ():
        print(tupla[0]) # imprime el primer elemento de la tupla.
        imprimeValoresTuplaRec[tupla[1:]] # llama a la funcion en el resto de la tupla.

# ImprimeValoresTuplaRec((2, 4, 6))
# 2
# 4
# 6

# DIFERENCIAS DE LAS TUPLAS CON LAS LISTAS
# Las tuplas no poseen mecanismos de modificacion, ionserción ni eleiminación.
# Ademas las tuplas no son mutables, es decir, son inmutables por lo que sus
# valores no se pueden modificar una vez creada y tienen un tamaño fijo.

# ¿PARA QUE SIRVEN LAS TUPLAS?
# Supongamos que necesitamos almacenar la informacion: nombre, apellido, celular 
# de cierto conjunto de personas.
# Seria conveniente utilizar tuplas de la forma: (nombre, apellido, celular)
# Pues si usamos listas le podriamos insertar datos, modificando la estructura
# queremos que tenga cada persona.
# Pero las listas van a formar parte de la solucion, pues no sabemos de antemano
# cuantas personas tiene el conjunto, por ello necesitamos una lista para guardar
# la informacion de las personas.
# Por lo tanto, vamos a tener una lista de tuplas, de la forma:
# [(nombre1, apellido1, celular1), (nombre2, apellido2, celular2), ...]

# Lo que necesitamos, ante todo, es una funcion que dada una lista de personas
# permita agregar una nueva persona.
# Hay varias formas de hacer esto, por ejemplo:
def agregarPersona(listaDePersonas):
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    celular = input('Celular: ')
    listaDePersonas += [(nombre, apellido, celular)]

# Supongamos que nuestro conjunto de personas es un conjunto de alumnos.
# Generemos una funcion que tome una lista de alumnos y nos genere una
# salida amigable por pantalla:
def muestraListaAlumnos(listaDeAlumnos):
    for (nombre,apellido,celular) in listaDeAlumnos:
        print("El alumno", nombre, apellido, "tiene el celular:", celular)

# Conclusiones: las tuplas son mas rapidas que las listas en operaciones de acceso. (por su inmutabilidad)
# ademas por esta misma razon, ocupan menos memoria.
# Las tuplas se usan generalmente para representar conjuntos de elementos heterogeneos y para datos
# que no deben cambiar a lo largo de la ejecucion del programa.


