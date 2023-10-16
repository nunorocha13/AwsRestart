

print("Introduza minutos da música 1:")
min1=int(input())
print("Introduza segundos da música 1:")
seg1=int(input())

print("Introduza minutos da música 2:")
min2=int(input())
print("Introduza segundos da música 2:")
seg2=int(input())

print("Introduza minutos da música 3:")
min3=int(input())
print("Introduza segundos da música 3:")
seg3=int(input())

print("Introduza minutos da música 4:")
min4=int(input())
print("Introduza segundos da música 4:")
seg4=int(input())

print("Introduza minutos da música 5:")
min5=int(input())
print("Introduza segundos da música 5:")
seg5=int(input())

#calcular total do album em segundos
segundosTotais=(min1+min2+min3+min4+min5)*60+(seg1+seg2+seg3+seg4+seg5)

#calcular horas totais (multiplicar segundos totais por 3600)
horas=int((segundosTotais/3600))

#calcular minutos (tiro tempo que ja esta em horas)
minutos=int((segundosTotais)/60-(horas*60))

#calcular os segundos (tiro o tempo em horas e segundos)
segundos=int((segundosTotais)-(horas*3600)-(minutos*60))

print(horas,"h", minutos,"m", segundos,"s")
#print(bla,"h",cla,"m",dla,"s")
