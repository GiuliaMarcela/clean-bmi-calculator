from src.common.constants import (
    MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE,
    MAX_METRIC_HEIGHT,
    MAX_METRIC_WEIGHT,
)
from src.common.input_validator import InputValidator
from src.common.numbers import convert_to_formatted_decimal
from src.domain.bmi_calculator import Calculator


class CalculateMetricBMIUseCase(Calculator):
    """
    Classe concreta que calcula o Índice de Massa Corporal (IMC)
    com base no peso em quilogramas (kg) e na altura em metros (m).

    A classe `CalculateMetricBMIUseCase` estende a classe abstrata `Calculator`,
    fornecendo uma implementação concreta do método `calculate`
    para calcular o IMC com unidades métricas.
    """

    def __init__(self):
        self.input_validator = InputValidator()

    def calculate(self, weight, height) -> float:
        self.input_validator.validate_height(height)
        self.input_validator.validate_weight(weight)

        height_in_decimal_value = convert_to_formatted_decimal(
            height
        )

        if weight > MAX_METRIC_WEIGHT:
            raise ValueError(MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE)
        if height_in_decimal_value > MAX_METRIC_HEIGHT:
            raise ValueError(MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE)

        return round((weight / (height_in_decimal_value ** 2)), 1)
