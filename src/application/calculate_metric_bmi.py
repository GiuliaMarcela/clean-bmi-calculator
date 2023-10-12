from src.domain.bmi_calculator import BMICalculator
from src.common.input_validator import InputValidator
from src.common.constants import (
    MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE,
    MAX_METRIC_HEIGHT,
    MAX_METRIC_WEIGHT
)


class MetricBMI(BMICalculator):
    """
    Classe concreta que calcula o Índice de Massa Corporal (IMC) 
    com base no peso em quilogramas (kg) e na altura em metros (m).

    A classe `MetricBMI` estende a classe abstrata `BMICalculator`, 
    fornecendo uma implementação concreta do método `calculate`
    para calcular o IMC com unidades métricas.
    """

    def __init__(self):
        self.input_validator = InputValidator()

    def calculate(self, weight, height):
        self.input_validator.validate_height(height)
        self.input_validator.validate_weight(weight)

        if weight > MAX_METRIC_WEIGHT:
            raise ValueError(MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE)
        if height > MAX_METRIC_HEIGHT:
            raise ValueError(MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE)

        return round((weight / (height**2)), 1)
