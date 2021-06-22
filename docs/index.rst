.. mimikit documentation master file, created by
   sphinx-quickstart on Fri Jan  8 04:24:18 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

mimikit-notebooks
=================

|Colab Badge|  |GitHub Badge|

.. toctree::
   :maxdepth: 2
   :caption: Content

The mimikit-notebooks are a small collections of jupyter notebooks containing scripts to train audio generative neural networks.

.. list-table:: Notebooks Overview
   :widths: auto

   * - **Model**
     - **Plain**
     - **Colab**
   * - Wavenet
     - |Github Wavenet|
     - |Colab Wavenet|
   * - SampleRNN
     - |Github SampleRNN|
     - |Colab SampleRNN|
   * - FreqNet
     - |Github FreqNet|
     - |Colab FreqNet|
   * - Seq2SeqLSTM
     - |Github S2S|
     - |Colab S2S|


You'll find examples of what those notebooks output when trained on different single audio files at

   https://ktonal.github.io/mimikit-demo-outputs


Since all notebooks follow the same design, this documentation covers the general usage of the notebooks.
It is intended for people who have little prior knowledge of python & deep-learning and wants to get a hands-on first contact.

The fastest track, is to open one of the "Open in Colab" above, and evaluate the cells with `shift+enter`. The program will
require you to connect to your Gdrive. Before doing so, make sure you placed some audio files in ``<username>/MyDrive/data`` on your Gdrive.
Keep running the cells with `shift+enter`. Generated audio will be displayed during training.

If you have questions or troubles running the scripts, join our slack channel |Slack Badge|

.. toctree::
   :maxdepth: 1
   :caption: User Guide

   Pre-requisites
   How to run a demo
   How to train on data you provide
   How to save outputs and models


.. |Colab Badge| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/ktonal/mimikit-notebooks/blob/main

.. |GitHub Badge| image:: https://img.shields.io/static/v1.svg?logo=github&label=Repo&message=View%20On%20Github&color=blue
   :target: https://github.com/ktonal/mimikit-notebooks/

.. |Slack Badge| image:: https://img.shields.io/badge/slack-mimikit-blue.svg?logo=slack
   :target: https://join.slack.com/t/mimikit/shared_invite/zt-rsu1cuzm-a8Zi~dDOtIr5nE6uaAlJUA

.. |Colab Wavenet| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/ktonal/mimikit-notebooks/blob/main/demos/colab/wavenet.ipynb

.. |GitHub Wavenet| image:: https://img.shields.io/static/v1.svg?logo=github&label=Repo&message=View%20On%20Github&color=blue
   :target: https://github.com/ktonal/mimikit-notebooks/blob/main/demos/plain/wavenet.ipynb

.. |Sample Wavenet| raw:: html

   <audio controls="controls" style="height:24px;width:128px">
      <source src="https://github.com/ktonal/mimikit-notebooks/blob/main/assets/wn.mp3?raw=true" >
      Your browser does not support the <code>audio</code> element.
    </audio>

.. |Colab SampleRNN| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/ktonal/mimikit-notebooks/blob/main/demos/colab/sample-rnn.ipynb

.. |GitHub SampleRNN| image:: https://img.shields.io/static/v1.svg?logo=github&label=Repo&message=View%20On%20Github&color=blue
   :target: https://github.com/ktonal/mimikit-notebooks/blob/main/demos/plain/sample-rnn.ipynb

.. |Sample SampleRNN| raw:: html

   <audio controls="controls" style="height:24px;width:128px">
      <source src="https://github.com/ktonal/mimikit-notebooks/blob/main/assets/srnn.mp3?raw=true" >
      Your browser does not support the <code>audio</code> element.
    </audio>

.. |Colab FreqNet| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/ktonal/mimikit-notebooks/blob/main/demos/colab/freqnet.ipynb

.. |GitHub FreqNet| image:: https://img.shields.io/static/v1.svg?logo=github&label=Repo&message=View%20On%20Github&color=blue
   :target: https://github.com/ktonal/mimikit-notebooks/blob/main/demos/plain/freqnet.ipynb

.. |Sample FreqNet| raw:: html

   <audio controls="controls" style="height:24px;width:128px">
      <source src="https://github.com/ktonal/mimikit-notebooks/blob/main/assets/freqnet.mp3?raw=true" >
      Your browser does not support the <code>audio</code> element.
    </audio>

.. |Colab S2S| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/ktonal/mimikit-notebooks/blob/main/demos/colab/s2s.ipynb

.. |GitHub S2S| image:: https://img.shields.io/static/v1.svg?logo=github&label=Repo&message=View%20On%20Github&color=blue
   :target: https://github.com/ktonal/mimikit-notebooks/blob/main/demos/plain/s2s.ipynb

.. |Sample S2S| raw:: html

   <audio controls="controls" style="height:24px;width:128px">
      <source src="https://github.com/ktonal/mimikit-notebooks/blob/main/assets/s2s.mp3?raw=true" >
      Your browser does not support the <code>audio</code> element.
    </audio>