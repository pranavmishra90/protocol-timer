FROM pranavmishra90/singulab:latest

#########################
ARG IMAGE_VERSION="0.0.2"
#########################

LABEL org.opencontainers.image.title="Pranav Mishra's Datascience Image"
LABEL version=${IMAGE_VERSION}}
LABEL org.opencontainers.image.version=${IMAGE_VERSION}}
LABEL org.opencontainers.image.authors='Pranav Kumar Mishra (Rush University)'
LABEL description="A docker image which creates a jupyter notebook environment, version controlled by Datalad, for datascience projects."
LABEL org.opencontainers.image.source="https://gitea.mishracloud.com/Rush/docker-datascience/src/branch/develop/docker/Dockerfile"
LABEL org.opencontainers.image.licenses="MIT WITH BSD-3-Clause-Modification"

ARG NB_USER="coder"
ARG NB_UID="1000"
ARG NB_GID="100"

USER root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update --yes && \
    # - apt-get upgrade is run to patch known vulnerabilities in apt-get packages as
    #   the ubuntu base image is rebuilt too seldom sometimes (less than once a month)
    apt-get install --yes --no-install-recommends \
    # - bzip2 is necessary to extract the micromamba executable.
    ca-certificates \
    sudo \
    # - tini is installed as a helpful container entrypoint that reaps zombie
    #   processes and such of the actual executable we want to start, see
    #   https://github.com/krallin/tini#why-tini for details.
    tini \
    wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

USER ${NB_UID}

# Pin python version here, or set it to "default"
ARG PYTHON_VERSION=3.11.4

# Configure container startup
ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

COPY environment.yml /tmp/environment.yml

# Install Python 3 packages
RUN mamba env create -f /tmp/environment.yml