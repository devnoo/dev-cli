import logging
import os
from pathlib import Path

import subprocess


def install_script(path: Path):
    if (path/'pyproject.toml').exists():

        logging.debug(f'pyproject.toml found, running poetry install')
        p = subprocess.Popen(['poetry', 'install'], cwd=path.absolute())
        p.wait()
    else:
        logging.debug(f'No pyproject.toml found, skipping {path}')