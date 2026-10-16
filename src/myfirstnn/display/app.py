"""
This file manage the user interaction with the software via CLI
Authors: Alessio Parolini
"""

__all__ = ["AutoNNApp"]

from textual.app import App, ComposeResult

from .components import Titles, ModelConfig


class AutoNNApp(App):

    CSS_PATH = "styles/app.tcss"

    def compose(self) -> ComposeResult:

        yield Titles()

        yield ModelConfig()
