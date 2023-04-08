#!/bin/bash

# This script is used to complete the shell command


# Dummy autocomplete function
autocomplete() {
    local command_so_far=$1
    local possible_completion="ls -l"  # TODO: replace with real completion
    printf "$possible_completion"
}



record_history() {
    # this function records the command history with the current directory the command was executed in
    local current_directory=$PWD
    local command_so_far=$1
    echo "$current_directory $command_so_far" >> history.txt
}    