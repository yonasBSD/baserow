ARG FROM_IMAGE=baserow/baserow:1.34.2
# This is pinned as version pinning is done by the CI setting FROM_IMAGE.
# hadolint ignore=DL3006
FROM $FROM_IMAGE as image_base

RUN apt-get update \
    && apt-get remove -y postgresql postgresql-contrib redis-server \
    && apt-get clean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY deploy/render/render_env.sh /baserow/supervisor/env/render_env.sh
