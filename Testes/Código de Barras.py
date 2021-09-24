from barcode import EAN13
from barcode.writer import ImageWriter

numero = (input("Coloque um número (somente números!) com 12 digitos: "))
codigo = EAN13(numero, writer=ImageWriter())

codigo.save("novo_codigo1")
