#Este ejercicio es para subir una decima en el corte
while True:
    num= input("Ingrese un numero")

    try:
        num = int(num)
    except ValueError:
        print("Por favor, ingrese un número válido.")

    for i in range(1,num+1):
        conta = 0
        for n in range(1, i+1):     
            residue = i%n
            if residue == 0:
                conta = conta + 1
    if conta == 2:
       print(f'{i} Si es numero un primo')
    else:
       print(f'{i} No es un numero primo')
