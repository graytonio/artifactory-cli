import click
from tabulate import tabulate

from jfrog.api import api_get_request, api_post_request, api_put_request

# Repository Commands
# TODO Add more feature flags for create/update

package_types = ['alpine', 'cargo', 'composer', 'bower', 'chef', 'cocoapods', 'conan', 'cran', 'debian', 'docker', 'helm', 'gems', 'gitlfs', 'go', 'gradle', 'ivy', 'maven', 'npm', 'nuget', 'opkg', 'pub', 'puppet', 'pypi', 'rpm', 'sbt', 'swift', 'terraform', 'vagrant', 'yum', 'generic']

@click.group(help="Commands Relating to Repository Mangement")
def repo():
    pass


@repo.command(help="Create a New Repository")
@click.option("-n", "--name", prompt=True, help="Repository Key")
@click.option("-d", "--description", help="Repository Description")
@click.option("--notes", help="Internal Notes for Repository")
@click.option("-t", "--package-type", help="Repository Package Type", type=click.Choice(package_types, case_sensitive=False), default="generic")
def new(name, description, notes, package_type):
    try:
        api_put_request(
            f"/artifactory/api/repositories/{name}", 
            json={ 'rclass': 'local', 'description': description, 'notes': notes, 'packageType': package_type })
        click.echo("Repo Created Successfully")
    except Exception as err:
        click.echo(err)


@repo.command(help="Update Repository Settings")
@click.option("-n", "--name", help="New Repository Name")
@click.option("-d", "--description", help="Repository Description")
@click.option("--notes", help="Internal Notes for Repository")
def update(name, description, notes):
    try:
        data = {}
        if description is not None:
            data['description'] = description
        if notes is not None:
            data['notes'] = notes

        api_post_request(
            f"/artifactory/api/repositories/{name}", json=data)
        click.echo("Repo Updated Successfully")
    except Exception as err:
        click.echo(err)


@repo.command(help="List Repositories", name="list")
def list_repos():
    try:
        results = api_get_request("/artifactory/api/repositories")
        data = results.json()
        click.echo(tabulate(data, headers={
                   'key': "ID", "description": "Description", "type": "Type", "url": "URL", "packageType": "Package Type"}))
    except Exception as err:
        click.echo(err)
