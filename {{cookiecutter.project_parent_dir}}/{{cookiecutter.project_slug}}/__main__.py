"""{{cookiecutter.project_slug}}/__main__.py"""
from {{cookiecutter.project_slug}}.cli import cli_args
from {{cookiecutter.project_slug}}.logger import setup_logger


def main():
    """Main execution of package."""

    # Setup root logger
    setup_logger()

    # Capture CLI arguments
    args = cli_args()


if __name__ == '__main__':
    main()
