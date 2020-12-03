import importlib
import pkgutil

from click.testing import CliRunner
from glcli.glcli import GitlabContext

from devcli import devcli

context = GitlabContext.from_config_file()
def load_plugins():
    return {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in pkgutil.iter_modules()
        if name.startswith('devcli')
    }


plugins = load_plugins()
runner = CliRunner()
result = runner.invoke(devcli.cli, ['--group', 'dearhealth', '--import'])


