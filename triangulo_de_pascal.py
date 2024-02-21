import math

numero = int(input("Digite la cantidad de filas que desea imprimir: "))

for i in range(1, numero+1):
    for j in range(1, i+1):

        if j == 1:
            print(1, end=" ")
        elif j == i:
            print(1, end=" ")
        else:
            coeficiente_binomial = math.factorial(i-1) // (math.factorial(j-1) * math.factorial(i-j))
            print(coeficiente_binomial, end=" ")
    print()  
