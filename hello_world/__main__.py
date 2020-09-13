import click
from .hello_world import hello


@click.command()
@click.option("--name", prompt="Your name", help="The person to greet.")
def main(name=""):
    hello(name)


main()