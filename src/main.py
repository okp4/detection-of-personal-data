import click
from transformers import pipeline
from functions import predict
import pandas as pd
import os
from tqdm import tqdm
import __init__ as init
import json
from nltk.tokenize import sent_tokenize


def validate_dir_path(ctx, param, value):
    if not os.path.isdir(value):
        raise click.BadParameter("path must point to an existing directory")
    return value


def validate_file_path(ctx, param, value):
    if not os.path.isfile(value):
        raise click.BadParameter("path must point to an existing file")
    return value


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
    "-i",
    "--input",
    "input_file",
    type=str,
    callback=validate_file_path,
    required=True,
    help="path to text file",
)
@click.option(
    "-o",
    "--output",
    "out_dir",
    type=str,
    callback=validate_dir_path,
    default=".",
    show_default=True,
    help="output directory where json file will be written",
)
@click.option(
    "-tr",
    "--thresh",
    "thresh",
    type=float,
    default=0.9,
    show_default=True,
    help="the minimum probability of private data for label : cookie, location, health, social security number,Tax file number, credit card",
)
def pii_detect(
    out_dir,
    input_file,
    thresh,
) -> list:
    """Represents cli 'pii_detect' command"""
    with open(input_file) as f:
        list_sent = [line.rstrip() for line in f]
    pipe = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    detected_labels: list = [
        predict(pipe, sent, thresh) for sent in tqdm(list_sent, total=len(list_sent))
    ]
    results = list(zip(*detected_labels))[0]
    results = list(filter(None, results))
    sentences = list(zip(*detected_labels))[1]
    sentences = list(filter(None, sentences))
    outputs_detected = {}
    detected = 0
    if results != []:
        detected = sum(list(zip(*results))[0])
        outputs_detected = {
            sent: reslt for (sent, reslt) in zip(sentences, list(zip(*results))[1])
        }
    output = {
        "FileName": os.path.basename(input_file),
        "Personal information detected": True if detected > 0 else False,
        "Results": outputs_detected,
    }
    output_path = os.path.join(
        "./", out_dir, "sheet_" + os.path.basename(input_file) + "_result.json"
    )
    with open(output_path, "w") as fp:
        json.dump(output, fp)


if __name__ == "__main__":
    cli()
