not1=float(input("Nota 1:"))
not2=float(input("Nota 2:"))
not3=float(input("Nota 3:"))

mediaponderada=((not1)*0.25+(not2)*0.35+(not3)*0.4)
if(mediaponderada>=9.5 and mediaponderada<=20):
    print("Nota:",mediaponderada,"\nParabéns, aprovado!")
else:
    print("Nota:",mediaponderada, "\nEstuda mais, não aprovado!")
