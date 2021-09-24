from barcode import EAN13

from barcode.writer import ImageWriter

number = '043280710847'
my_code = EAN13(number, writer=ImageWriter())

my_code.save("new_code1")
