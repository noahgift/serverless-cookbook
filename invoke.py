#!/usr/bin/env python
import click
import requests


@click.group()
@click.version_option("1.0")
def cli():
    """Invoker"""


@cli.command("http")
@click.option("--amount", default=1.34, help="Change to Make")
@click.option(
    "--host",
    default="https://us-central1-cloudai-194723.cloudfunctions.net/change722",
    help="Host to invoke",
)
def mkrequest(amount, host):
    """Asks a web service to make change"""

    click.echo(
        click.style(
            f"Querying host {host} with amount: {amount}", bg="green", fg="white"
        )
    )
    payload = {"amount": amount}
    result = requests.post(url=host, json=payload)
    click.echo(click.style(f"result: {result.text}", bg="red", fg="white"))


if __name__ == "__main__":
    cli()
