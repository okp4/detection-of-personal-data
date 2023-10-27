
# Detection Of Personal data

[![version](https://img.shields.io/github/v/release/okp4/detection-of-personal-data?style=for-the-badge&logo=github)](https://github.com/okp4/detection-of-personal-data/releases)[![lint](https://img.shields.io/github/actions/workflow/status/okp4/detection-of-personal-data/lint.yml?branch=main&label=lint&style=for-the-badge&logo=github)](https://github.com/okp4/detection-of-personal-data/actions/workflows/lint.yml)[![build](https://img.shields.io/github/actions/workflow/status/okp4/detection-of-personal-data/build.yml?branch=main&label=build&style=for-the-badge&logo=github)](https://github.com/okp4/detection-of-personal-data/actions/workflows/build.yml)[![test](https://img.shields.io/github/actions/workflow/status/okp4/detection-of-personal-data/test.yml?branch=main&label=test&style=for-the-badge&logo=github)](https://github.com/okp4/detection-of-personal-data/actions/workflows/test.yml)
[![codecov](https://img.shields.io/codecov/c/github/okp4/detection-of-personal-data?style=for-the-badge&token=G5OBC2RQKX&logo=codecov)](https://codecov.io/gh/okp4/detection-of-personal-data)
[![conventional commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=for-the-badge&logo=conventionalcommits)](https://conventionalcommits.org)
[![contributor covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg?style=for-the-badge)](https://github.com/okp4/.github/blob/main/CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg?style=for-the-badge)](https://opensource.org/licenses/BSD-3-Clause)

## Purpose

`detection-of-personal-data` is a CLI tool to detect sensitive personal data, including names, contact information, health details, identification numbers, and financial details.

Users can input a variety of text files (e.g., `.txt`, `.csv`) which the service then processes, returning a JSON. The JSON not only indicates the presence of personal information but also provides tags for the detected data.

## Technology

### Nltk

NLTK is a leading platform for building Python programs to work with human language data. It provides easy - to - use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial - strength NLP libraries, and an active discussion forum.

### RE (Regular Expression)

A regular expression is a method used in programming for pattern matching. Regular expressions provide a flexible and concise means to match strings of text.

### [Transformers](https://huggingface.co/docs/transformers/index)

State-of-the-art Machine Learning for PyTorch, TensorFlow and JAX.
Transformers provides APIs to easily download and train state-of-the-art pretrained models.

### Usage

Retrieve command help with:

```sh
poetry run detection-of-personal-data pii-detect --help
```

```console
Usage: detection-of-personal-data pii-detect [OPTIONS]

  Represents cli 'pii_detect' command

Options:
  -i, --input TEXT               path to text file  [required]
  -o, --output TEXT              output directory where json file will be
                                 written  [default: .]
  -tr, --thresh <TEXT FLOAT>...  the minimum probability of private data for
                                 labels
  -f, --force                    overwrite existing file
  --dry-run                      passthrough, will not write anything
  --help                         Show this message and exit.
```

Example:

```sh
poetry run detection-of-personal-data pii-detect \
  -tr person 0.3 \
  -tr passport 0.3 \
  -i ./tests/data/inputs_test/text \
  -o ./tests/data/outputs -f
```

## System requirements

### Python

The repository targets python `3.9` and higher.

### Poetry

The repository uses [Poetry](https://python-poetry.org) as python packaging and dependency management. Be sure to have it properly installed before.

```sh
curl -sSL https://install.python-poetry.org | python3
```

#### Docker

You can follow the link below on how to install and configure **Docker** on your local machine:

- [Docker Install Documentation](https://docs.docker.com/install/)

## Everyday activity

### Build

Project is built by [poetry](https://python-poetry.org). Initialize the project using:

```sh
poetry install
```

### Quality Assurance

> ⚠️ Ensure your code complies with our linters to pass CI checks.

**Code linting** is performed by [flake8](https://flake8.pycqa.org).

```sh
poetry run flake8 --count --show-source --statistics
```

**Static type check** is performed by [mypy](http://mypy-lang.org/).

```sh
poetry run mypy .
```

To improve code quality, we use other linters in our workflows, if you want them to succeed in the CI,
please check these additional linters.

**Markdown linting** is performed by [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli).

```sh
markdownlint "**/*.md"
```

**Docker linting** is performed [hadolint](https://github.com/hadolint/hadolint).

```sh
hadolint Dockerfile
```

#### Unit Testing

> ⚠️ Be sure to write tests that succeed to pass CI checks.

Unit testing is performed by the [pytest](https://docs.pytest.org) testing framework.

```sh
poetry run pytest -v
```

### Build & run docker image (locally)

Build a local docker image using the following command line:

```sh
docker build -t detection-of-personal-data .
```

Once built, you can run the container locally with the following command line:

```sh
docker run -ti --rm detection-of-personal-data
```

## You want to get involved? 😍

Please check out OKP4 health files :

- [Contributing](https://github.com/okp4/.github/blob/main/CONTRIBUTING.md)
- [Code of conduct](https://github.com/okp4/.github/blob/main/CODE_OF_CONDUCT.md)
