"""
This file manage the user interaction with the software via CLI
Authors: Alessio Parolini
"""

__all__ = ["onboard"]

from rich.console import Console

console = Console()


def onboard() -> str:
    """
    Print on screen title and ask for the model name and others info for the model training
    :return: the model name
    """

    console.print("[orange]Welcome to [b]autoNN[b/]![/]\n", justify="center")

    model_name = console.input("Enter the model name: ")



    return model_name
