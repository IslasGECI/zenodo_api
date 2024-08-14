FROM python:3.11
WORKDIR /workdir
COPY . .
ENV PATH="/root/.local/lib/shellspec:$PATH"
RUN pip install --upgrade pip && pip install \
    batcat \
    black \
    flake8 \
    mutmut \
    mypy \
    pylint \
    pytest \
    pytest-cov

RUN apt update && apt full-upgrade && apt install --yes \
    jq

# Instala ShellSpec
RUN src/install_shellspec.sh

