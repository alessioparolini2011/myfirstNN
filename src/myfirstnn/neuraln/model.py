"""
model.py
Author: Alessio Parolini
Contains the data about the Neural Network Model
"""

__all__ = ["SimpleNN"]

import torch

from torch import nn


class SimpleNN(nn.Module):
    """
    This is the class to create the model to predict parables
    It has got 3 layers:
    1 -> 22 -> 1.
    Uses the ReLU
    """

    def __init__(self, name: str):

        super().__init__()

        self.relu = nn.ReLU()

        self.name = name

        self.layer1 = nn.Linear(in_features=1, out_features=22)  # first layer

        self.layer2 = nn.Linear(in_features=22, out_features=22)  # hidden layer

        self.layer3 = nn.Linear(in_features=22, out_features=1)  # final layer

        self.layers: list[nn.Linear] = [self.layer1, self.layer2, self.layer3]

    def __str__(self) -> str:

        return f"""Model name: {self.name}\n
                Layers: {len(self.layers)}\n
                Input: {getattr(self.layers[0], "in_features")}\n
                Output: {getattr(self.layers[-1], "out_features")}\n"""

    def forward(self, x: torch.Tensor) -> torch.Tensor:

        for layer in self.layers:

            x = layer(x)

            if layer is not self.layers[-1]:

                x = self.relu(x)

        return x
