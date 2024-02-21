numero = int(input("Digite un numero: "))
suma = 0

for i in range(1, numero):
    if(numero % i == 0):
        suma = suma + i
        
if(numero == suma):
    print("El numero es perfecto")
else:
    print("El numero no es perfecto")
