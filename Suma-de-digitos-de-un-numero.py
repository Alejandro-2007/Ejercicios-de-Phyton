numero = input("Introduce un numero: ")
suma_digitos = 0
for digito in numero:
    suma_digitos += int(digito)
print(f"La suma de los digitos del numero {numero} es: {suma_digitos}")  