sal=float(input("Insira o salário:"))

if(sal<=15000):
    imposto=sal*0.2
    print("Paga taxa de 20%:",imposto,"€")
else:
    imposto=sal*0.3
    print("Paga taxa de 30%", imposto,"€")
