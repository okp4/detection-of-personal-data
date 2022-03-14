# Personal Data Detection (PDD)

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


## Foreword
This repository contains a service to retrieve personal data such as first and last names, license plates, phone numbers, emails, postal addresses from DataFrames and return a dictionary of labels that are most often found on the dataframe. 
The labels are: person, emails, address, phones and license_plate.

## Technology

### Nltk
NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.

### RE (Regular Expression)

A regular expression is a method used in programming for pattern matching. Regular expressions provide a flexible and concise means to match strings of text.

## Organization of the repository

The project is organized as follows:
```text

├── README.md
└── src                   
    └── pii.py   

```

## System requirements
### Python

The repository targets python `3.9` and higher.


### Poetry

The repository uses [Poetry](https://python-poetry.org) as python packaging and dependency management. Be sure to have it properly installed before.

```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```


## Local setup

This script runs using Python 3.  Dependencies in the pyproject.toml file can be installed using [Poetry](https://python-poetry.org) :

```sh
poetry install 
```

Next, install [NLTK](https://www.nltk.org/data.html#command-line-installation) Averaged Perceptron Tagger:

```sh
python3 -m nltk.downloader averaged_perceptron_tagger
```

If poetry is not found, use the following command to configure your current shell :

```sh
source $HOME/.poetry/env
```


## How to use

The main script pii.py can be tested, based on the provided file test_file_small_sample.csv, using the following command: 

```sh
poetry run python3 src/test_pii.py
```
