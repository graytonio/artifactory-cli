import click

from jfrog.api import api_delete_request, api_put_request

# User Commands
# TODO Add more feature flags for create


@click.group(help="Commands Relating to User Management")
def user():
    pass


@user.command()
@click.option("-u", "--username", prompt=True, help="Username to give new User")
@click.option("-e", "--email", prompt=True, help="Email of New User")
@click.option("-p", "--password", prompt=True, hide_input=True, help="Password of New User")
@click.option("-a", "--admin", is_flag=True, help="Create Admin User")
@click.option("-g", "--group", multiple=True, help="A Group User Should belong to")
def new(username, email, password, admin, group):
    try:
        json = {'email': email, 'password': password, "admin": admin, "groups": group}
        api_put_request(f"/artifactory/api/security/users/{username}", json)
        click.echo("User Created Successfully")
    except Exception as err:
        click.echo(err)


@user.command()
@click.option("-u", "--username", prompt=True, confirmation_prompt=True, help="Username of User to Delete")
def delete(username):
    try:
        api_delete_request(f'/artifactory/api/security/users/{username}')
        click.echo("User Deleted Successfully")
    except Exception as err:
        click.echo(err)
