"""
tui.py
Authors: Alessio Parolini
This file contains the class for the app headers
"""

__all__ = ["Titles"]

from textual.app import ComposeResult

from textual.widgets import Label

from textual.containers import Container, Center


class Titles(Container):

    def compose(self) -> ComposeResult:

        with Center():

            yield Label(
                content=r"""
                         ░██               ░███    ░██ ░███    ░██
                         ░██               ░████   ░██ ░████   ░██
 ░██████   ░██    ░██ ░████████  ░███████  ░██░██  ░██ ░██░██  ░██
      ░██  ░██    ░██    ░██    ░██    ░██ ░██ ░██ ░██ ░██ ░██ ░██
 ░███████  ░██    ░██    ░██    ░██    ░██ ░██  ░██░██ ░██  ░██░██
░██   ░██  ░██   ░███    ░██    ░██    ░██ ░██   ░████ ░██   ░████
 ░█████░██  ░█████░██     ░████  ░███████  ░██    ░███ ░██    ░███ """,
                id="tui-title",
            )

            yield Label(
                content="""An incredible tool to create [bold #ffffff]your own AI model[/] from [bold #ffffff]random datas[/]!.\n
For now, it can learn only how to calculate squares (x^2) of numbers.\n
[bold]Try to edit number of inputs[/] to see how the precision changes!""",
                id="description",
            )
