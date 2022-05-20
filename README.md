![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) 
[![PyPI](https://img.shields.io/pypi/v/converter-excel-to-csv)](https://pypi.org/project/converter-excel-to-csv/) [![conventional commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org) [![license](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
# Personal Data Detection (PDD)

## Purpose
This repository contains detection sensible information service.
The purpose of this service is to detect personal data such as: name, phone, email, mailing address, health information, birth information, passport number, driver's license number, social security number, tax file number, and credit card number of the person. The input to the service is a text file, i.e. any text file such as .txt, .csv, etc. and returns a json. 
The json indicates whether personal information was detected. If so, the json must also contain, for tokens (phrases) that contain personal information, the detected tags (referenced above).
## Technology

### Nltk
NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.

### RE (Regular Expression)

A regular expression is a method used in programming for pattern matching. Regular expressions provide a flexible and concise means to match strings of text.

### [Transformers](https://huggingface.co/docs/transformers/index)
State-of-the-art Machine Learning for PyTorch, TensorFlow and JAX.
Transformers provides APIs to easily download and train state-of-the-art pretrained models. 


## Usage

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
 poetry run python3 src/main.py pii-detect -tr person 0.3 -tr passport 0.3 -i ./data_test/inputs/personal_data_db.csv -o ./data_test/outputs -f 
 ```

## System requirements
### Python

The repository targets python `3.9` and higher.
```sh
import nltk
nltk.download('punkt')
```
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
