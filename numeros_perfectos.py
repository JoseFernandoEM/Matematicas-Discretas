numero = int(input("Digite un numero: "))
suma = 0

for i in range(1, numero):
    if(numero % i == 0):
        suma = suma + i

if(numero == suma):
    print("El numero es perfecto")
else:
    print("El numero no es perfecto")

for i in range(2, numero + 1):
    es_primo = True
    for j in range(2, i):
        if i % j == 0:
            es_primo = False
            break
        
    if es_primo:
        numero_perfecto = pow(2, i-1)*(pow(2, i)-1)
        if(numero_perfecto <= numero):
            print(numero_perfecto)