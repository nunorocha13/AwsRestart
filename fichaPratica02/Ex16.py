valor=int(input("Digite o valor em euros (múltiplos de 5):"))
if(valor%5!=0):
    print("Não é múltiplo de 5!")
valorfinal=valor

notas_200=valor // 200
valor=valor%200

notas_100=valor // 100
valor=valor%100

notas_50=valor // 50
valor=valor%50

notas_20=valor // 20
valor=valor%20

notas_10=valor // 10
valor=valor%10

notas_5=valor // 5

print("Valor lido:",valorfinal)
print("Notas de 200:",notas_200)
print("Notas de 100:",notas_100)
print("Notas de 50:",notas_50)
print("Notas de 20:",notas_20)
print("Notas de 10:",notas_10)
print("Notas de 5:",notas_5)
