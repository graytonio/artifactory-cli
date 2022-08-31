import click

from jfrog.api import api_get_request


@click.group(help="Commands Relating to Storage Configuration")
def storage():
    pass


@storage.command(help="Get Storage Summary")
def info():
    try:
        results = api_get_request("/artifactory/api/storageinfo")
        data = results.json()
        click.echo("Binaries:")
        click.echo(f"\tCount: {data['binariesSummary']['binariesCount']}")
        click.echo(f"\tTotal Size: {data['binariesSummary']['binariesSize']}")
        click.echo("Artifacts:")
        click.echo(f"\tCount: {data['binariesSummary']['artifactsCount']}")
        click.echo(f"\tTotal Size: {data['binariesSummary']['artifactsSize']}")
        click.echo("Files:")
        click.echo(
            f"\tStorage Type: {data['fileStoreSummary']['storageType']}")
        click.echo(
            f"\tTotal Space: {'N/A' if not 'totalSpace' in data['fileStoreSummary'] == None else data['fileStoreSummary']['totalSpace']}")
        click.echo(
            f"\tUsed Space: {'N/A' if not 'usedSpace' in data['fileStoreSummary'] == None else data['fileStoreSummary']['usedSpace']}")
        click.echo(
            f"\tFree Space: {'N/A' if not 'freeSpace' in data['fileStoreSummary'] == None else data['fileStoreSummary']['freeSpace']}")
    except Exception as err:
        click.echo(err)
