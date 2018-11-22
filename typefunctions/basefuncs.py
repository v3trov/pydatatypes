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
    if type(papram) in (int, float):
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
