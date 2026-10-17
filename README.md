# autoNN

A simple TUI tool to create and train NN on random datas, to **teach the model how to calculate squares (x^2)**

> [!NOTE]
> I built this project for consolidate my skills and my knowledge about AI and Deep Learning. I know isn't perfect, I
know isn't so useful, I know the README is a too short... but is a **part of a bigger goal I'm working on. Stay tuned,
I'm gonna develop it soon**!

## Software Structure

The file has 4 packages:

+ **display**: contains the module that handles the TUI with Textual. Also contains the sub-package **components** with
  the different TUI components.

+ **learning**: contains the module with the functions to train the model once is created.

+ **neuraln**: contains the module with the class to create the model with his NN.

+ **core**: starts and runs all the software. His called in __main__.py to start the whole package

## How it works

When you start the software, the TUI runs in your terminal. When you set the name and the number of inputs, you can
press the button **"Start Training"** and let the magic starts! You'll see al the log of the training, with a live loss,
and ** you're gonna prove how an AI model training works!**

## How to install

To install this software, I need to have installed on your machine [Python](https://python.org) 3.11 or newest.

> [!NOTE]
>Please note that Python 3.15 is currently not fully supported by PyTorch, as key deep learning features like
torch.compile are broken and official precompiled binaries for CUDA/GPU acceleration are missing.

Then run

```bash
pip install myfirstnn

myfirstnn
```

to have a run-ready software. If you want to have an easier access to the software files on your device, run

```bash
git clone https://github.com/alessioparolini2011/autoNN.git
```

This command needs [Git](https://git-scm.com) on your device.

## Credits

This project was built using the following amazing open-source libraries:

* **[PyTorch](https://pytorch.org)** - An open-source machine learning framework used for creating, structuring, and
  training the neural network models.
* **[Textual](https://textualize.io)** - A Python framework, used to build the beautiful and interactive Terminal User
  Interface (TUI).

