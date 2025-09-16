#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde'] #Colores que se van a implementar (elementos de la lista)
#input()
print(my_lista) # Se esta imprimiendo lista
print(type(my_lista)) # devuelve el tipo de dato de la variable, en este caso list
print(my_lista[2]) #Esta accediendo al elemento del indice 2 en este caso el color amarillo
print("my_lista size: ", len(my_lista)) #Len utilizado para obtener el numero de elementos que contiene la lista   
print(my_lista[0:2]) #Se esta estableciendo el bloque o una sublista con los elementos 0 y 1 ya que es desde 0 hasta dos sin incluir el 2
print(my_lista[:2]) # Se esta tomando todos los elementos hasta el indice 2 sin incluirlo

my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista)

my_lista.insert(3, 'Negro') #Se le agrega el color negro en la posicion 3 a la lista que ya existe
print(my_lista)

my_lista.extend(['Marron', 'Gris'])   #Concatena los elementos de otra lista al final de la original
print(my_lista)

print(my_lista.index('Azul')) #Para encontrar la posicion en la que se encuentra un elemento dentro de la lista

#my_lista.remove('Magenta')
my_lista.remove('Marron') #Utilizado para eliminar un elemento de la lista, en este caso el marron
print(my_lista)

"my_lista.insert(8, 'Marron') #Insertar el color marron en la posicion 8 de la lista"
print(my_lista)

print(my_lista.pop()) #para quitar el ultimo elemento de la lista y devolver ese elemento
size = len(my_lista) #Para saber el numero de elementos que contiene la lista
print("size = ", size) #Imprime size
#print(my_lista.pop(size))

my_lista_3 = my_lista*3 #Crea una lista con los elementos repetidos 3 veces que continene la lista my_lista en el mismo orden 
print("my_lista_3: ", my_lista_3) #Imprime my_lista3

print("Sort:") #Imprime el texto "Sort"
print()
my_listaSort = my_lista.sort() #Ordena los elementos de la lista original ("my_lista") en su mismo lugar ya sea en orden ascendente o descendente
print(my_listaSort) #imprime my_listaSort

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1] #Crea la lista desde el elemento 10 hasta el 1
print("Ordering my_NumList: ") #muestra la nueva lista
my_NumList.sort() #ordena la lista my_numList (Por defecto es en orden ascendente)
print(my_NumList)
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista) #permite almacenar datos como una lista pero con la diferencia de que no se pueden modificar
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])#Imprime el elemento 0 de la tupla
print(my_tupla[2])#Imprime el elemento de la tupla en la posicion 2

#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)