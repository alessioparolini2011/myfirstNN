"""
form.py
Authors: Alessio Parolini
This file contains the class to make the user config his model
"""

__all__ = ["ModelConfig"]

from textual.widgets import Label, Input, Button, RichLog

from textual.app import ComposeResult

from textual.containers import VerticalScroll

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

        yield Input(
            placeholder="Your model name here...",
            id="model-name",
            type="text",
        )

        yield Button(
            label="Start training!",
            id="start-button",
            variant="warning",
        )

        yield RichLog()

    # functions

    def on_button_pressed(self, event: Button.Pressed) -> None:

        if event.button.id == "start-button":

            model_name = self.query_one("#model-name", Input).value

            self.training_setup(model_name=model_name)

    @work(thread=True, exclusive=True)
    def training_setup(self, model_name: str):
        """
        Uses the resources form other sub-packages (learning and neuraln) to create a model and train it.
        Everything runs on a separate thread
        """

        model = SimpleNN(name=model_name)

        test_data = rand_tens(n_input=1000, n_range=2, y_function=lambda x: x**2)

        text_log = self.query_one(RichLog)

        text_log.write("Starting the model log...")

        model_l(model=model, data=test_data, epochs=10000, log_func=text_log.write)
