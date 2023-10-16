from src.common.numbers import convert_to_formatted_decimal


class TestNumbers:
    """
    Classe destinada a armazenar testes relacionados a classe utilitária numbers
    """

    def test_convert_to_formatted_decimal_integer(self):
        """
        Testa a função convert_to_formatted_decimal com um número inteiro.
        """
        assert convert_to_formatted_decimal(164) == 1.64

    def test_convert_to_formatted_decimal_original_value(self):
        """
        Testa a função convert_to_formatted_decimal com um número
        de ponto flutuante sem alterações.
        """
        assert convert_to_formatted_decimal(1.64) == 1.64

    def test_convert_to_formatted_decimal_negative_integer(self):
        """
        Testa a função convert_to_formatted_decimal com um número inteiro negativo.
        """
        assert convert_to_formatted_decimal(-42) == -0.42

    def test_convert_to_formatted_decimal_zero(self):
        """
        Testa a função convert_to_formatted_decimal com o número 0.
        """
        assert convert_to_formatted_decimal(0) == 0.00

    def test_convert_to_formatted_decimal_large_integer(self):
        """
        Testa a função convert_to_formatted_decimal com um número inteiro grande.
        """
        assert convert_to_formatted_decimal(1000000) == 10000.00

    def test_convert_to_formatted_decimal_large_float(self):
        """
        Testa a função convert_to_formatted_decimal com um número de ponto flutuante grande.
        """
        assert convert_to_formatted_decimal(1234567.89) == 1234567.89
