
# Personal Data Detection (PDD)

[![PyPI](https://img.shields.io/pypi/v/converter-excel-to-csv)](https://pypi.org/project/converter-excel-to-csv/)[![conventional commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)[![license](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# Purpose

This repository contains detection sensible information service.
The purpose of this service is to detect personal data such as: name, phone, email, mailing address, health information, birth information, passport number, driver's license number, social security number, tax file number, and credit card number of the person.
The input to the service is a text file, i.e. any text file such as .txt, .csv, etc. and returns a json.
The json indicates whether personal information was detected. If so, the json must also contain, for tokens(phrases) that contain personal information, the detected tags(referenced above).

# Technology

# Nltk

NLTK is a leading platform for building Python programs to work with human language data. It provides easy - to - use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial - strength NLP libraries, and an active discussion forum.

# RE (Regular Expression)

A regular expression is a method used in programming for pattern matching. Regular expressions provide a flexible and concise means to match strings of text.

# [Transformers](https://huggingface.co/docs/transformers/index)

State - of - the - art Machine Learning for PyTorch, TensorFlow and JAX.
Transformers provides APIs to easily download and train state - of - the - art pretrained models.

# Usage

The usage is given as follows:

```sh
Usage: main.py pii-detect [OPTIONS]

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

```shell
poetry run python3 src/detection_of_personal_data/main.py pii-detect - tr person 0.3 - tr passport 0.3 - i ./data_test/inputs/personal_data_db.csv - o ./data_test/outputs - f
 ```

## For developers

### Prerequisites

```sh
nltk.download('punkt')
```

#### Python

The repository targets python `3.9` and higher.

#### Poetry

The repository uses [Poetry](https://python-poetry.org) as python packaging and dependency management. Be sure to have it properly installed before.

```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

#### Docker

You can follow the link below on how to install and configure **Docker** on your local machine:

- [Docker Install Documentation](https://docs.docker.com/install/)

### Build

Project is built by [poetry](https://python-poetry.org).

```sh
poetry install
```

### Lint

Code linting is performed by [flake8](https://flake8.pycqa.org).

> ⚠️ Be sure to write code compliant with `flake8` rules or else you'll be rejected by the CI.

```sh
poetry run flake8 --count --show-source --statistics
```

### Unit Test

Unit tests are performed by the [unittest](https://docs.python.org) testing framework.

> ⚠️ Be sure to write tests that succeed or else you'll be rejected by the CI.

```sh
poetry run python -m unittest discover
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

## Contributing

So you want to contribute? Great. We appreciate any help you're willing to give. Don't hesitate to open issues and/or
submit pull requests.
