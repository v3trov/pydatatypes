import random
from typefunctions import basefuncs

i = random.randint(1, 10000)            # Случайное целое число из диапазона (x, y)
f = random.uniform(1.0, 10000.0)        # Случайное число с плавающей точкой из диапазона (x, y)

print("Методы int:\n", basefuncs.methods_list(i), "\n")
print("Методы float:\n", basefuncs.methods_list(f), "\n")

print("Docstring int:\n", basefuncs.docstring(i), "\n")
print("Docstring float:\n", basefuncs.docstring(f), "\n")
