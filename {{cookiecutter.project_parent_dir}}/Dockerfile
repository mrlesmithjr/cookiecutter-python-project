ARG VARIANT=3.8
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

# [Option] Install Node.js
ARG INSTALL_NODE="false"
ARG NODE_VERSION="lts/*"
RUN if [ "${INSTALL_NODE}" = "true" ]; then su vscode -c "source /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi
COPY requirements*.txt .
RUN pip install -r requirements.txt -r requirements-dev.txt \
    && pip install pre-commit
