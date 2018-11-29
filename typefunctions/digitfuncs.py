import sys


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
    """Преобразование целого числа в bytes
    
    Keyword Arguments:
        digit {int} -- целое число на вход (default: {1})
    
    Returns:
        digit.to_bytes() -- представление в битах
    """
    try:
        return digit.to_bytes(4, byteorder=sys.byteorder)
    except (AttributeError, OverflowError):
        raise

def from_bytes(digit=1):
    """
    Преобразование в целое число из байтового представления digitfuncs.to_bytes()    
    Keyword Arguments:
        digit {int} -- целое число на вход (default: {1})
    
    Raises:
        AttributeError -- [description]
    
    Returns:
        [type] -- [description]
    """

    try:
        return int.from_bytes(digit, byteorder=sys.byteorder)
    except AttributeError:
        raise