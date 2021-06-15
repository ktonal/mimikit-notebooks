from textwrap import dedent
import nbformat as nbf
from inspect import getsource
import re

import mimikit as mmk


def colab_setup():
    title = nbf.v4.new_markdown_cell("""\
## Connect to your GDrive\
""")
    mount_drive = nbf.v4.new_code_cell("""\
from google.colab import drive
drive.mount('/gdrive')
%cd /gdrive/MyDrive
""")
    install = nbf.v4.new_markdown_cell("""\
### Install `mimikit`\
""")
    pip = nbf.v4.new_code_cell(f"""
!pip install mimikit=={mmk.__version__}""")
    return [title, mount_drive, install, pip]


def demo_to_notebook(demo, out_file, colab=False):
    code = getsource(demo)
    code = code.strip("def demo():\n")
    code = dedent(code)
    parts = re.split(r"(\"\"\".*\"\"\")", code)
    nb = nbf.v4.new_notebook()
    cells = []
    if colab:
        nb["metadata"].update(dict(accelerator='GPU'))
        cells += colab_setup()
    else:
        warning = nbf.v4.new_markdown_cell(f"""\
this notebook assumes you already installed mimikit on your system through the command-line
```bash
pip install mimikit=={mmk.__version__}
```
""")
        cells += [warning]
    for part in parts:
        if '"""' in part:
            cells += [nbf.v4.new_markdown_cell(part.strip('"""'))]
        else:
            part = dedent(part.strip('\n\n').strip("\n"))
            if part:
                cells += [nbf.v4.new_code_cell(part)]
    signature = nbf.v4.new_markdown_cell("""<img src="https://ktonal.com/k-circle-bw.png" alt="logo" width="75"/>""")
    nb['cells'] = cells + [signature]
    with open(out_file, 'w') as f:
        nbf.write(nb, f)


if __name__ == '__main__':
    import os
    from mimikit.models.freqnet import demo as fnet_demo
    from mimikit.models.sample_rnn import demo as srnn_demo
    # from mimikit.models.wavenet import demo as wn_demo
    from mimikit.models.s2s_lstm import demo as s2s_demo

    roots = [
        './demos/plain',
        './demos/colab',
    ]

    demos = {
        "freqnet.ipynb": fnet_demo,
        "sample-rnn.ipynb": srnn_demo,
        "seq2seq-lstm.ipynb": s2s_demo,
    }

    for root in roots:
        if not os.path.exists(root):
            os.makedirs(root, exist_ok=True)
        for name, demo in demos.items():
            demo_to_notebook(demo, os.path.join(root, name), colab='colab' in root)

