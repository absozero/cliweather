import requests
import sys
import click


weath_gov = "https://api.weather.gov/"

usweath = requests.get(weaht_gov)

@click.command()
def hello():
    click.echo(usweath.json())

if __name__ == '__main__':
    hello()




