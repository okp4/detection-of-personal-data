
# Detection Of Personal data

[![version](https://img.shields.io/github/v/release/okp4/detection-of-personal-data?style=for-the-badge&logo=github)](https://github.com/okp4/detection-of-personal-data/releases)[![lint](https://img.shields.io/github/workflow/status/okp4/detection-of-personal-data/Lint?label=lint&style=for-the-badge&logo=github)](https://github.com/okp4/detection-of-personal-data/actions/workflows/lint.yml)[![build](https://img.shields.io/github/workflow/status/okp4/detection-of-personal-data/Build?label=build&style=for-the-badge&logo=github)](https://github.com/okp4/detection-of-personal-data/actions/workflows/build.yml)[![test](https://img.shields.io/github/workflow/status/okp4/detection-of-personal-data/Test?label=test&style=for-the-badge&logo=github)](https://github.com/okp4/detection-of-personal-data/actions/workflows/test.yml)
[![codecov](https://img.shields.io/codecov/c/github/okp4/detection-of-personal-data?style=for-the-badge&token=G5OBC2RQKX&logo=codecov)](https://codecov.io/gh/okp4/detection-of-personal-data)
[![conventional commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=for-the-badge&logo=conventionalcommits)](https://conventionalcommits.org)
[![contributor covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg?style=for-the-badge)](https://github.com/okp4/.github/blob/main/CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg?style=for-the-badge)](https://opensource.org/licenses/BSD-3-Clause)

## Purpose

This repository contains detection sensible information service.
The purpose of this service is to detect personal data such as: name, phone, email, mailing address, health information, birth information, passport number, driver's license number, social security number, tax file number, and credit card number of the person.
The input to the service is a text file, i.e. any text file such as .txt, .csv, etc. and returns a json.
The json indicates whether personal information was detected. If so, the json must also contain, for tokens(phrases) that contain personal information, the detected tags(referenced above).

## Technology

### Nltk

NLTK is a leading platform for building Python programs to work with human language data. It provides easy - to - use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial - strength NLP libraries, and an active discussion forum.

### RE (Regular Expression)

A regular expression is a method used in programming for pattern matching. Regular expressions provide a flexible and concise means to match strings of text.

### [Transformers](https://huggingface.co/docs/transformers/index)

State-of-the-art Machine Learning for PyTorch, TensorFlow and JAX.
Transformers provides APIs to easily download and train state-of-the-art pretrained models.

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

## What's included

This template provides the following:

- [poetry](https://python-poetry.org) for dependency management.
- [flake8](https://flake8.pycqa.org) for linting python code.
- [mypy](http://mypy-lang.org/) for static type checks.
- [pytest](https://docs.pytest.org) for unit testing.
- [click](https://palletsprojects.com/p/click/) to easily setup your project commands

The project is also configured to enforce code quality by declaring some CI workflows:

- conventional commits
- lint
- unit test
- semantic release

## Everyday activity

### Build

Project is built by [poetry](https://python-poetry.org).

```sh
poetry install
```

### Usage

```sh
poetry run detection-of-personal-data --help
```

Will give something like

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
poetry run detection-of-personal-data pii-detect -tr person 0.3 -tr passport 0.3 -i ./tests/data/inputs_test/text -o ./tests/data/outputs -f
```

### Lint

> ⚠️ Be sure to write code compliant with linters or else you'll be rejected by the CI.

**Code linting** is performed by [flake8](https://flake8.pycqa.org).

```sh
poetry run flake8 --count --show-source --statistics
```

**Static type check** is performed by [mypy](http://mypy-lang.org/).

```sh
poetry run mypy .
```

To improve code quality, we use other linters in our workflows, if you don't want to be rejected by the CI,
please check these additional linters.

**Markdown linting** is performed by [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli).

```sh
markdownlint "**/*.md"
```

**Docker linting** is performed [hadolint](https://github.com/hadolint/hadolint).

```sh
hadolint Dockerfile
```

### Unit Test

> ⚠️ Be sure to write tests that succeed or else you'll be rejected by the CI.

Unit tests are performed by the [pytest](https://docs.pytest.org) testing framework.

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
