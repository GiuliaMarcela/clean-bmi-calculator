from abc import ABC, abstractmethod


class CLIInterface(ABC):
    """
    Interface que define os métodos essenciais para uma implementação
    da interface de linha de comando (CLI).

    Esta interface define métodos abstratos que devem ser implementados
    por classes concretas para interagir com a interface de linha de comando,
    incluindo a impressão de ajuda, resultados e mensagens de erro.
    """

    @abstractmethod
    def print_help(self) -> None:
        """
        Método abstrato para imprimir mensagens de ajuda na interface de linha de comando.
        """

    @abstractmethod
    def print_result(self, value: str, category: str) -> None:
        """
        Método abstrato para imprimir o resultado do cálculo do IMC na interface
        de linha de comando, incluindo o valor e a categoria correspondente.

        args:
            value(str): resultado obtido do cálculo do IMC.
            category(str): categoria obtida através do resultado do cálculo do IMC.
        """

    @abstractmethod
    def print_error(self, message: str) -> None:
        """
        Método abstrato para imprimir mensagens de erro formatadas na interface
        de linha de comando em caso de problemas.

        args:
            message(str): mensagem para exibir para o usuário
        """
