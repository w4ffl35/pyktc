# Python Keyword Transposition Cipher

An implementation of a basic keyword transposition cipher in Python.

## Installation

`pip install .`

## Usage

- **Initialize** `from pyktc import Cipher; ktc = Cipher('secret')`
- **Encrypt** `ktc.encrypt('CRYPTOLOGY')`
- **Decrypt** `ktc.decrypt('JHQSU XFXBQ')`

## Limitations

The basic implementation only works with A-Z though it can easily be extended to support other characters.