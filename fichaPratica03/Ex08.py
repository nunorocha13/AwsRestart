contador=0
num=0
soma=0

while(num!=-1):
    num=int(input("Insere numéro:"))
    if(num!=-1):
        soma=soma+num
        contador=contador+1

print("Média", int(soma/contador))
