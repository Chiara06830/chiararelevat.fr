"""
description
"""

import json
from pathlib import Path
from flask import Flask, render_template
from src.backend.services.native_runner import run_binary

app = Flask(__name__)


@app.route("/")
def index():
    """display the main page of the website

    Returns:
        str: HTML of the main page of the website
    """
    return render_template("index.html")


@app.route("/teaching")
def teaching():
    """display the teaching from a json file

    Returns:
        str: HTML of the teaching page
    """
    teaching_file = (
        Path(__file__).parent / "data" / "teaching2526.json"
    )
    with open(teaching_file, "r", encoding="utf-8") as f:
        classes = json.load(f)

    return render_template("teaching.html", classes=classes)


@app.route("/experiences")
def experience():
    """display the experiences from a json file

    Returns:
        str: HTML of the experiences page
    """
    exepriences_file = (
        Path(__file__).parent / "data" / "experiences.json"
    )
    with open(exepriences_file, "r", encoding="utf-8") as f:
        experiences = json.load(f)

    return render_template("experiences.html", experiences=experiences)


@app.route("/education")
def education():
    """display the education from a json file

    Returns:
        str: HTML of the education page
    """
    education_file = (
        Path(__file__).parent / "data" / "education.json"
    )
    with open(education_file, "r", encoding="utf-8") as f:
        educations = json.load(f)

    return render_template("education.html", educations=educations)


@app.route("/projects")
def projects():
    """display the projects from a json file

    Returns:
        str: HTML of the projects page
    """
    academic_projects_file = (
        Path(__file__).parent / "data" / "academic-projects.json"
    )
    with open(academic_projects_file, "r", encoding="utf-8") as f:
        academic_projects = json.load(f)

    categorised_projects: dict[str, list] = {}
    for project in academic_projects:
        if project["diploma"] not in categorised_projects:
            categorised_projects[project["diploma"]] = []
        categorised_projects[project["diploma"]].append(project)

    return render_template("projects.html", projects=categorised_projects)


@app.route("/ocaml")
def ocaml_exec():
    """execute ocaml hello world

    Returns:
        str: the standard output of the hello world program
    """
    result = run_binary("./bin/helloworld_ocaml.x", "")
    return result["stdout"]


@app.route("/c")
def c_exec():
    """execute C hello world

    Returns:
        str: the standard output of the hello world program
    """
    result = run_binary("./bin/helloworld_c.x", "")
    return result["stdout"]
