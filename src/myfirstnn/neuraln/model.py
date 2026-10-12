"""
model.py
Author: Alessio Parolini
Contains the data and the model for the initial tests
"""

import torch

# creating the input data for the test datas (example: temperature and humidity)

x_input = [[22.5, 45.0], [28.0, 60.5], [15.2, 30.0]]

X = torch.tensor(x_input, dtype=torch.float32)  # creating the tensor

# creating the expected output (canche of raining)

expected_out = [[0.2], [0.8], [0.1]]

Y = torch.tensor(expected_out, dtype=torch.float32)

print("INPUT TENSOR:\n")

print(X)

print(f"""
Shape: {X.shape}\n
Data type: {X.dtype}""")

print("OUTPUT TENSOR:\n")

print(Y)

print(f"""
Shape: {Y.shape}\n
Data type: {Y.dtype}""")
