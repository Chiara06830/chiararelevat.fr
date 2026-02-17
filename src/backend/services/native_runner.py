"""
Module to execute native binary code
"""

import subprocess


def __run_command(command: str):
    try:
        result = subprocess.run(
            command.split(),
            capture_output=True,
            text=True,
            timeout=3,  # évite blocage
            check=False
        )

        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": str(result.returncode),
            "executed_line": command
        }

    except subprocess.TimeoutExpired:
        return {"error": "Timeout"}


def run_binary(path: str, args: str = "") -> dict[str, str]:
    """Run any binary with its arguments

    Args:
        path (str): path of binary to execute
        args (str): argument to provide to binary source

    Returns:
        dict[str, str]: dict of all the output of the program
    """
    line: str = path + " " + args
    return __run_command(line)


def compile_single_file_c(path: str) -> dict[str, str]:
    """Compile a file in and gnerate the excutable in bin/

    Args:
        path (str): path of the file to compile

    Returns:
        dict[str, str]: dict of all the output of the compilation
    """
    executable_path: str = "bin/" + path.split("/")[-1].replace(".c", ".x")
    line: str = "gcc " + path + " -Wall " + " -Wextra " + " -pedantic " + " -std=c99"\
        + " -g " + " -o" + executable_path
    return __run_command(line)


def compile_single_file_ocaml(path: str) -> dict[str, str]:
    """Compile a ml file in and gnerate the excutable in bin/

    Args:
        path (str): path of the file to compile

    Returns:
        dict[str, str]: dict of all the output of the compilation
    """
    executable_path: str = "bin/" + path.split("/")[-1].replace(".ml", ".x")
    line: str = "ocamlc " + path + " -o " + executable_path
    result = __run_command(line)

    subprocess.run(
        ["rm", "-f", "src/ocaml/*.cmi", "src/ocaml/*.cmo"],
        capture_output=True,
        text=True,
        timeout=3,  # évite blocage
        check=False
    )

    return result
