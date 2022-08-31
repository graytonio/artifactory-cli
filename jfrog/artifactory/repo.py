import click
from tabulate import tabulate

from jfrog.api import api_get_request, api_post_request, api_put_request

# Repository Commands
# TODO Add more feature flags for create/update


@click.group(help="Commands Relating to Repository Mangement")
def repo():
    pass


@repo.command(help="Create a New Repository")
@click.option("-n", "--name", prompt=True)
def new(name):
    try:
        api_put_request(
            f"/artifactory/api/repositories/{name}", json={'rclass': 'local'})
        click.echo("Repo Created Successfully")
    except Exception as err:
        click.echo(err)


@repo.command(help="Update Repository Settings")
@click.option("-n", "--name", prompt=True)
@click.option("-u", "--new_name", prompt=True)
def update(name, new_name):
    try:
        api_post_request(
            f"/artifactory/api/repositores/{name}", json={'rclass': 'local', 'key': new_name})
        click.echo("Repo Updated Successfully")
    except Exception as err:
        click.echo(err)


@repo.command(help="List Repositories")
def list():
    try:
        results = api_get_request("/artifactory/api/repositories")
        data = results.json()
        click.echo(tabulate(data, headers={
                   'key': "ID", "description": "Description", "type": "Type", "url": "URL", "packageType": "Package Type"}))
    except Exception as err:
        click.echo(err)
