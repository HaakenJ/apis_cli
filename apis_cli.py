import click

@click.group()
def apis():
    """A CLI wrapper for the API of Public APIs."""





if __name__ == '__main__':
    apis(prog_name='apis')