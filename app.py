"""
description
"""

import json
from pathlib import Path
from typing import Any, cast
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/teaching")
def teaching():
    teaching_file = (
        Path(__file__).parent / "data" / "istic_25_26.json"
    )
    with open(teaching_file, "r", encoding="utf-8") as f:
        classes: list[dict[str, Any]] = \
            cast(list[dict[str, Any]], json.load(f))

    return render_template("teaching.html", classes=classes)


@app.route("/experiences")
def experiences():
    exepriences_file = (
        Path(__file__).parent / "data" / "experiences.json"
    )
    with open(exepriences_file, "r", encoding="utf-8") as f:
        experiences: list[dict[str, Any]] = \
            cast(list[dict[str, Any]], json.load(f))

    return render_template("experiences.html", experiences=experiences)


@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")
