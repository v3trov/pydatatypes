import random
from typefunctions import basefuncs
from typefunctions import digitfuncs

i = basefuncs.random_int()            # Случайное целое число из диапазона (x, y)
f = basefuncs.random_float()        # Случайное число с плавающей точкой из диапазона (x, y)
by = digitfuncs.to_bytes(random.randint(-10000, 10000))  # Представление рандомного целого числа в байтах
hexf = random.uniform(1.0, 10000.0).hex()

print("Методы int:\n", basefuncs.methods_list(i), "\n")
print("Методы float:\n", basefuncs.methods_list(f), "\n")

print("Docstring int:\n", basefuncs.docstring(i), "\n")
print("Docstring float:\n", basefuncs.docstring(f), "\n")

print("Длина в битах числа %s:" % i, digitfuncs.bit_legth(i))
print("Число %s в байтах это:" % abs(i), digitfuncs.to_bytes(i))
print("Байты %s -- это число %s" % (by, digitfuncs.from_bytes(by)))

print("Число %s по-другому можно записать как %s" % (f, digitfuncs.as_integer_ratio(f)))
print("Число %s в hex -- это %s" % (f, digitfuncs.hex(f)))

print("Hash чисел %s и %s -- %s; %s" % (i, f, basefuncs.hash(i), basefuncs.hash(f)))
