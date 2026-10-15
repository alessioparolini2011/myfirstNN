"""
form.py
Authors: Alessio Parolini
This file contains the class to make the user config his model
"""

from textual.widgets import Label, Input, Button, ProgressBar

from textual.app import ComposeResult

from textual.containers import VerticalScroll, Horizontal, Center

from textual.color import Gradient

from textual import work

from myfirstnn.learning import model_learning as model_l

from myfirstnn.learning import random_io_tensors as rand_tens

from myfirstnn.neuraln import SimpleNN


class ModelConfig(VerticalScroll):
    """
    This class manage the user inputs to start the training
    """

    def __init__(self, *children, **kwargs):

        super().__init__(*children, **kwargs)

    def compose(self) -> ComposeResult:

        yield Label(content="Write here your model name:")

        yield Input(placeholder="Your model name here...", value="str", id="model-name")

        yield Button(label="Start training!", id="start-button", variant="warning")

        with Center(id="progress-div"):

            with Horizontal():

                gradient = Gradient.from_colors("#ffeb99", "#ffd633", "#e6b800")

                yield Label("[bold]Progress:[/] ")

                yield ProgressBar(gradient=gradient)

    # functions

    def start_training(self, event: Button.Pressed) -> None:

        if event.button.id == "start-button":

            model_name = self.query_one("#model-name", Input).value

    @work(thread=True, exclusive=True)
    def train_model(self, model_name: str):
        """
        Uses the resources form other sub-packages (learning and neuraln) to create a model and train it.
        Everything runs on a separate thread
        """

        model = SimpleNN(name=model_name)

        test_data = rand_tens(n_input=1000, n_range=2, y_function=lambda x: x**2)

        model_l(model=model, data=test_data, epochs=10000)
