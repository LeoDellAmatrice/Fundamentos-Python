dinheiro = input("você tem dinheiro para tomar sorvete? ")
sol = input("tem sol? ")
dia = input("qual o dia da semana?(seg, ter, qua, qui, sex, sab, dom) ")

if dinheiro == "sim" and sol == "sim" and (dia == "sab" or dia == "dom"):
    print("você pode tomar um sorvete!")
else:
    print("você não pode tomar um sorvete!")
