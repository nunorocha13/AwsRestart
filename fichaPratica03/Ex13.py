num_c=int(input("Quantos numéros quer colocar?:"))
contador=1
posicao=1

if(num_c)>=2:
    num_i=int(input("Introduza um numéro:"))
    while(contador<num_c):
        valorNovo=int(input("Insira numéro:"))

        if(valorNovo>num_i):

            posicao=posicao+1
        contador=contador+1

        num_i=valorNovo
    if(posicao==num_c):
        print("Numéros crescentes")
    else:
        print("Não são crescentes")
else:
    print("Mete dois valores por favor:")