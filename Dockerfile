FROM python:3.7.2-slim-stretch

# TODO: Analyzer specific packages below

# Setup analysis user for docker
RUN groupadd -r analysis && useradd -m --no-log-init --gid analysis analysis
USER analysis
COPY src /analyzer


# Setup entrypoint into the analysis code logic
WORKDIR /
CMD ["/analyzer/analyze.sh"]