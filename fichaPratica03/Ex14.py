numero = int(input("Digite um número inteiro não negativo: "))

if(numero < 0):
    print("O número deve ser não negativo.")
else:
    resultado = 1
    i = 1

    while(i <= numero):
        resultado =resultado * i
        i += 1


    print(f"O fatorial de",numero, "é", resultado)