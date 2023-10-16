sal=float(input("Insira salário:"))
if(sal<=15000):
    print("Imposto 20%:", sal*0.2)

if(sal>15000 and sal<=20000):
    print("Imposto 30%:", sal*0.3)

if(sal>20000 and sal<=25000):
    print("Imposto 35%:", sal*0.35)

if(sal>25000):
    print("Imposto 40%:", sal*0.4)

