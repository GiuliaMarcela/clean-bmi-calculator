from abc import ABC, abstractmethod


class BMICalculator(ABC):
    """
    Classe abstrata que define um contrato para calcular o Índice de Massa Corporal (IMC).
    
    As classes concretas que implementam esta interface devem fornecer uma implementação 
    do método "calculate" que calcula o IMC com base no peso e altura fornecidos.
    """
    @abstractmethod
    def calculate(self, weight, height):
        """
        Este método abstrato deve ser implementado nas subclasses. 
        Ele recebe dois argumentos:

        args:
        ---
            weight(float): peso da pessoa em unidades de medida específicas
            height(float): altura da pessoa em unidades de medida específicas

        returns:
        ---
            O método deve retornar o valor calculado do IMC.
        """
