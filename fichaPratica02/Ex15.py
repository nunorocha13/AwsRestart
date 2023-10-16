num1=float(input("Introduza numéro:"))
num2=float(input("Introduza numéro:"))
num3=float(input("Introduza numéro:"))
ord=input("Ordem?:")

if(ord=="C" and num1<num2 and num1<num3 and num2<num3 ):
    print(num1,num2,num3)
elif (ord=="C" and num1 < num2 and num1 < num3 and num3 < num2):
    print(num1, num3, num2)
elif(ord=="C" and num2<num3 and num2<num1 and num1<num3 ):
    print(num2, num1, num3)
elif(ord=="C" and num2<num3 and num2<num1 and num3<num1 ):
    print(num2, num3, num1)
elif(ord=="C" and num3<num2 and num3<num1 and num2<num1 ):
    print(num3, num2, num1)
elif(ord=="C" and num3<num2 and num3<num1 and num1<num2 ):
    print(num3, num1, num2)

elif(ord=="D" and num1>num2 and num1>num3 and num2>num3 ):
    print(num1,num2,num3)
elif (ord=="D" and num1 > num2 and num1 > num3 and num3 > num2):
    print(num1, num3, num2)
elif(ord=="D" and num2>num3 and num2>num1 and num1>num3 ):
    print(num2, num1, num3)
elif(ord=="D" and num2>num3 and num2>num1 and num3>num1 ):
    print(num2, num3, num1)
elif(ord=="D" and num3>num2 and num3>num1 and num2>num1 ):
    print(num3, num2, num1)
elif(ord=="D" and num3>num2 and num3>num1 and num1>num2 ):
    print(num3, num1, num2)
elif(ord!="D"and ord!="C"):
    print("Não é possivel realizar o pedido!")

