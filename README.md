## Development

This website is develloped with [Flask](https://flask.palletsprojects.com/).

### Requirement

- Python >= 3

### Installing website

1. Create a python environment

```bash
python3 -m venv .venv
```

2. Activate this environmen

   ```bash
   . .venv/bin/activate
   ```
3. Install Flask and dependencies

   ```bash
   pip install -r requirements.txt
   ```

### Launching website locally

```bash
. .venv/bin/activate
flask --app app run --debug
```

The server will be running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Deployment

The website is deployed thanks to [PythonAnyWhere](https://www.pythonanywhere.com/).

You can find the deployed version on [chiara06830.pythonanywhere.com](https://chiara06830.pythonanywhere.com/).
