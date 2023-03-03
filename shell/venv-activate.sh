#!/bin/bash
if [[ -z "$1" ]]; then
    echo "env name not provided"
    return 1
fi

ENV_NAME="$1"

[ -z "$VENVS_BASE_PATH" ] && VENVS_BASE_PATH="$HOME/envs"

if [ ! -d "$VENVS_BASE_PATH" ]; then
  echo "Base envs dir $VENVS_BASE_PATH not found..."
  return 1
fi

source $VENVS_BASE_PATH/$ENV_NAME/bin/activate
