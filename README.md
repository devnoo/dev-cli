# Simple development cli
This is a simple development cli, that i wrote for mainly for my own usage in day
to day tasks.
It currently supports a gitlab plugin, which you can sync a group to a local directory,
and if found installing poetry and npm packages. This is plugin based, so easy to
extend to your use case. It also supports installing precommit hooks.
It is very opinionated, seeing I wrote it for my own use cases.

It also has a couple of methods around starting all pipelines for a group,
editing a file in all repos in a group, adding a file to all repo's in a group
etc.


## Basic usage


## Gitlab plugin

In the ~/.devcli_config file there should be the following:

```yaml
gitlab.token=<your-presonal-token>
```

### sync command
It will scan the given group for all subprojects, including those in subgroups,
and will pull them to the current directory, respecting the tree structure in gitlab.
Basically like gitlabber does it.
If --install is passed, it will run all plugins install_scripts.
By default there is a poetry install plugin(running poetry install), a  npm install plugin(npm install) and a precommit hooks
plugin, which will do its work if precommit is installed locally, or as dev dependecy in .venv of the project

```shell
devcli gitlab sync --group 'devnoo' --install
```
devcli_poetry_install






