import click
from transformers import pipeline
import os
from detection_of_personal_data.functions import predict, out
from tqdm import tqdm
import detection_of_personal_data.__init__ as init
from nltk.tokenize import sent_tokenize
import logging

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s ",
    level=logging.INFO,
)

threshs = {
    "birth": 0.8,
    "person": 0.8,
    "persons": 0.8,
    "mail": 0.8,
    "phone": 0.8,
    "driving_licence": 0.6,
    "passport": 0.6,
    "cookie": 0.9,
    "location": 0.9,
    "health": 0.9,
    "social_security_number": 0.9,
    "tax_file_number": 0.9,
    "credit_card": 0.9,
}


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
    "--thresh",
    "-tr",
    "thresh",
    type=(str, float),
    multiple=True,
    help="the minimum probability of private data for labels",
)
@click.option(
    "-f",
    "--force",
    "overwrite",
    type=bool,
    is_flag=True,
    default=False,
    help="overwrite existing file",
)
@click.option(
    "--dry-run",
    "dry_run",
    type=bool,
    is_flag=True,
    default=False,
    help="passthrough, will not write anything",
)
def pii_detect(
    input_file: str,
    out_dir: str,
    thresh,
    overwrite: bool = False,
    dry_run: bool = False,
    to_test: bool = False,
):
    """Represents cli 'pii_detect' command"""
    # validate_args(sentence, thresh)
    tresh_dict = dict(thresh)
    thresholds = {
        tag: tresh_dict[tag] if tag in tresh_dict.keys() else threshs[tag]
        for tag in threshs.keys()
    }
    file_name = os.path.basename(input_file).split(".")[0]
    with open(input_file) as f:
        list_sent = [line.rstrip() for line in f]
    text = " ".join(list_sent)
    df = sent_tokenize(text)
    logging.info("loading pipeline")
    pipe = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    logging.info("prediction in progress")
    detected_labels: list = [
        predict(pipe, sent, thresholds) for sent in tqdm(df, total=len(df))
    ]
    logging.info("saving results...")
    out(input_file, out_dir, file_name, detected_labels, dry_run, overwrite, to_test)


if __name__ == "__main__":
    cli()
