intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

numero = int(input("Digite um número inteiro positivo (ou um número negativo para sair): "))
while(numero>=0):
    if(numero>=0 and numero<=25):
        intervalo_0_25+=1
    if(numero >=26 and numero<=50):
        intervalo_26_50+=1
    if(numero>=51 and numero<=75):
        intervalo_51_75+=1
    if(numero>=76 and numero<=100):
        intervalo_76_100+=1

    numero = int(input("Digite um número inteiro positivo (ou um número negativo para sair): "))

print("Números no intervalo [0, 25]:", intervalo_0_25)
print("Números no intervalo [26, 50]:", intervalo_26_50)
print("Números no intervalo [51, 75]:", intervalo_51_75)
print("Números no intervalo [76, 100]:", intervalo_76_100)