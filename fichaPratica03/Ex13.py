num_c=int(input("Quantos numéros quer colocar?:"))

contador=1

ant=int(input("Insira um numéro:"))

crescente=bool(True)

while(contador<num_c):
    num=int(input("Insira um numéro:"))
    contador+=1

    if(num<=ant):
        crescente=False

    ant=num

if(crescente):
    print("Crescente")
else:
    print("Não crecente")