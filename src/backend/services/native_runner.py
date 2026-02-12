"""
Module to execute native binary code
"""

import subprocess


def run_binary(path: str, args: str) -> dict[str, str]:
    """Run any binary with its arguments

    Args:
        path (str): path of binary to execute
        args (str): argument to provide to binary source

    Returns:
        dict[str, str]: dict of all the output of the program
    """
    try:
        result = subprocess.run(
            [path, args],
            capture_output=True,
            text=True,
            timeout=3,  # évite blocage
            check=False
        )

        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": str(result.returncode)
        }

    except subprocess.TimeoutExpired:
        return {"error": "Timeout"}
    except Exception as e:
        return {"error": str(e)}
