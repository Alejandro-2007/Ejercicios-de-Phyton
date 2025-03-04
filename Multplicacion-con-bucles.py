numero = int(input("Introduce un numero: "))
print(f"Tabla de multiplicr del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}") 