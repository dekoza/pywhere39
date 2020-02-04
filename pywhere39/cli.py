"""Console script for pywhere39."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for pywhere39."""
    click.echo("Replace this message by putting your code into " "pywhere39.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
