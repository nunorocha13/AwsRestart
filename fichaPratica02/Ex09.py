num1=int(input("Insira um número inteiro:"))
num2=int(input("Insira um número inteiro:"))
num3=int(input("Insira  um número inteiro:"))

if (num1<num2)and(num1<num3):
    print("O número ", num1, " é o menor")
else:
    if (num2<num1)and(num2<num3):
        print("O número ", num2, " é o menor")
    else:
        print("O número ", num3, " é o menor")
#if(num1<num2 and num1<num3):
    #print(num1)