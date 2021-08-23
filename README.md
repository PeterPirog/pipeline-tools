# Hello World

This is an example project demonstaraing how to publish a python module to PyPI

## Installation

Run the following to install:
```bash
$ pip install helloworld
```

## Usage

```python
from pipeline_tools import say_hello

# Generate "Hello World!
say_hello()

# Generate "Hello Everybody"
say_hello("Everybody")
```
#Developing Hello World
To install helloworld, along the tools you need to develop and run tests, run the following in your virtualenv:
```bash
$ pip install -e .[dev]
```