import click
from transformers import pipeline
from functions import predict
import __init__ as init


@click.group
def cli():
    """Represents the root cli function"""
    pass


@cli.command
def version():
    """Represents cli 'version' command"""
    click.echo(init.__version__)


@cli.command
@click.option(
    "-s", "--sentence", "sentence", type=str, required=True, help="sentence to process"
)
@click.option(
    "-tr",
    "--thresh",
    "thresh",
    type=float,
    default=0.9,
    show_default=True,
    help="the minimum probability of private data",
)
def detect_labels(sentence, thresh):
    pipe = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    """Detect personal data"""
    predict(
        pipe,
        sentence,
        thresh,
    )


if __name__ == "__main__":
    cli()
