import sys

# Методы для int
def bit_legth(digit=1):
    """
    Количество бит передаваемого целого числа        
    Keyword Arguments:
        digit {int} -- целое число на вход (default: {1})
    
    Returns:
        digit.bit_length() -- Количество бит переданного целого числа
    """
    try:
        return digit.bit_length()
    except AttributeError:
        raise

def to_bytes(digit=1):
    """
    Преобразование целого числа в bytes
    Keyword Arguments:
        digit {int} -- целое число на вход (default: {1})
    
    Returns:
        digit.to_bytes() -- представление в битах
    """
    try:
        return (abs(digit).to_bytes(4, byteorder=sys.byteorder)) # Берём абсолютное значение числа
    except (AttributeError, OverflowError):
        raise

def from_bytes(digit=1):
    """
    Преобразование в целое число из байтового представления digitfuncs.to_bytes()   
    Keyword Arguments:
        digit {int} -- целое число на вход (default: {1})
    
    Returns:
        int.from_bytes -- преобразование из байт в целое число
    """
    try:
        return int.from_bytes(digit, byteorder=sys.byteorder)
    except AttributeError:
        raise

# Методы для float
def as_integer_ratio(digit=1.25):
    """
    Представление числа с точкой в виде дроби    
    Keyword Arguments:
        digit {float} -- число с точкой на вход (default: {1.0})
    
    Returns:
        digit.as_integer_ratio() -- представление в виде дроби
    """

    try:
        return digit.as_integer_ratio()
    except (OverflowError, ValueError, AttributeError):
        raise

def hex(digit=1.0):
    """
    Преобразование числа с точкой в hex представление    
    Keyword Arguments:
        digit {float} -- число с точкой на вход (default: {1.0})
    
    Returns:
        digit.hex() -- hex представление числа с точкой
    """
    try:
        return digit.hex()
    except (AttributeError, OverflowError, ValueError):
        raise