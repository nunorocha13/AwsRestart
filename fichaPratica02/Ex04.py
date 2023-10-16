pos=int(input("Introduza a posição na corrida:"))
if(pos==8):
    print("Ganhou 1 ponto")
if(pos==7):
    print("Ganhou 2 pontos")
if(pos==6):
    print("Ganhou 3 pontos")
if(pos==5):
    print("Ganhou 4 pontos")
if(pos==4):
    print("Ganhou 5 pontos")
if(pos==3):
    print("Ganhou 6 pontos")
if(pos==2):
    print("Ganhou 8 pontos")
if(pos==1):
    print("Ganhou 10 pontos!")
if(pos>8):
    print("Não ganhou pontos")
#pode-se utilizar "elif" por uma questão de otimização
