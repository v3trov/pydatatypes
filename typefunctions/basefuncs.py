"""
Базовые функции для всех типов
"""

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
