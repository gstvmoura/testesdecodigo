s = int(input("Escreva o valor do salário: "))
a = int(input("Escreva o valor do aumento %: "))
aumento = s * a / 100
salario = s + aumento
print (f"O valor do aumento foi de: {aumento:.2f}")
print (f"O novo salário é: {salario:.2f}")
