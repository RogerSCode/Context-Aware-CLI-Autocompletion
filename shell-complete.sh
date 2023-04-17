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

read_key() {
    local key
    local tmp=$IFS
    IFS="\n"
    read -r -s -n 1 key
    IFS=$tmp
    echo "$key"
}

read_input() {
  
  text=""
  
  while true
   do

    # Read a single character
    key=$(read_key)



    if [[ $key = "" ]]; then
      printf "\n"
      record_history "$text" # record the command history
      eval "$text"
      text=""
    elif [[ $key = $'\x7f' ]]; then
      # If the character is a backspace, remove the last character from the text string
      text=${text%?}
      printf '\b \b'
    elif [[ $key = $'\x09' ]]; then
      # If the character is a tab, complete the command
      text=$(autocomplete "$text")
      printf "$text"
    else
      # Add the character to the text string and print it to the screen
      text+=$key
      printf "$key"
    fi
  done

}

read_input