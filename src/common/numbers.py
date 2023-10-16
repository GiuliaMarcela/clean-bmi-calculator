from numbers import Number
from typing import List

from src.common.constants import INVALID_VALUE_MESSAGE


def convert_to_formatted_decimal(value: Number):
    """
    Converte um número para o valor decimal formatado com duas casas decimais,
    se for um número inteiro.

    Esse método verifica se o número fornecido é um número inteiro. Se for, ele divide
    o número por 100 e retorna o resultado como um número de ponto flutuante
    com precisão de duas casas decimais.
    Se não for, ele retorna o número original sem alterações.

    Args:
        value(Number): o número a ser convertido.

    Returns:
        float: O número convertido com duas casas decimais, se for um número inteiro;
        caso contrário, ele retorna o número original

    Examples:
        >>> convert_to_formatted_decimal(180)
        1.80
        >>> convert_to_formatted_decimal(123.45)
        123.45
        >>> convert_to_formatted_decimal(1.64)
        1.64
    """
    if isinstance(value, int):
        decimal_value = value / 100
        return round(decimal_value, 2)
    return value


def convert_arguments_to_float(args: List[str]):
    """
    Esta função recebe uma lista de duas strings, representando peso e altura, e tenta convertê-las
    em valores float. Se a conversão for bem-sucedida, retorna uma tupla contendo o peso e a altura
    como floats.

    Args:
        args (List[str]): Uma lista de duas strings representando o peso e altura.

    Returns:
        Tuple[float, float]: Uma tupla contendo o peso e a altura como valores float.

    Raises: ValueError: Se a conversão de qualquer uma das strings para float falhar, uma exceção
    ValueError é lançada.

    Example:
        >>> convert_arguments_to_float(['70.5', '1.75'])
        >>> (70.5, 1.75)
    """
    try:
        weight = float(args[0])
        height = float(args[1])
        return weight, height
    except ValueError as exception:
        raise ValueError(INVALID_VALUE_MESSAGE) from exception
