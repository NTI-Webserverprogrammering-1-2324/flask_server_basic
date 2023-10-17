FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    pandoc \
    texlive-xetex \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    flask \
    jupyter \
    nbconvert

WORKDIR /workspace
