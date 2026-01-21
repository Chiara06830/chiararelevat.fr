## Development

This website is develloped with [Flask](https://flask.palletsprojects.com/).
And it uses [Poetry](https://python-poetry.org/) for handling dependencies.

### Requirement

- Python >= 3

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

## Deployment

The website is deployed thanks to [PythonAnyWhere](https://www.pythonanywhere.com/).

You can find the deployed version on [chiara06830.pythonanywhere.com](https://chiara06830.pythonanywhere.com/).
