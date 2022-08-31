from jfrog.config import set_config
import click

@click.group(help="Commands Realting to Authentication")
def auth():
    pass

@auth.command(help="Authenticate with JFrog Credentials")
@click.option("--url", prompt=True)
@click.option("-u", "--username", prompt=True)
@click.option('-p', '--password', prompt=True, hide_input=True, help="An Access Token Generated From Your Dashboard")
def login(url, username, password):
    set_config("auth", "url", url)
    set_config("auth", "username", username)
    set_config("auth", "access_token", password)
    click.echo("Authentication Successful")