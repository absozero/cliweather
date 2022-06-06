import requests
import click
import json

weath_gov = "https://api.weather.gov/"

usweath = requests.get(weath_gov)


@click.group()
def cli():
    # This is the main function that will be called when the program is run
    # It is the entry point of the program, as well as the command line interface.
    # It is a gro
    pass

@cli.command()
def us():
    click.secho(usweath.json(), fg='green')

@cli.group()
def ca():
    pass

@ca.command()
def toronto():
    click.secho("Toronto", fg='green')

if __name__ == '__main__':
    cli()




