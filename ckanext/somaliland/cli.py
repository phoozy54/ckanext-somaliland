import click


@click.group(short_help="somaliland CLI.")
def somaliland():
    """somaliland CLI.
    """
    pass


@somaliland.command()
@click.argument("name", default="somaliland")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [somaliland]
