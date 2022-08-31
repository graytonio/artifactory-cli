import click

from .auth.commands import auth
from .artifactory.commands import arti as artifactory

@click.group()
def entry_point():
    pass

entry_point.add_command(auth)
entry_point.add_command(artifactory)