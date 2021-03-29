ARG VARIANT=bionic

FROM ubuntu:${VARIANT} AS builder

LABEL maintainer="{{cookiecutter.email}}"

ARG DEFAULT_PYTHON_VERSION=3.9.1
ARG USER_GID=1000
ARG USER_UID=1000
ARG USERNAME=vscode

ENV LC_ALL="C.UTF-8"
ENV LANG="C.UTF-8"
ENV PYENV_ROOT="/home/$USERNAME/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PATH"
ENV SHELL="/bin/bash"

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

RUN apt-get install -y build-essential curl git libbz2-dev libffi-dev \
    libreadline-dev libsqlite3-dev libssl-dev zlib1g-dev

USER $USERNAME

COPY requirements.txt .
COPY requirements-dev.txt .

RUN git clone https://github.com/pyenv/pyenv.git "$PYENV_ROOT" \
    && pyenv install "$DEFAULT_PYTHON_VERSION" \
    && pyenv global "$DEFAULT_PYTHON_VERSION" \
    && eval "$(pyenv init -)" \
    && pip install --upgrade pip pip-tools \
    && pip-sync requirements.txt requirements-dev.txt \
    && echo 'eval "$(pyenv init -)"' >> "/home/$USERNAME/.bashrc"

FROM ubuntu:${VARIANT}

LABEL maintainer="{{cookiecutter.email}}"

ARG USER_GID=1000
ARG USER_UID=1000
ARG USERNAME=vscode

ENV LC_ALL="C.UTF-8"
ENV LANG="C.UTF-8"
ENV PYENV_ROOT="/home/$USERNAME/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PATH"
ENV SHELL="/bin/bash"

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y git sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && echo 'eval "$(pyenv init -)"' >> "/home/$USERNAME/.bashrc"

USER $USERNAME

COPY --from=builder $PYENV_ROOT $PYENV_ROOT
