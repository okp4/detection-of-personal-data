import click
from transformers import pipeline
from joblib import Parallel, delayed
import pandas as pd
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
    "-s",
    "--sentence",
    "sentence",
    type=str,
    required=True,
    help="sentence to process"
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
def pii_detect(
    df: pd.DataFrame,
    thresh =0.9,
):
    """Represents cli 'pii_detect' command"""
    # validate_args(sentence, thresh)
    pipe = pipeline("zero-shot-classification",
                    model="facebook/bart-large-mnli")
    res= [Parallel()(delayed(predict)(pipe, sentence, thresh) for sentence in df['sentence'])]
    print(res)


# def validate_args(
#     sentence: str, thresh: float
# ):
#     return True


if __name__ == "__main__":
    cli()
