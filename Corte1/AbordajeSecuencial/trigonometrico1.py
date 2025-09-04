import math

radians=float(input("Ingrese un valor en radianes"))
proyeccion=math.sin(radians)
print ("Resultado:", proyeccion) #Para que muestre el seno de los radianes

#No existe alguna funcion para la cual calcule el seno en grados

Grados=radians*(180/math.pi)
print ("Conversion (Radianes a Grados):", Grados) #Para que muestre la conversion de grados a radianes
proyeccion2=math.sin(Grados)
print ("Resultado:", proyeccion2) #Para que muestre el seno de los grados