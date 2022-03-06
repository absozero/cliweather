import requests
import sys
import click


usweath = requests.get("https://api.weather.gov/")

@click.command()
def hello():
    click.echo(usweath.json())

if __name__ == '__main__':
    hello()




