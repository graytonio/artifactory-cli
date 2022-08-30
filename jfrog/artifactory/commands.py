import click
from jfrog.api import api_delete_request, api_get_request, api_post_request, api_put_request

from tabulate import tabulate

@click.group()
def arti():
    pass

# System Level Commands
@arti.command()
def ping():
    try:
        api_get_request('/artifactory/api/system/ping')
        click.echo("System is Healthy")
    except Exception as err:
        click.echo(err)

@arti.command()
def version():
    try:
        results = api_get_request("/artifactory/api/system/version")
        data = results.json()
        click.echo("Version: {}".format(data['version']))
        click.echo("Revision: {}".format(data['revision']))
        click.echo("Addons: {}".format(", ".join(data['addons'])))
    except Exception as err:
        click.echo(err)   
    
@arti.command()
def storageinfo():
    try:
        results = api_get_request("/artifactory/api/storageinfo")
        data = results.json()
        click.echo("Binaries:")
        click.echo("\tCount: {}".format(data['binariesSummary']['binariesCount']))
        click.echo("\tTotal Size: {}".format(data['binariesSummary']['binariesSize']))
        
        click.echo("Artifacts:")
        click.echo("\tCount: {}".format(data['binariesSummary']['artifactsCount']))
        click.echo("\tTotal Size: {}".format(data['binariesSummary']['artifactsSize']))
        
        click.echo("Files:")
        click.echo("\tStorage Type: {}".format(data['fileStoreSummary']['storageType']))
        click.echo("\tTotal Space: {}".format("N/A" if not 'totalSpace' in data['fileStoreSummary'] == None else data['fileStoreSummary']['totalSpace']))
        click.echo("\tUsed Space: {}".format("N/A" if not 'usedSpace' in data['fileStoreSummary'] == None else data['fileStoreSummary']['usedSpace']))
        click.echo("\tFree Space: {}".format("N/A" if not 'freeSpace' in data['fileStoreSummary'] == None else data['fileStoreSummary']['freeSpace']))
    except Exception as err:
        click.echo(err)
    
# User Commands
# TODO Add more feature flags for create
@arti.group()
def user():
    pass

@user.command()
@click.option("-u", "--username", prompt=True)
@click.option("-e", "--email", prompt=True)
@click.option("-p", "--password", prompt=True, hide_input=True)
def new(username, email, password):
    try:
        json = { 'email': email, 'password': password }
        api_put_request("/artifactory/api/security/users/{}".format(username), json)
        click.echo("User Created Successfully")
    except Exception as err:
        click.echo(err)
    
@user.command()
@click.option("-u", "--username", prompt=True, confirmation_prompt=True)
def delete(username):
    try:
        api_delete_request('/artifactory/api/security/users/{}'.format(username))
        click.echo("User Deleted Successfully")
    except Exception as err:
        click.echo(err)
    
# Repository Commands
# TODO Add more feature flags for create/update
@arti.group()
def repo():
    pass
    
@repo.command()
@click.option("-n", "--name", prompt=True)
def new(name):
    try:
        api_put_request("/artifactory/api/repositories/{}".format(name), json={ 'rclass': 'local' })
        click.echo("Repo Created Successfully")
    except Exception as err:
        click.echo(err)
    
@repo.command()
@click.option("-n", "--name", prompt=True)
@click.option("-u", "--new_name", prompt=True)
def update(name, new_name):
    try: 
        api_post_request("/artifactory/api/repositores/{}".format(name), json={ 'rclass': 'local', 'key': new_name })
        click.echo("Repo Updated Successfully")
    except Exception as err:
        click.echo(err)

@repo.command()
def list():
    try:
        results = api_get_request("/artifactory/api/repositories")
        data = results.json()
        click.echo(tabulate(data, headers={ 'key': "ID", "description": "Description", "type": "Type", "url": "URL", "packageType": "Package Type" }))
    except Exception as err:
        click.echo(err)