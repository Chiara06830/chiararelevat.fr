"""
description
"""

import json
from pathlib import Path
from typing import Any, cast
from flask import Flask, render_template
from src.backend.services.native_runner import run_binary

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/teaching")
def teaching():
    teaching_file = (
        Path(__file__).parent / "data" / "teaching2526.json"
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
    education_file = (
        Path(__file__).parent / "data" / "education.json"
    )
    with open(education_file, "r", encoding="utf-8") as f:
        educations: list[dict[str, Any]] = \
            cast(list[dict[str, Any]], json.load(f))

    return render_template("education.html", educations=educations)


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/ocaml")
def ocaml_exec():
    result = run_binary("./bin/helloworld_ocaml.x", "")
    return result["stdout"]


@app.route("/c")
def c_exec():
    result = run_binary("./bin/helloworld_c.x", "")
    return result["stdout"]
