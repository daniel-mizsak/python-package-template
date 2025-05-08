# Set basic image data
ARG BASE_IMAGE_NAME=python
ARG BASE_IMAGE_TAG=3.12
FROM ${BASE_IMAGE_NAME}:${BASE_IMAGE_TAG}
LABEL maintainer="Daniel Mizsak"

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV TZ=Europe/Copenhagen

WORKDIR /workspace

# APT: Install linux utilities
# hadolint ignore=DL3008
RUN apt-get update --quiet --quiet --yes \
 && apt-get install --no-install-recommends --quiet --quiet --yes \
 build-essential \
 curl \
 git \
 && apt-get clean --quiet --quiet \
 && rm --recursive --force /var/lib/apt/lists/* \
 && rm --recursive --force /tmp/* \
 && rm --recursive --force /var/tmp/*
