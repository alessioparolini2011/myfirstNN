"""
tui.py
Authors: Alessio Parolini
This file creates and manage the TUI using Textual
"""

from textual.app import App, ComposeResult

from textual.widgets import Button, Label

from textual.containers import Center


class AutoNN(App):

    CSS_PATH = "styles/app.tcss"

    def compose(self) -> ComposeResult:

        with Center():

            yield Label(
                content=r"""
               __        _   ___   __
  ____ ___  __/ /_____  / | / / | / /
 / __ `/ / / / __/ __ \/  |/ /  |/ /
/ /_/ / /_/ / /_/ /_/ / /|  / /|  /
\__,_/\__,_/\__/\____/_/ |_/_/ |_/
        """,
                id="tui-title",
            )

        yield Label(
            content="A incredible tool to create [bold]your own AI model[/] from [bold]your datas[/]!"
        )
