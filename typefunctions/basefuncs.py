import random
import string

"""
Базовые функции
"""

def random_int():
    """
    Возвращает случаное целое число
    Returns:
        int -- случайное целое число
    """
    digit = random.randint(-10000, 10000)
    return digit

def random_float():
    """
    Возвращает случайное число с точкой
    Returns:
        float -- случайное число с точкой
    """
    digit = random.uniform(-10000.0, 10000.0)
    return digit

def random_string():
    """
    Возвращает случайную строку из n символов
    Returns:
        str -- случайна строка из n символов
    """
    n = 32
    s = "".join(random.choice(string.ascii_letters + string.digits + string.printable) for i in range(n))
    return s

def methods_list(param):
    """
    Возвращает список методов передаваемого параметра (экземпляра)
    Args:
        param: экземпляр класса (типа данных)

    Returns: список методов dir()

    """
    try:
        return dir(param)
    except:
        raise

def docstring(param):
    """
    Возвращает docstring передаваемого параметра (экземпляра)
    Args:
        param: экземпляр класса (типа данных)

    Returns: docstring __doc__

    """
    return param.__doc__

def hash(param):
    """
    Возвращает hash переданного экземпляра    
    Arguments:
        param -- переменная на вход
    
    Returns:
        param.__hash__() -- hash переданной переменной
    """
    try:
        return param.__hash__()
    except (AttributeError, ValueError, OverflowError):
        raise
