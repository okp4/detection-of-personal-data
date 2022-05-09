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
    "--tresh",
    "tresh",
    type=float,
    default=0.9,
    show_default=True,
    help="the minimum probability of prvate data",
)
def pii_detect(
    sentence,
    tresh,
):
    """Represents cli 'pii_detect' command"""
    validate_args(sentence, tresh)
    pipe = pipeline("zero-shot-classification",
                    model="facebook/bart-large-mnli")
    res = predict(pipe, sentence, tresh)
    print(res)


def validate_args(
    sentence: str, tresh: float
):
    return True


if __name__ == "__main__":
    cli()
