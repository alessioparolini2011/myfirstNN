"""
training.py
Authors: Alessio Parolini
Manage the training of the model
"""

import torch

from torch import nn

from torch import optim


def random_io_tensors(
    seed: int, n_input: int, n_range: int
) -> tuple[torch.Tensor, torch.Tensor]:

    torch.manual_seed(seed)

    x = (
        2 * n_range * torch.rand(n_input, 1) - n_range
    )  # creating the results and putting in a range from -2 to 2

    y = (
        x**2 + torch.randn(100, 1) * 0.2
    )  # creating a parable with X, but add a little error like is a real data

    return x, y


def model_learning(model: nn.Module, data: torch.Tensor, epoch: int = 300):

    pass
