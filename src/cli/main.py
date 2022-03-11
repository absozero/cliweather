import requests
import sys
import click


weath_gov = "https://api.weather.gov/"

usweath = requests.get(weath_gov)

@click.command()
def hello():
    click.secho(usweath.json(), fg='green')

if __name__ == '__main__':
    hello()




