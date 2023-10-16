import sys

from src.application.calculator_factory import CalculatorFactory
from src.common.bmi_classifier import BMIClassifier
from src.common.constants import TYPE_CHOICES
from src.common.exception.invalid_input_exception import InvalidInputException
from src.common.numbers import convert_arguments_to_float
from src.interface.cli_interface import CLIInterface


class Cli:
    """
    Classe responsável por gerenciar a interface da linha de comando (CLI) para o cálculo do IMC.

    args:
        adapter (CLIInterface): Um adaptador para a interface de usuário da CLI.
        calculator_factory (CalculatorFactory): Uma fábrica para criar instâncias
        de calculadoras de IMC.

    attributes:
        __adapter (CLIInterface): O adaptador da interface do usuário.
        __calculator (CalculatorFactory): A fábrica de calculadoras de IMC.
    """

    def __init__(self, adapter: CLIInterface, calculator_factory: CalculatorFactory):
        self.__adapter = adapter
        self.__calculator = calculator_factory

    def execute(self):
        """
        Executa a interface da linha de comando (CLI) para calcular o IMC.

        Este método é responsável por controlar a interação com o usuário e realizar os cálculos
        do IMC com base nas entradas fornecidas.
        """
        try:
            type_of_calculation, weight_index, height_index = self.handle_command_line_args()
            str_weight = sys.argv[weight_index + 1]
            str_height = sys.argv[height_index + 1]

            weight, height = convert_arguments_to_float([str_weight, str_height])

            calculator = self.__calculator.create_calculator(type_of_calculation)
            result = calculator.calculate(weight, height)
            category = BMIClassifier(result).classify()

            self.__adapter.print_result(str(result), category)

            sys.exit(0)
        except ValueError as error:
            self.__adapter.print_error(
                f'{error}'
                f'\nEntrada: {" ".join(sys.argv[1:])}'
            )
            sys.exit(1)
        except InvalidInputException as error:
            self.__adapter.print_error(
                f'{error}'
                f'\nEntrada: {" ".join(sys.argv[1:])}'
            )
            sys.exit(1)

    def handle_command_line_args(self) -> tuple[str, int, int]:
        """
        Analisa e processa os argumentos da linha de comando para extrair informações relevantes.

        Esta função é responsável por analisar os argumentos passados via linha de comando
        e extrair informações necessárias para o cálculo do IMC. Ela retorna uma tupla contendo
        o tipo de cálculo (unidade), o índice do argumento de peso e o índice do argumento de altura
        na lista de argumentos da linha de comando.

        Returns:
            Tuple[str, int, int]: Uma tupla contendo as seguintes informações:
                - str: O tipo de cálculo, que pode ser 'metric' ou 'imperial' (padrão é 'metric').
                - int: O índice do argumento de peso na lista de argumentos da linha de comando.
                - int: O índice do argumento de altura na lista de argumentos da linha de comando.

        Raises:
            InvalidInputException: Se os argumentos da linha de comando
            estiverem ausentes ou incorretos, uma exceção `InvalidInputException` será lançada com
            uma mensagem de erro explicativa.
        """
        type_of_calculation = "metric"

        if len(sys.argv) == 1 or "--help" in sys.argv or "-h" in sys.argv:
            self.__adapter.print_help()
            sys.exit(0)

        if "calculate" not in sys.argv:
            self.__adapter.print_help()
            sys.exit(0)

        if "--unit" in sys.argv:
            unit_index = sys.argv.index("--unit")

            if (
                    unit_index + 1 >= len(sys.argv)
                    or sys.argv[unit_index + 1] not in TYPE_CHOICES
            ):
                raise InvalidInputException(
                    "Unidade de medida inválida. Use 'metric' ou 'imperial'")

            type_of_calculation = sys.argv[unit_index + 1]

        if "--weight" not in sys.argv or "--height" not in sys.argv:
            raise InvalidInputException("Entrada inválida. As opções --weight e --height são "
                                        "obrigatórias.")

        weight_index = sys.argv.index("--weight")
        height_index = sys.argv.index("--height")

        if weight_index + 1 >= len(sys.argv) or height_index + 1 >= len(sys.argv):
            raise InvalidInputException(
                "Entrada inválida. Valores para --weight e --height não foram especificados "
                "corretamente."
            )

        return type_of_calculation, weight_index, height_index
