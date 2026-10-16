"""
tui.py
Authors: Alessio Parolini
This file contains the class for the app headers
"""

__all__ = ["Titles"]

from textual.app import ComposeResult

from textual.widgets import Label

from textual.containers import Center


class Titles(Center):

    def compose(self) -> ComposeResult:

        yield Label(
            content=r"""
                         ░██               ░███    ░██ ░███    ░██ 
                         ░██               ░████   ░██ ░████   ░██ 
 ░██████   ░██    ░██ ░████████  ░███████  ░██░██  ░██ ░██░██  ░██ 
      ░██  ░██    ░██    ░██    ░██    ░██ ░██ ░██ ░██ ░██ ░██ ░██ 
 ░███████  ░██    ░██    ░██    ░██    ░██ ░██  ░██░██ ░██  ░██░██ 
░██   ░██  ░██   ░███    ░██    ░██    ░██ ░██   ░████ ░██   ░████
 ░█████░██  ░█████░██     ░████  ░███████  ░██    ░███ ░██    ░███
 """,
            id="tui-title",
        )

        yield Label(
            content="""An incredible tool to create [bold #ffffff]your own AI model[/] from [bold #ffffff]your datas[/]!""",
            id="description",
        )
