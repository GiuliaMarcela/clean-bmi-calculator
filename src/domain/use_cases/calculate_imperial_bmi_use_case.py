from src.common.constants import (
    MAX_IMPERIAL_WEIGHT,
    MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE,
    MAX_IMPERIAL_HEIGHT
)
from src.common.input_validator import InputValidator
from src.domain.bmi_calculator import Calculator


class CalculateImperialBMIUseCase(Calculator):
    """
    Classe concreta que calcula o Índice de Massa Corporal (IMC)
    com base no peso em libras e na altura em pés.

    A classe `CalculateImperialBMIUseCase` estende a classe abstrata `Calculator`,
    fornecendo uma implementação concreta do método `calculate`
    para calcular o IMC com unidades métricas.
    """

    def __init__(self):
        self.input_validator = InputValidator()

    def calculate(self, weight, height) -> float:
        self.input_validator.validate_height(height)
        self.input_validator.validate_weight(weight)

        if weight > MAX_IMPERIAL_WEIGHT:
            raise ValueError(MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE)
        if height > MAX_IMPERIAL_HEIGHT:
            raise ValueError(MEASUREMENTS_EXCEED_WORLD_RECORDS_MESSAGE)

        return round((weight / (height ** 2)) * 703, 1)
