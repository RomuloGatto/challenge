# They Said Code Challenge
A piece of code to test my skill based on csv, time and itertools packages only. (based on https://gitlab.com/hari22/nuffsaid-coding-challenge)

## Prerequisites

This project has been developed on Windows, to keep the development going on this plataform, you will need to install the following packages/tools below to run everything smooth:
- Python 3.9+: `https://www.python.org/downloads/`
- Poetry: `https://python-poetry.org/docs/#installation`
- Make: `choco install make` after Chocolatey installation completed

## Usage in local development
The `Makefile` file that exists on the project root, has all the commands mapped, from building to testing.

To install all required packages and create a virtual environment:
`$ make setup`

To test all the challenge requirements:
`$ make test`

For other needs, please refer directly to the Makefile file.