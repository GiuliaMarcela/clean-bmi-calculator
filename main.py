from src.adapters.cli.rich_adapter import RichAdapter
from src.application.calculator_factory import CalculatorFactory
from src.application.cli.cli import Cli


def main():
    """
    Função principal do programa.
    """
    start_application()


def start_application():
    """
    Cria instâncias dos adaptadores e fábricas necessários e inicia a CLI para executar a aplicação.

    Usage:
        Para executar a aplicação, chame esta função no seu script Python.
    """
    rich_adapter = RichAdapter()
    calculator_factory = CalculatorFactory()
    cli = Cli(adapter=rich_adapter, calculator_factory=calculator_factory)
    cli.execute()


if __name__ == "__main__":
    main()
