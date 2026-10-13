"""
training.py
Authors: Alessio Parolini
Manage the training of the model
"""

__all__ = ["random_io_tensors", "model_learning"]

import torch

from torch import nn

from torch import optim

from src.myfirstnn.neuraln import ParableNN

from typing import Callable


def random_io_tensors(n_input: int, n_range: int, y_function : Callable[[torch.Tensor], torch.Tensor], seed: int = 28) -> tuple[torch.Tensor, torch.Tensor]:

    """
    Generates random numbers for the tests. They will be always the sames, but's better for training.
    :param n_input: the number of the random generated numbers
    :param n_range: the range (before and after zero) where the number are created in
    :param y_function: the function (even a lambda) to calculate the expected output
    :param seed: the manual seed, to generate every time the same numbers.
    :return: 2 torch.Tensors with X and Y
    """

    torch.manual_seed(seed)  # setting the manual seed

    x = (2 * n_range * torch.rand(n_input, 1) - n_range)  # creating the results and putting in a range from -2 to 2

    y = y_function(x) + torch.randn(n_input, 1) * 0.1   # calculating the Y starting from X, using the given function and add a Gaussian noise

    return x, y


def model_learning(model: ParableNN, data: tuple[torch.Tensor, torch.Tensor], epochs: int = 300):

    error = nn.MSELoss()  # initializing the error function

    learning_optimizer = optim.Adam(model.parameters(), lr=0.02)  #initializing the optimizer (ADAM)

    final_loss = 0

    print(f"Starting the training for {getattr(model, "name")}. It will last exactly {epochs} epochs. ")

    for epoch in range(epochs):

        learning_optimizer.zero_grad() # resets the model gradients

        expected_out = model(data[0]) # get the model output

        loss = error(expected_out, data[1])  # calculate the error from the expected output

        loss.backward() # update the gradients

        learning_optimizer.step() # the optimizer updates the weights

        if epoch % 10 == 0:  # every 10 epochs gives a report

            print(f"Epoch: {epoch + 1} on {epochs} - Actual loss: {loss.item():.6f}")

        final_loss = loss.item() # updating every epoch for logic causes (if the loop doesn't start) the assignment doesn't happen and there's no error



    print(f"""Training is done.\n
            Final loss: {final_loss:.6f}""")










