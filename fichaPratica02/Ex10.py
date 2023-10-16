num1=float(input("Introduzir numéro:"))
num2=float(input("Introduzir numéro:"))
ope=input("Operação (/*-+):")
if(ope=="+"):
    print("Soma:",num1+num2)
if(ope == "-"):
    print("Subtração:",num1-num2)
if(ope == "*"):
     print("Multiplicação:",num1*num2)
if(ope == "/"):
    print("Divisão:",num1/num2)
if(ope!= "+" and ope!="*" and ope!="-" and ope!="/"):
    print("ERRO!")
#posso utilizar elif e depois terminar com else