import click
from jfrog.api import api_get_request
from .repo import repo
from .user import user
from .storage import storage


@click.group(help="Artifactory API")
def arti():
    pass


arti.add_command(repo)
arti.add_command(user)
arti.add_command(storage)


@arti.command(help="Check on System Health")
def ping():
    try:
        api_get_request('/artifactory/api/system/ping')
        click.echo("System is Healthy")
    except Exception as err:
        click.echo(err)


@arti.command(help="Get System Version Information")
def version():
    try:
        results = api_get_request("/artifactory/api/system/version")
        data = results.json()
        click.echo(f"Version: {data['version']}")
        click.echo(f"Revision: {data['revision']}")
        click.echo(f"Addons: {data['addons']}")
    except Exception as err:
        click.echo(err)
