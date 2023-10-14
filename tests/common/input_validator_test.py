import pytest

from src.common.constants import (
    WEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE,
    HEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE
)
from src.common.input_validator import InputValidator


class TestInputValidator:
    """
    Classe destinada aos cenários de teste da classe `InputValidator`
    """

    def test_validate_weight_valid_input(self):
        """
        O teste verifica se nenhum erro é retornado quando um
        peso válido é fornecido.
        """
        input_validator = InputValidator()
        valid_weight = 70
        input_validator.validate_weight(valid_weight)

    def test_validate_height_valid_input(self):
        """
        O teste verifica se nenhum erro é retornado quando uma
        altura válida é fornecida.
        """
        input_validator = InputValidator()
        height = 1.75
        input_validator.validate_height(height)

    def test_validate_weight_invalid_input(self):
        """
        O teste verifica se erro é lançado quando um valor negativo (inválido)
        para o peso é fornecido.
        """
        input_validator = InputValidator()
        weight = -5

        with pytest.raises(ValueError) as exception:
            input_validator.validate_weight(weight)
        assert str(exception.value) == WEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE

    def test_validate_height_invalid_input(self):
        """
        O teste verifica se erro é lançado quando um valor negativo (inválido)
        para a altura é fornecida.
        """
        input_validator = InputValidator()
        height = 0
        with pytest.raises(ValueError) as exception:
            input_validator.validate_height(height)
        assert str(exception.value) == HEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE
