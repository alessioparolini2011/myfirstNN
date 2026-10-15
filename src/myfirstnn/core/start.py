"""
main.py
Authors: Alessio Parolini
Manage and starts all the functions from other sub-packages. Imported in __main__.py for starts the package.
"""

__all__ = ["main"]

from myfirstnn.learning import model_learning as model_l

from myfirstnn.learning import random_io_tensors as rand_tens

from myfirstnn.neuraln import SimpleNN

from myfirstnn.display import onboard


def main() -> None:

    model_name = onboard()

    model = SimpleNN(name=model_name)

    test_data = rand_tens(n_input=1000, n_range=2, y_function=lambda x: x**2)

    model_l(model=model, data=test_data, epochs=10000)


if __name__ == "__main__":

    main()
