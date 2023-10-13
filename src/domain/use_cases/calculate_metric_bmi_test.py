import pytest

from src.common.constants import (
    HEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE,
    INVALID_VALUE_MESSAGE,
    MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE,
    WEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE,
)
from src.domain.use_cases.calculate_metric_bmi_use_case import CalculateMetricBMIUseCase


class TestCalculateMetricBMIUseCase:
    """
    Classe destinada aos cenários de teste da classe `CalculateMetricBMIUseCase`
    """

    def test_should_return_correct_bmi_value(self):
        """
        Testa se o cálculo do Índice de Massa Corporal (IMC) retorna o valor correto.

        Este teste verifica se a função de cálculo do IMC produz o valor esperado
        com base em valores de peso e altura fornecidos.
        """
        metric = CalculateMetricBMIUseCase()
        assert metric.calculate(64, 1.64) == 23.8

    def test_should_throw_error_if_zero_height_is_provided(self):
        """
        Testa se uma exceção é lançada quando zero é fornecido como altura.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando zero é fornecido como altura.
        """
        metric = CalculateMetricBMIUseCase()
        with pytest.raises(ValueError, match=HEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE):
            metric.calculate(70, 0)

    def test_should_throw_error_if_zero_weight_is_provided(self):
        """
        Testa se uma exceção é lançada quando zero é fornecido como peso.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando zero é fornecido como peso.
        """
        metric = CalculateMetricBMIUseCase()
        with pytest.raises(ValueError, match=WEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE):
            metric.calculate(0, 1.64)

    def test_should_throw_error_if_negative_weight_is_provided(self):
        """
        Testa se uma exceção é lançada quando valor negativo é fornecido como peso.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando valor negativo é fornecido como peso.
        """
        metric = CalculateMetricBMIUseCase()
        with pytest.raises(ValueError, match=WEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE):
            metric.calculate(-2, 1.64)

    def test_should_throw_error_if_negative_height_is_provided(self):
        """
        Testa se uma exceção é lançada quando valor negativo é fornecido como altura.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando valor negativo é fornecido como altura.
        """
        metric = CalculateMetricBMIUseCase()
        with pytest.raises(ValueError, match=HEIGHT_LESS_THAN_OR_EQUAL_TO_ZERO_MESSAGE):
            metric.calculate(98, -1.64)

    def test_should_throw_error_if_invalid_weight_is_provided(self):
        """
        Testa se uma exceção é lançada quando um peso inválido é fornecido.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando um peso inválido é fornecido.
        """
        metric = CalculateMetricBMIUseCase()
        with pytest.raises(ValueError, match=INVALID_VALUE_MESSAGE):
            metric.calculate("a", 1.64)

    def test_should_throw_error_if_invalid_height_is_provided(self):
        """
        Testa se uma exceção é lançada quando uma altura inválida é fornecida.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando uma altura inválida é fornecida.
        """
        metric = CalculateMetricBMIUseCase()
        with pytest.raises(ValueError, match=INVALID_VALUE_MESSAGE):
            metric.calculate(70, "a")

    def test_should_throw_error_if_large_weight_is_provided(self):
        """
        Testa se uma exceção é lançada quando um peso muito grande é fornecido.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando um peso maior que o limite permitido é fornecido.
        """
        metric = CalculateMetricBMIUseCase()
        with pytest.raises(ValueError, match=MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE):
            metric.calculate(596, 1.64)

    def test_should_throw_error_if_large_height_is_provided(self):
        """
        Testa se uma exceção é lançada quando uma altura muito grande é fornecida.

        Este teste verifica se a função de validação lança uma exceção 'ValueError'
        quando uma altura muito grande é fornecida.
        """
        metric = CalculateMetricBMIUseCase()
        with pytest.raises(ValueError, match=MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE):
            metric.calculate(70, 2.51)
