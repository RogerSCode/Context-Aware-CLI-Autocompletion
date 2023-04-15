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



read_input() {
  
  text=""

  while true
   do
    # Read a single character
    tmp= $IFS
    IFS="\n"
    read -r -s -n 1 key
    IFS= $tmp

    if [[ $key = "" ]]; then
      printf "\n"
      eval "$text"
      break
    elif [[ $key = $'\x7f' ]]; then
      # If the character is a backspace, remove the last character from the text string
      text=${text%?}
      printf '\b \b'
    else
      # Add the character to the text string and print it to the screen
      text+=$key
      printf "$key"
    fi
  done

}

read_input