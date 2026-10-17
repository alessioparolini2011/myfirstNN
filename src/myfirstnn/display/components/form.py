"""
form.py
Authors: Alessio Parolini
This file contains the class to make the user config his model
"""

__all__ = ["ModelConfig"]

from textual.widgets import Label, Input, Button, RichLog

from textual.app import ComposeResult

from textual.containers import Container, Center

from textual import work

from myfirstnn.learning import model_learning as model_l

from myfirstnn.learning import random_io_tensors as rand_tens

from myfirstnn.neuraln import SimpleNN


class ModelConfig(Container):
    """
    This class manage the user inputs to start the training
    """

    def __init__(self, *children, **kwargs):

        super().__init__(*children, **kwargs)

    def compose(self) -> ComposeResult:

        yield Label(
            content="[bold]Write here your model name:[/]",
            id="model-label",
            classes="form-label",
        )

        yield Input(
            placeholder="Your model name here...",
            id="model-name",
            type="text",
        )

        yield Label(
            content="[bold]How much data you wanna use (type an integer)?[/] Remind: more data means more work for your CPU/GPU",
            id="inputs-label",
            classes="form-label",
        )

        yield Input(
            placeholder="Enter the number of input do you wanna use...",
            id="model-inputs",
            type="integer",
            restrict="^[0-9]+$",
        )

        with Center():

            yield Button(
                label="Start training!",
                id="start-button",
                variant="warning",
            )

        yield RichLog(markup=True, id="training-log")

    # functions

    def on_button_pressed(self, event: Button.Pressed) -> None:

        if event.button.id == "start-button":

            model_name = self.query_one("#model-name", Input).value or "UserModel"

            model_inputs = self.query_one("#model-inputs", Input).value or 200

            self.query_one("#start-button", Button).disabled = True

            self.app.set_focus(self.query_one("#training-log"))

            self.training_setup(model_name=model_name, model_inputs=int(model_inputs))

    @work(thread=True, exclusive=True)
    def training_setup(self, model_name: str, model_inputs: int):
        """
        Uses the resources form other sub-packages (learning and neuraln) to create a model and train it.
        Everything runs on a separate thread
        """

        model = SimpleNN(name=model_name)

        test_data = rand_tens(
            n_input=model_inputs, n_range=2, y_function=lambda x: x**2
        )

        text_log = self.query_one(RichLog)

        text_log.write("Starting the model log...")

        model_l(model=model, data=test_data, epochs=10000, log_func=text_log.write)

        self.app.call_from_thread(
            lambda: setattr(self.query_one("#start-button", Button), "disabled", False)
        )
