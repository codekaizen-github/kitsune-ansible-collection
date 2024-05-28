FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC
ENV LANGUAGE=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y \
    software-properties-common \
    python3-pip \
    curl

RUN apt-add-repository -y ppa:ansible/ansible

RUN apt-get update && apt-get install -y \
    ansible

# https://tomgregory.com/aws/running-docker-in-docker-on-windows/
RUN curl -sSL https://get.docker.com/ | sh

# Copy the rest of the files
COPY ./ /workspace
