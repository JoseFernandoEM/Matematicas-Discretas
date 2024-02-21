numero_uno = int(input("Digite el primer numero: "))
numero_dos = int(input("Digite el segundo numero: "))
suma_uno = 0
suma_dos = 0

for i in range(1, numero_uno):
    if(numero_uno % i == 0):
        suma_uno = suma_uno + i

for j in range(1, numero_dos):
    if(numero_dos % j == 0):
        suma_dos = suma_dos + j
        

if(numero_uno == suma_dos and numero_dos == suma_uno):
    print("Los numeros son amigos")
else:
    print("Los numeros no son amigos")