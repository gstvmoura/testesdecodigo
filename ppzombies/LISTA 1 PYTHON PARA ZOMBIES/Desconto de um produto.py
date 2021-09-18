m = int(input("Escreva o valor do produto: "))
d = int(input("Escreva o valor do desconto %: "))
desconto = m * d / 100
valor = m - desconto
print(f"O Valor do produto com o desconto é: {valor:.2f}")
