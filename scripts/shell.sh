#!/usr/bin/env bash

DOCKER_COMPOSE=./scripts/docker-compose-dev.sh
DOCKER_COMPOSE_SERVICE=app

start_time="$(date +%s)"
grace_period=2 # seconds

if [[  $# -eq 0 ]]; then
    # the extra environment variables helps on not messing up the history search in bash
    $DOCKER_COMPOSE exec \
		    -e COLUMNS="$(tput cols)" \
		    -e LINES="$(tput lines)" \
		    $DOCKER_COMPOSE_SERVICE \
		    /bin/bash -i
else
    $DOCKER_COMPOSE exec $DOCKER_COMPOSE_SERVICE $@
fi

# capture the exit code of the docker-compose command
exit_code=$?

# mention the hint about the running container if the command failed within the "grace period"
if [[ $exit_code -ne 0 ]] && (( ($start_time + $grace_period) > $(date +%s) )); then
    echo "Are you sure that the app container is running? (exit code: $exit_code)"
    exit $?
fi
