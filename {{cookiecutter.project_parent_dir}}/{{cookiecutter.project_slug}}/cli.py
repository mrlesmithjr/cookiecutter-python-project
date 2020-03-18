"""{{cookiecutter.project_slug}}/cli.py"""

import argparse
from {{cookiecutter.project_slug}}.release import __package_name__, __version__


def cli_args():
    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version',
                        version=f'{__package_name__} {__version__}')
    args = parser.parse_args()

    return args
