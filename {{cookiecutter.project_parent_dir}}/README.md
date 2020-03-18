# {{ cookiecutter.project_slug }}

{{ cookiecutter.description }}
{% if cookiecutter.default_ci_badges == "Y" %}

## Build Status

### GitHub Actions

![Python Test](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Python%20Test/badge.svg)

### Travis CI

[![Build Status](https://travis-ci.org/{{ cookiecutter.travis_username }}/{{ cookiecutter.project_slug }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.travis_username }}/{{ cookiecutter.project_slug }})

{% endif %}

## Requirements

- [requirements.txt](requirements.txt)
- [requirements-dev.txt](requirements-dev.txt)

## Dependencies

## License

{{ cookiecutter.license }}

## Author Information

{{ cookiecutter.author }}

- [@{{ cookiecutter.twitter }}](https://twitter.com/{{ cookiecutter.twitter }})
- [{{ cookiecutter.email }}](mailto:{{ cookiecutter.email }})
- [{{ cookiecutter.website }}]({{ cookiecutter.website }})

> NOTE: Repo has been created/updated using [https://github.com/mrlesmithjr/cookiecutter-python-project](https://github.com/mrlesmithjr/cookiecutter-python-project) as a template.
