import click
import time

from .config import get_config, set_config
from .artifactory import commands as artifactory

@click.group()
def entry_point():
    pass

@entry_point.command()
@click.option("--url", prompt=True)
@click.option("-u", "--username", prompt=True)
@click.option('-p', '--password', prompt=True, hide_input=True, help="An Access Token Generated From Your Dashboard")
def login(url, username, password):
    set_config("auth", "url", url)
    set_config("auth", "username", username)
    set_config("auth", "access_token", password)
    click.echo("Authentication Successful")

entry_point.add_command(artifactory.arti)