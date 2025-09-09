#Este ejercicio es para subir una decima en el corte
while True:
    try:
        num = int(input("Digite el número que desea consultar: "))
        if num % 2 == 0:
            print(f"{num} es par")
        else:
            print(f"{num} es impar")
    
    except ValueError:
        print("Ingrese un número válido.")
    



