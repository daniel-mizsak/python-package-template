ARG BASE_IMAGE=python:3.12
FROM ${BASE_IMAGE}
LABEL maintainer="Daniel Mizsak"

ARG USER=vscode
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV TZ=Europe/Copenhagen

RUN apt update --quiet --quiet --yes && \
    apt install --no-install-recommends --quiet --quiet --yes \
    build-essential \
    curl \
    git && \
    apt clean --quiet --quiet && \
    rm --recursive --force /var/lib/apt/lists/* && \
    rm --recursive --force /tmp/*

WORKDIR /workspace
