def convert_to_formatted_decimal(number: any):
    """
    Converte um número para o valor decimal formatado com duas casas decimais,
    se for um número inteiro.

    Esse método verifica se o número fornecido é um número inteiro. Se for, ele divide
    o número por 100 e retorna o resultado como um número de ponto flutuante
    com precisão de duas casas decimais.
    Se não for, ele retorna o número original sem alterações.

    Args:
        number(any): o número a ser convertido.

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
    if number.is_integer():
        decimal_value = number / 100
        return round(decimal_value, 2)
    return number
