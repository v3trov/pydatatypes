import random
from typefunctions import basefuncs
from typefunctions import digitfuncs

"""
Методы int:
'__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__',
'__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__',
'__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', 
'__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', 
'__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', 
'__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', 
'__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', 
'__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', 
'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 

'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'

Методы float:
'__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', 
'__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', 
'__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', 
'__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', 
'__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', 
'__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 

'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real'
"""


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
