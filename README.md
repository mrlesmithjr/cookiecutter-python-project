# Cookiecutter - Python Project

A cookiecutter project template for Python Projects. By using [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/),
consistent Python projects can be achieved with common constructs. Many great
projects already use cookiecutter behind the scenes (Ansible, Molecule).

## Requirements

- [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

## Usage

Execute the following and answer the relevant questions.

```bash
cookiecutter https://github.com/mrlesmithjr/cookiecutter-python-project
```

### Example

In this example we will create an example project named `MyExample`.

```bash
cookiecutter https://github.com/mrlesmithjr/cookiecutter-python-project
```

```bash
project_name [Enter Python project name]: MyExample
project_parent_dir [myexample]:
project_slug [myexample]:
description [Enter description of project]: My Example Project
version [0.1.0]:
author [Your Name]: Larry Smith Jr.
company [Enter company name]: Example
email [me@example.com]: mrlesmithjr@gmail.com
website [http://example.com]:
twitter [example]: mrlesmithjr
Select license:
1 - MIT
2 - BSD-3
3 - Apache Software License 2.0
Choose from 1, 2, 3 [1]: 1
year [2020]: 2021
github_username [mrlesmithjr]:
gitlab_username [mrlesmithjr]:
travis_username [mrlesmithjr]:
Select default_ci_badges:
1 - Y
2 - N
Choose from 1, 2 [1]:
```

Once the above is completed our new `myexample` directory will look similar to:

```bash
ls -la
...
total 152
drwxr-xr-x  24 smithlar  staff    768 Mar 29 10:37 .
drwxr-xr-x   4 smithlar  staff    128 Mar 29 10:37 ..
-rw-r--r--   1 smithlar  staff     25 Mar 29 10:37 .flake8
drwxr-xr-x   3 smithlar  staff     96 Mar 29 10:37 .github
-rw-r--r--   1 smithlar  staff   2112 Mar 29 10:37 .gitignore
-rw-r--r--   1 smithlar  staff    268 Mar 29 10:37 .gitlab-ci.yml
-rw-r--r--   1 smithlar  staff    212 Mar 29 10:37 .travis.yml
-rw-r--r--   1 smithlar  staff    617 Mar 29 10:37 .yamllint
-rw-r--r--   1 smithlar  staff      0 Mar 29 10:37 CHANGELOG.md
-rw-r--r--   1 smithlar  staff   3356 Mar 29 10:37 CODE_OF_CONDUCT.md
-rw-r--r--   1 smithlar  staff    372 Mar 29 10:37 CONTRIBUTING.md
-rw-r--r--   1 smithlar  staff     40 Mar 29 10:37 CONTRIBUTORS.md
-rw-r--r--   1 smithlar  staff   1072 Mar 29 10:37 LICENSE.md
-rw-r--r--   1 smithlar  staff    953 Mar 29 10:37 README.md
drwxr-xr-x   4 smithlar  staff    128 Mar 29 10:37 docs
-rw-r--r--   1 smithlar  staff     21 Mar 29 10:37 mkdocs.yml
drwxr-xr-x   8 smithlar  staff    256 Mar 29 10:37 myexample
-rw-r--r--   1 smithlar  staff  16636 Mar 29 10:37 pylintrc
-rw-r--r--   1 smithlar  staff    104 Mar 29 10:37 requirements-dev.in
-rw-r--r--   1 smithlar  staff      0 Mar 29 10:37 requirements-dev.txt
-rw-r--r--   1 smithlar  staff     36 Mar 29 10:37 requirements.in
-rw-r--r--   1 smithlar  staff      0 Mar 29 10:37 requirements.txt
-rw-r--r--   1 smithlar  staff    164 Mar 29 10:37 setup.py
drwxr-xr-x   3 smithlar  staff     96 Mar 29 10:37 tests
```

## Licensing

The current licensing model is MIT by default.

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
