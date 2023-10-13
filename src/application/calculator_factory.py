from src.domain.bmi_calculator import Calculator
from src.domain.use_cases.calculate_imperial_bmi_use_case import CalculateImperialBMIUseCase
from src.domain.use_cases.calculate_metric_bmi_use_case import CalculateMetricBMIUseCase


class CalculatorFactory:
    """
    Classe de fábrica para criar instâncias de calculadoras.

    Esta classe fornece um método estático para criar instâncias de subclasses de calculadoras
    com base no tipo de cálculo especificado (seja 'métrico' ou 'imperial').
    """

    @staticmethod
    def create_calculator(type_of_calculation: str) -> Calculator:
        """
        Cria uma instância de uma calculadora com base no tipo de cálculo.

        args:
            type_of_calculation(str): O tipo de cálculo ('métrico' ou 'imperial').

        returns:
            Calculator: Uma instância de uma subclasse de Calculadora.

        raises:
            ValueError: Se um tipo de cálculo inválido for fornecido.
        """
        if type_of_calculation == "metric":
            return CalculateMetricBMIUseCase()

        if type_of_calculation == "imperial":
            return CalculateImperialBMIUseCase()

        raise ValueError(f'Tipo inválido: {type_of_calculation}')
