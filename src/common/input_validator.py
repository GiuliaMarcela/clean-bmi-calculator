from typing import Union

from src.common.constants import (
    HEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE,
    INVALID_VALUE_MESSAGE,
    WEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE,
)


class InputValidator:
    """
    Classe utilitária para validar dados de peso e altura.

    Essa classe fornece métodos estáticos para verificar se os valores de peso e altura são válidos.
    Caso contrário, uma exceção 'ValueError' é lançada com uma mensagem descritiva.
    """

    @staticmethod
    def validate_weight(weight: Union[int, float]):
        """
        Valida o peso fornecido.

        Args:
            weight(int): O valor do peso a ser validado.

        Raises:
            ValueError: Se o peso for menor ou igual a zero
            ou se o valor fornecido não for do tipo `int`.
        """
        if not isinstance(weight, (int, float)):
            raise ValueError(INVALID_VALUE_MESSAGE)
        if weight <= 0:
            raise ValueError(WEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE)

    @staticmethod
    def validate_height(height: Union[int, float]):
        """
        Valida a altura fornecida.

        Args:
            height(float): O valor da altura a ser validado.

        Raises:
            ValueError: Se a altura for menor ou igual a zero ou
            se o valor informado diferente de `int` ou `float`.
        """
        if not isinstance(height, (int, float)):
            raise ValueError(INVALID_VALUE_MESSAGE)
        if height <= 0:
            raise ValueError(HEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE)
