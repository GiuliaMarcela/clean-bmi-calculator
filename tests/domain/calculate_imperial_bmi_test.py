import pytest

from src.common.constants import (
    MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE,
    INVALID_VALUE_MESSAGE,
    WEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE,
    HEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE
)
from src.domain.use_cases.calculate_imperial_bmi_use_case import CalculateImperialBMIUseCase


class TestCalculateImperialBMIUseCase:
    """
    Classe para testar o cenário de uso da classe `CalculateImperialBMIUseCase`.

    Esta classe é usada para realizar testes do cenário de uso da classe
    `CalculateImperialBMIUseCase`. Ela utiliza valores em libras
    para representar o peso e polegadas para representar a altura.
    """

    def test_should_return_correct_bmi_value(self):
        """
        Testa se o cálculo do Índice de Massa Corporal (IMC) retorna o valor correto.

        Este teste verifica se a função de cálculo do IMC produz o valor esperado
        com base em valores de peso e altura fornecidos.
        """
        metric = CalculateImperialBMIUseCase()
        assert metric.calculate(200, 70) == 28.7
        assert metric.calculate(150, 66) == 24.2

    def test_should_throw_error_if_zero_height_is_provided(self):
        """
        Testa se uma exceção é lançada quando zero é fornecido como altura.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando zero é fornecido como altura.
        """
        metric = CalculateImperialBMIUseCase()
        with pytest.raises(ValueError, match=HEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE):
            metric.calculate(180, 0)

    def test_should_throw_error_if_zero_weight_is_provided(self):
        """
        Testa se uma exceção é lançada quando zero é fornecido como peso.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando zero é fornecido como peso.
        """
        metric = CalculateImperialBMIUseCase()
        with pytest.raises(ValueError, match=WEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE):
            metric.calculate(0, 72)

    def test_should_throw_error_if_negative_weight_is_provided(self):
        """
        Testa se uma exceção é lançada quando valor negativo é fornecido como peso.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando valor negativo é fornecido como peso.
        """
        metric = CalculateImperialBMIUseCase()
        with pytest.raises(ValueError, match=WEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE):
            metric.calculate(-150, 66)

    def test_should_throw_error_if_negative_height_is_provided(self):
        """
        Testa se uma exceção é lançada quando valor negativo é fornecido como altura.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando valor negativo é fornecido como altura.
        """
        metric = CalculateImperialBMIUseCase()
        with pytest.raises(ValueError, match=HEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE):
            metric.calculate(150, -74)

    def test_should_throw_error_if_invalid_weight_is_provided(self):
        """
        Testa se uma exceção é lançada quando um peso inválido é fornecido.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando um peso inválido é fornecido.
        """
        metric = CalculateImperialBMIUseCase()
        with pytest.raises(ValueError, match=INVALID_VALUE_MESSAGE):
            metric.calculate("invalid", 70)

    def test_should_throw_error_if_invalid_height_is_provided(self):
        """
        Testa se uma exceção é lançada quando uma altura inválida é fornecida.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando uma altura inválida é fornecida.
        """
        metric = CalculateImperialBMIUseCase()
        with pytest.raises(ValueError, match=INVALID_VALUE_MESSAGE):
            metric.calculate(70, "invalid")

    def test_should_throw_error_if_large_weight_is_provided(self):
        """
        Testa se uma exceção é lançada quando um peso muito grande é fornecido.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando um peso maior que o limite permitido é fornecido.
        """
        metric = CalculateImperialBMIUseCase()
        with pytest.raises(ValueError, match=MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE):
            metric.calculate(1401, 96)

    def test_should_throw_error_if_large_height_is_provided(self):
        """
        Testa se uma exceção é lançada quando uma altura muito grande é fornecida.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando uma altura muito grande é fornecida.
        """
        metric = CalculateImperialBMIUseCase()
        with pytest.raises(ValueError, match=MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE):
            metric.calculate(150, 108)
