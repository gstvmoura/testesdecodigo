cigarros = int(input("Quantidade de cigarros fumados por dia: "))
anos = int(input("Quantidade de anos fumando: "))
ttcigarros = anos * 365 * cigarros
dias = ttcigarros / 144
print (f"Você viverá {dias:.1f} dias a menos!")
