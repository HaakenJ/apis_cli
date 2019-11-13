import click

@click.group()
def apis():
    """A CLI wrapper for the API of Public APIs."""


@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@click.option('-c', '--category', help='Return only APIs from this category')
@click.option('-t', '--title', help='Name of API (matches via substring - i.e. "at" would return "cat" and "atlas".)')
@apis.command()
def entries(title: str, category: str, no_auth: bool):
    """List all cataloged APIs."""


@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@click.option('-c', '--category', help='Return only APIs from this category')
@click.option('-t', '--title', help='Name of API (matches via substring - i.e. "at" would return "cat" and "atlas".)')
@apis.command()
def random(title: str, category: str, no_auth: bool):
    """List a single API selected at random."""



@apis.command()
def categories():
    """List all categories of APIs."""



if __name__ == '__main__':
    apis(prog_name='apis')