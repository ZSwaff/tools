#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# ZSH setup
export ZSH=/Users/zackswafford/.oh-my-zsh

ZSH_THEME="powerlevel9k/powerlevel9k"
plugins=(git zsh-autosuggestions)

source $ZSH/oh-my-zsh.sh


# Personal additions
DEFAULT_USER=zackswafford
prompt_context(){}

POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(virtualenv context dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status background_jobs history command_execution_time time)
POWERLEVEL9K_SHORTEN_DIR_LENGTH=2
POWERLEVEL9K_SHORTEN_DELIMITER="…"
POWERLEVEL9K_SHORTEN_STRATEGY="truncate_from_right"
POWERLEVEL9K_COMMAND_EXECUTION_TIME_THRESHOLD=5

. ~/.envvars

unset LSCOLORS
export CLICOLOR=1
export CLICOLOR_FORCE=1
autoload -U colors
colors

. ~/.aliases
. ~/.aliases_plenty
. ~/.aliases_kubectl

export PATH=/Users/zackswafford/bin:/Users/zackswafford/Desktop/workspace/plenty-scripts:/Users/zackswafford/Desktop/workspace/plenty-scripts/user_management:$PATH
