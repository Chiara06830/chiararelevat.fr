## Development

This website is develloped with [Flask](https://flask.palletsprojects.com/).

### Requirement

- Python >= 3

### First time launching website

1. Create a python environment

```bash
python3 -m venv .venv
```

2. Activate this environmen

   ```bash
   . .venv/bin/activate
   ```
3. Install Flask

   ```bash
   pip install Flask
   ```

### Launching the website locally

```bash
flask --app app run
```

The server will be running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
