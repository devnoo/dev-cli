import os
from pathlib import Path

import subprocess


def install_script(path: Path):
    print(path)
    if (path/'package.json').exists():
        p = subprocess.Popen(['npm', 'install'], cwd=path.absolute())
        p.wait()
        print('bla')