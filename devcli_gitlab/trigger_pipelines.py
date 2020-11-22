import click

from . import GitlabClient
from .gitlab_group import gitlab


@gitlab.command(short_help='triggers the pipeline for all projects in group')
@click.pass_obj
@click.option('--group')
def trigger_pipelines(client: GitlabClient , group):
    client.do_for_every_project(group, lambda project: project.pipelines.create({'ref': 'master'}))

