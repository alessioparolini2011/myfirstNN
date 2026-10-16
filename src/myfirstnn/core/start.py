"""
main.py
Authors: Alessio Parolini
Manage and starts all the functions from other sub-packages. Imported in __main__.py for starts the package.
"""

__all__ = ["main"]

from myfirstnn.display import AutoNNApp


def main() -> None:

    app = AutoNNApp()

    app.run()


if __name__ == "__main__":

    main()
