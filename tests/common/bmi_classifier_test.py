from src.common.bmi_classifier import BMIClassifier


class TestBMIClassifier:
    """
    Classe destinada aos cenários de teste da classe `BMIClassifier`
    """

    def test_classify_low_weight(self):
        """
        O teste verifica se a categoria "Baixo peso" é corretamente atribuída
        pela BMIClassifier com base em um valor de IMC fornecido.
        """
        category = BMIClassifier(15.0).classify()
        assert category == "Baixo peso"

    def test_classify_normal_weight(self):
        """
        O teste verifica se a categoria "Peso normal" é corretamente atribuída
        pela BMIClassifier com base em um valor de IMC fornecido.
        """
        category = BMIClassifier(22.0).classify()
        assert category == "Peso normal"

    def test_classify_overweight(self):
        """
        O teste verifica se a categoria "Sobrepeso" é corretamente atribuída
        pela BMIClassifier com base em um valor de IMC fornecido.
        """
        category = BMIClassifier(27.5).classify()
        assert category == "Sobrepeso"

    def test_classify_obesity_1(self):
        """
        O teste verifica se a categoria "Obesidade grau 1" é corretamente atribuída
        pela BMIClassifier com base em um valor de IMC fornecido.
        """
        category = BMIClassifier(32.5).classify()
        assert category == "Obesidade grau 1"

    def test_classify_obesity_2(self):
        """
        O teste verifica se a categoria "Obesidade grau 2" é corretamente atribuída
        pela BMIClassifier com base em um valor de IMC fornecido.
        """
        category = BMIClassifier(37.5).classify()
        assert category == "Obesidade grau 2"

    def test_classify_obesity_3(self):
        """
        O teste verifica se a categoria "Obesidade grau 3" é corretamente atribuída
        pela BMIClassifier com base em um valor de IMC fornecido.
        """
        category = BMIClassifier(45.0).classify()
        assert category == "Obesidade grau 3"

    def test_classify_unknown_category(self):
        """
        O teste verifica se a categoria "Categoria não encontrada" é corretamente
        atribuída pela BMIClassifier com base em um valor de IMC fornecido.
        """
        category = BMIClassifier(-50).classify()
        assert category == "Categoria não encontrada"
