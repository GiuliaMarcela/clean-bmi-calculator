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
        pass
