med=float(input("Salário médio:"))
if(med<=2000):
    print("Sem crédito!")
if(med>2000 and med<=4000):
    print("Crédito de:", med*0.2)
if(med>4000 and med<=6000):
    print("Crédito de:", med*0.3)
if(med>6000):
    print("Crédito de:", med*0.4)

