import click

from jfrog.api import api_delete_request, api_put_request

# User Commands
# TODO Add more feature flags for create


@click.group(help="Commands Relating to User Management")
def user():
    pass


@user.command()
@click.option("-u", "--username", prompt=True)
@click.option("-e", "--email", prompt=True)
@click.option("-p", "--password", prompt=True, hide_input=True)
def new(username, email, password):
    try:
        json = {'email': email, 'password': password}
        api_put_request(f"/artifactory/api/security/users/{username}", json)
        click.echo("User Created Successfully")
    except Exception as err:
        click.echo(err)


@user.command()
@click.option("-u", "--username", prompt=True, confirmation_prompt=True)
def delete(username):
    try:
        api_delete_request(f'/artifactory/api/security/users/{username}')
        click.echo("User Deleted Successfully")
    except Exception as err:
        click.echo(err)
