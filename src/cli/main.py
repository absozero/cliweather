import argparse
import requests

import click


@click.command()
def hello():
    click.echo('Hello World!')

usweath = requests.get("https://api.weather.gov/")

if __name__ == '__main__':
    hello()




