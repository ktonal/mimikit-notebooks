Hardware and software setup - basic python and jupyter notebooks
================================================================

In a Nutshell
-------------

If you are completely new to the whole python/deep-learning environment, here are a few facts you need to know.

- **python** is a programming language that can run on any OS and is, de facto, becoming the most used language in deep-learning.
- a **notebook** is an interface to an `IPython kernel`, a background process that execute python code. In a notebook, you can store, edit and execute python code and interact with whatever this code outputs.
- mimikit is a package that contains the python code that is then `invoked` or `called` by the mimikit-notebooks.


Hardware Setup
--------------

Doing deep-learning requires a **GPU** (Graphics Processing Unit), simply because deep-learning algorithms rely on certain computations
for which GPUs have been designed. Although running those algorithms on a CPU is perfectly fine, it is, unfortunately, prohibitively slow.

Furthermore, deep-learning libraries specifically need **NVIDIA GPU** and are not compatible with models from other manufacturer.

GPU Providers
^^^^^^^^^^^^^

If you don't own a NVIDIA GPU, there exists several online GPU provider that offer limited free access along with various paid plans.
For instance :

    - `Google Colab <https://colab.research.google.com/notebooks/intro.ipynb>`_

    - `Paperspace <https://www.paperspace.com/>`_

    - `Kaggle <https://www.kaggle.com/code>`_

When using those services, you essentially rent or borrow a computer with a GPU and connect to it through a web page in your browser (a notebook).

If you have access to a NVIDIA GPU, you only need to make sure that an appropriate driver is installed on your system, before you go through the Software installation steps.


Software Installation
---------------------

On your system
^^^^^^^^^^^^^^^^^

In order to run the mimikit-notebooks on your system, you'll need Linux or MacOS with ``python>=3.8`` and ``pip`` installed.
Once you do, open a terminal and enter the command-line

.. code-block:: bash

    pip install mimikit

This will download ``mimikit`` and install it on your system.

- create a directory in your ``User/home/``, something like ``User/home/mmk-stuff/``.
- under ``mmk-stuff/``, create two directories ``data/`` and ``notebooks/``.
- open a browser and go to `the list of plain notebooks on github <https://github.com/ktonal/mimikit-notebooks/tree/main/demos/plain>`_.
- Click on the one you want to download on the page showing its code
- click on the ``Raw`` button on the right.
- Hit `Cmd+S` or `Ctrl+S` to save the notebook on your system in ``mmk-stuff/notebooks``
- Now, open a terminal and ``cd`` to ``mmk-stuff``
- Finally, enter the command-line

.. code-block:: bash

    jupyter notebook

This will launch an IPython kernel and open a new window in your browser. In this window, navigate to where you downloaded a notebook and click on it.


With a GPU Provider
^^^^^^^^^^^^^^^^^^^

Because GPU providers want to make your life easier, they all offer kernels with software commonly used for deep-learning pre-installed.
Every time you open a kernel or a session, you get a "new computer" with ``python`` and the necessary deep-learning libraries already installed.

The only piece of software you'll still need to install *every time you open a session* is ``mimikit``. To do so, one only needs to execute a code cell with the following line

.. code-block::

    !pip install mimikit

Please note that **all the colab mimikit-notebooks already have this cell** so that running a notebook always includes installing ``mimikit``.


Basic Python - Jupyter Notebook
-------------------------------

Although running the mimikit-notebooks doesn't require you to be able to write python code, you might find it useful to know the basics.
Here, we simply point to resources we find useful and invite you to check them out.

- `Interactive Python tutorial <https://www.learnpython.org/>`_
- `Jupyter Notebook Basics <https://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb>`_
- `Jupyter Notebook Beginner Guide <https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/index.html>`_
- `Intro Colab <https://colab.research.google.com/notebooks/intro.ipynb>`_ and `Colab Features Overview <https://colab.research.google.com/notebooks/basic_features_overview.ipynb>`_

