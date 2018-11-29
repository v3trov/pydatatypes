import random
import string

"""
Базовые функции
"""

def random_int():
    digit = random.randint(-10000, 10000)
    return digit

def random_float():
    digit = random.uniform(-10000.0, 10000.0)
    return digit

def random_string():
    n = 32
    s = "".join(random.choice(string.ascii_letters + string.digits) for i in range(n))
    return s

def methods_list(param):
    """
    Возвращает список методов передаваемого параметра (экземпляра)
    Args:
        param: экземпляр класса (типа данных)

    Returns: список методов dir()

    """
    if type(param) in (int, float):
        return dir(param)
    else:
        raise TypeError("Некорректный тип. Должен быть int или float")


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
