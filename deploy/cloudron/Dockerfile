ARG FROM_IMAGE=baserow/baserow:1.34.2
# This is pinned as version pinning is done by the CI setting FROM_IMAGE.
# hadolint ignore=DL3006
FROM $FROM_IMAGE as image_base

# We need to move the conf at build time due to cloudrons readonly filesystem.
RUN apt-get remove -y "postgresql-$POSTGRES_VERSION" && \
    mv /baserow/supervisor/includes/disabled/embedded-redis.conf /baserow/supervisor/includes/enabled/embedded-redis.conf

COPY deploy/cloudron/cloudron_env.sh /baserow/supervisor/env/cloudron_env.sh
