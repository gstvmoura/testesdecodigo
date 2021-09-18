kmp = float(input("Informe a quantidade de KM que o carro percorreu: "))
ddu = int(input("Informe quantos dias usou o carro: "))
valor = ddu*60 + 0.15*kmp
print (f"O valor é de R$ {valor:.2f}")
