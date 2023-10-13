import sys

from src.application.calculator_factory import CalculatorFactory
from src.common.constants import TYPE_CHOICES
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
        type_of_calculation = "metric"

        if len(sys.argv) == 1 or "--help" in sys.argv or "-h" in sys.argv:
            self.__adapter.print_help()
            sys.exit(0)

        if "--type" in sys.argv:
            type_index = sys.argv.index("--type")

            if (
                    type_index + 1 >= len(sys.argv)
                    or sys.argv[type_index + 1] not in TYPE_CHOICES
            ):
                self.__adapter.print_error("Tipo inválido. Use 'metric' ou 'imperial'")
                sys.exit(1)

            type_of_calculation = sys.argv[type_index + 1]

        if "--weight" not in sys.argv or "--height" not in sys.argv:
            self.__adapter.print_error("As opções --weight e --height são obrigatórias.")
            sys.exit(1)
        else:
            weight_index = sys.argv.index("--weight")
            height_index = sys.argv.index("--height")

            if weight_index + 1 >= len(sys.argv) or height_index + 1 >= len(sys.argv):
                self.__adapter.print_error(
                    "Valores para --weight e --height não foram especificados corretamente."
                )
                sys.exit(1)

            try:
                _weight = float(sys.argv[weight_index + 1])
                _height = float(sys.argv[height_index + 1])

                calculator = self.__calculator.create_calculator(type_of_calculation)
                imc = calculator.calculate(_weight, _height)
                self.__adapter.print_result(str(imc), "Oi")
                sys.exit(0)
            except ValueError as error:
                message = str(error)
                if message == "Valores iguais a 0 ou negativos não são permitidos.":
                    self.__adapter.print_error(message)
                    sys.exit(1)

                self.__adapter.print_error(
                    f'Não foi possível converter o valor informado.'
                    f'\nEntrada: [red]{" ".join(sys.argv[1:])}[/red]'
                )
                sys.exit(1)
