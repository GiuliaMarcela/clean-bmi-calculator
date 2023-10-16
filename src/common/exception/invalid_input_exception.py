class InvalidInputException(Exception):
    """
    Exceção personalizada para representar erros de entrada inválida no cálculo do IMC.
    """

    def __init__(self, message):
        super().__init__(message)
