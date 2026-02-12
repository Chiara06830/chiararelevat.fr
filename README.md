## Development

This website is develloped with [Flask](https://flask.palletsprojects.com/).
And it uses [Poetry](https://python-poetry.org/) for handling dependencies.

### Installing website

1. Check you have poetry installed
```
poetry --version
```

2. Install dependencies
```
poetry install
```

### Launching website locally

```bash
poetry run flask --app app run --debug
```

The server will be running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Testing packages
```bash
poetry run python3 -m pytest test
```

## Deployment

The website is deployed thanks to [PythonAnyWhere](https://www.pythonanywhere.com/).

You can find the deployed version on [chiara06830.pythonanywhere.com](https://chiara06830.pythonanywhere.com/).

## Write module in C or Ocaml
There is a setup that allow execute code written in C and Ocaml.
The `src` file has three packages, one for python, one for c and one for ocaml.

To compile c code run
```
make c
```
To compile ocaml run 
```
make ocaml
```

Then binaries can be run with 
```python
from src.backend.services.native_runner import run_binary
run_binary("./bin/helloworld_ocaml.x", "")
```
