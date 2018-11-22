import random


def methods_list(digit):
    if type(digit) in (int, float):
        return dir(digit)
    else:
        raise TypeError("Некорректный тип. Должен быть int или float")
