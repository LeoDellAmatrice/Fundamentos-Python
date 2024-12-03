horas = int(input("digite uma quaantidade de horas: "))
minutos = int(input("minutos: "))

segundos = ((horas * 60) * 60) + (minutos * 60)
print(f"{horas} horas e {minutos} minutos equivalem a {segundos} segundos")
