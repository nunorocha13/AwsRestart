hor=int(input("Intoduzir horas:"))
min=int(input("Introduzir minutos:"))

if(hor<=12):
    print(hor,":",min,"AM")

if(hor>12):
    print(hor-12,":",min,"PM")