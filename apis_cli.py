import click
import requests

BASE_URL = 'https://api.publicapis.org'

@click.group()
def apis():
    """A CLI wrapper for the API of Public APIs."""


@click.option('-t', '--title', help='Name of API (matches via substring - i.e. "at" would return "cat" and "atlas".)')
@click.option('-c', '--category', help='Return only APIs from this category')
@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@apis.command()
def entries(title: str, category: str, no_auth: bool):
    """List all cataloged APIs."""
    params = {
        'title': title,
        'category': category
    }

    if no_auth:
        params['auth'] = 'null'

    response = requests.get(url=f'{BASE_URL}/entries', params=params)

    if response.status_code is 200:
        for i, entry in enumerate(response.json()['entries']):
            pretty_entry = '\n'.join(f'{k}: {v}' for k, v in entry.items())
            print(f'{i + 1}.\n{pretty_entry}\n')
    else:
        print(f'Could not get the APIs: {response.text}')


@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@click.option('-c', '--category', help='Return only APIs from this category')
@click.option('-t', '--title', help='Name of API (matches via substring - i.e. "at" would return "cat" and "atlas".)')
@apis.command()
def random(title: str, category: str, no_auth: bool):
    """List a single API selected at random."""
    response = requests.get(url=f'{BASE_URL}/random')

    if response.status_code is 200:
        for i in response.json()['entries']:
            pretty_entry = '\n'.join(f'{k}: {v}' for k, v in i.items())
            print(f'\n{pretty_entry}\n')
    else:
        print(f'Could not get the APIs: {response.text}')


@apis.command()
def categories():
    """List all categories of APIs."""

    response = requests.get(url=f'{BASE_URL}/categories')
    if response.status_code is 200:
        print('\n'.join(response.json()))
    else:
        print(f'Could not get the categories: {response.text}')
    



if __name__ == '__main__':
    apis(prog_name='apis')