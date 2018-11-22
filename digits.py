import random
from typefunctions import basefuncs

i = random.randint(1, 10000)
f = random.uniform(1.0, 10000.0)

print("Методы int:", basefuncs.methods_list(i), "\n")
print("Методы float", basefuncs.methods_list(f), "\n")

print("Docstring int:\n", basefuncs.docstring(i), "\n")
print("Docstring float:\n", basefuncs.docstring(f), "\n")
