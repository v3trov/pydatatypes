import random
from typefunctions import digitfuncs

i = random.randint(1, 10000)
f = random.uniform(1.0, 10000.0)

print("Методы int:", digitfuncs.methods_list(i), "\n")
print("Методы float", digitfuncs.methods_list(f), "\n")