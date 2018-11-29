import random
from typefunctions import basefuncs
from typefunctions import digitfuncs

i = random.randint(1, 10000)            # Случайное целое число из диапазона (x, y)
f = random.uniform(1.0, 10000.0)        # Случайное число с плавающей точкой из диапазона (x, y)
by = digitfuncs.to_bytes(random.randint(1, 10000))  # Представление рандомного целого числа в байтах

# print("Методы int:\n", basefuncs.methods_list(i), "\n")
# print("Методы float:\n", basefuncs.methods_list(f), "\n")

# print("Docstring int:\n", basefuncs.docstring(i), "\n")
# print("Docstring float:\n", basefuncs.docstring(f), "\n")

print("Длина в битах числа %s:" % i, digitfuncs.bit_legth(i))
print("Число %s в битах это:" % i, digitfuncs.to_bytes(i))
print("Байты %s -- это число %s" % (by, digitfuncs.from_bytes(by)))