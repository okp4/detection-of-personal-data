# Personal Data Detection (PDD)

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


## Foreword
This repository contains a service to detect personal data such as: name, phone, email, mailing address, health information, birth information, passport number, driver's license number, social security number, tax file number, and credit card number of the person. The input to the service is a text file, i.e. any text file such as .txt, .csv, etc. and returns a json. 
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
ﬂ
  Represents cli 'pii_detect' command

Options:
  -i, --input TEXT     path to text file  [required]
  -o, --output TEXT    output directory where json file will be written
                       [default: .]
  -tr, --thresh FLOAT  the minimum probability of private data [default: 0.9]
  --help               Show this message and exit.

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
