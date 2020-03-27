Machine Learning
================

This project is my effort to learn the fundamentals of Machine Learning in
Python. It is forked from [ageron's project](https://github.com/ageron/handson-ml2).
It contains the example code and solutions to the exercises in
[Hands-on Machine Learning with Scikit-Learn, Keras and TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) book.

![ML Book](https://images-na.ssl-images-amazon.com/images/I/51aqYc1QyrL._SX379_BO1,204,203,200_.jpg)

## Quick Start

Clone this project by opening a terminal and typing the following commands
 (do not type the first `$` signs on each line, they just indicate that these
are terminal commands):

    $ git clone https://github.com/hsgrewal/learning-ml.git
    $ cd learning-ml

If you want to use a GPU, then edit `environment.yml`
(or `environment-windows.yml` on Windows) and replace `tensorflow=2.0.1`
with `tensorflow-gpu=2.0.0`. Also replace `tensorflow-serving-api==2.0.1` with
 `tensorflow-serving-api-gpu==2.0.0`.

Next, run the following commands:

    $ conda env create -f environment.yml # or environment-windows.yml on Windows
    $ conda activate tf2
    $ python -m ipykernel install --user --name=python3

Then if you're on Windows, run the following command:

    $ pip install --no-index -f https://github.com/Kojoley/atari-py/releases atari_py

Finally, start Jupyter:

    $ jupyter notebook

If you need further instructions, read the [detailed installation instructions](INSTALL.md).
