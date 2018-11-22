def methods_list(digit):
    if type(digit) in (int, float):
        return dir(digit)
    else:
        raise TypeError("Некорректный тип. Должен быть int или float")


def docstring(digit):
    return digit.__doc__
