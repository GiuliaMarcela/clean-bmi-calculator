class BMIClassifier:
    """
    Tem como sua principal função mapear um valor de IMC para uma categoria específica.

    Args:
        result (float): O valor do Índice de Massa Corporal (IMC) a ser categorizado.
    """

    def __init__(self, result: float):
        self.__result = result

    def classify(self):
        """
        Retorna a categoria do IMC com base no valor do IMC

        Returns:
            str: A categoria do IMC. Pode ser uma das seguintes categorias:
                - "Baixo peso"
                - "Peso normal"
                - "Sobrepeso"
                - "Obesidade grau 1"
                - "Obesidade grau 2"
                - "Obesidade grau 3"
                Ou "Categoria não encontrada" se o valor do IMC não se encaixar
                em nenhuma das categorias.
        """
        categories = {
            "Baixo peso": [0, 18.4],
            "Peso normal": [18.5, 24.9],
            "Sobrepeso": [25, 29.9],
            "Obesidade grau 1": [30, 34.9],
            "Obesidade grau 2": [35, 39.9],
            "Obesidade grau 3": [40, float("inf")],
        }

        for category, value in categories.items():
            if value[0] <= self.__result <= value[1]:
                return category

        return "Categoria não encontrada"
