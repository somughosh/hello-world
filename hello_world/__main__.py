import typer
from . import hello_world


def main(name: str = "World"):
    """
    Say Hello with any name given
    """
    print(hello_world.hello(name))


if __name__ == "__main__":
    typer.run(main)
