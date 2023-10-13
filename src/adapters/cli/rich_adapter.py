import sys

from rich.align import Align
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from src.interface.cli_interface import CLIInterface


class RichAdapter(CLIInterface):
    """
    Adaptador que implementa a interface de linha de comando (CLI) usando a biblioteca Rich.

    Esta classe fornece métodos para imprimir mensagens formatadas e tabelas de resultados
    em uma interface de linha de comando usando a biblioteca Rich.
    """

    def __init__(self):
        self.console = Console()
        self.layout = Layout(name="main")

    def print_help(self) -> None:
        self._print_header()
        self._print_commands()
        self._print_options()

    def print_result(self, value, category) -> None:
        self._print_header()
        result_table = Table(expand=True)
        result_table.add_column("Valor")
        result_table.add_column("Categoria")
        result_table.add_row(value, category)
        self.console.print(Align.center(result_table))

    def print_error(self, message) -> None:
        self._print_header()
        panel_error = Panel.fit(
            title="Desculpa.. tivemos um problema! x(",
            title_align="center",
            renderable=Text(message, style="white"),
            padding=(1, 6, 1, 6),
        )
        self.console.print(Align.center(panel_error))
        sys.exit(1)

    def _print_header(self) -> None:
        title = Table.grid(padding=1)
        title.add_row(
            Text(
                """
█▀▀ ▄▀█ █░░ █▀▀ ░ █ █▀▄▀█ █▀▀
█▄▄ █▀█ █▄▄ █▄▄ ▄ █ █░▀░█ █▄▄
            """,
                justify="center",
            ),
        )
        title.add_row(
            Text(
                "Uso: python main.py calculate [--type type] --weight weight --height height",
                justify="center",
            )
        )
        title.add_row(
            Text(
                "Calcula com base no peso e altura do sistema de medida informado.",
                justify="center",
            )
        )
        title.add_row()

        self.console.print(title)

    def _print_commands(self) -> None:
        table_commands = Table.grid(padding=8)
        table_commands.add_row(
            "calculate",
            "Comando utilizado para realizar o cálculo do Índice de Massa Corporal (IMC)",
        )
        panel_commands = Panel.fit(
            title="Comandos",
            title_align="left",
            renderable=table_commands,
            padding=(1, 4, 1, 4),
        )
        self.console.print(Align.center(panel_commands))

    def _print_options(self) -> None:
        table_options = Table.grid(padding=1)
        table_options.add_row(
            "--help",
            "Exibe a mensagem de ajuda da calculadora",
        )
        table_options.add_row(
            "--type [green]<type>[/]",
            "Especifique o tipo de medida (metric ou imperial) (padrão: metric)",
        )
        table_options.add_row(
            "--weight [green]<weight>[/]",
            "Seu peso em unidades correspondentes ao sistema (obrigatório)",
        )
        table_options.add_row(
            "--height [green]<height>[/]",
            "Sua altura em unidades correspondentes ao sistema escolhido (obrigatório)",
        )
        panel_options = Panel.fit(
            title="Opções",
            title_align="left",
            renderable=table_options,
            padding=(1, 4, 1, 4),
        )
        self.console.print(Align.center(panel_options))
