"""
main.py
Authors: Alessio Parolini
Manage and starts all the functions from other sub-packages. Imported in __main__.py for starts the package.
"""

from src.myfirstnn.learning import model_learning as ml

from src.myfirstnn.learning import random_io_tensors as rand_t

from src.myfirstnn.neuraln import ParableNN


def main() -> None:

    while True:

        model_name: str = input("Enter the model name: \n").strip()

        if model_name:

            break

    model = ParableNN(name=model_name)

    test_data = rand_t(n_input=500, n_range=2, y_function=lambda x: x**2)

    ml(model=model, data=test_data, epochs=1000)


if __name__ == "__main__":

    main()
