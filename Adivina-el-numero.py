numero_secreto = (1, 100)
intento = None
print("Adivina el numero (entre 1 y 100):")
while intento != numero_secreto:
    intento = int(input("Introduce tu intento: "))
    if intento < numero_secreto:
        print("Mas alto")
    elif intento > numero_secreto:
        print("Mas bajo")
    print(f"¡Felicidades! Has adivinado el numero {numero_secreto}.") 