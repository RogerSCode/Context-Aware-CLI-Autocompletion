#!/bin/bash

# This script is used to complete the shell command


# Dummy autocomplete function
autocomplete() {
    local command_so_far=$1
    local possible_completion=$(python3 autocomplete.py "$command_so_far") #TODO check if python3 is correct command to call python 
    printf "${command_so_far}${possible_completion}"
}

record_history() {
    # this function records the command history with the current directory the command was executed in
    local current_directory=$PWD
    local command_so_far=$1
    echo "$current_directory $command_so_far" >> history.txt
}    

read_key() {
    # This function reads a single character from the keyboard
    local key
    local tmp=$IFS
    IFS="\n"
    read -r -s -n 1 key
    
  
    IFS=$tmp

    echo "$key"
}

execute_command(){
  printf "\n" >&2
  eval "$text" 
  # history should only be recorded if the command was executed successfully 
  #cuz it would not make sense to let the ai learn incorrect commands.

  if [[ $? -ne 0 ]]; then
    printf "Error: command not found: $text" >&2
    printf "\n" >&2
  else

    record_history "$text"
  fi
  
      
}

function clearline() {
    echo -ne "\033[2K\r"
}


display_prompt(){
  # This function displays the current directory and the prompt
    clearline >&2
    printf "%s> " "$PWD" >&2
    printf "$text"  >&2
}

read_input() {
  
  text=""
  
  while true
   do

    # Display the current directory and prompt
    display_prompt

    # Read a single character
    key=$(read_key)
    
    if [[ $key = "" ]]; then
      execute_command
      text=""
    elif [[ $key = $'\x7f' ]]; then
      # If the character is a backspace, remove the last character from the text string
      text=${text%?}
      printf '\b \b'
    elif [[ $key = $'\x09' ]]; then
      # If the character is a tab, complete the command
      text=$(autocomplete "$text")
      clearline
      printf "$text"
    elif [[ "$key" == $'\x1b' ]]; then
    read -rsn 2 key
    case "$key" in
      '[A') key="up" ;;
      '[B') key="down" ;;
      '[C') key="right" ;;
      '[D') key="left" ;;
      *) key="unknown" ;;
    esac
    else
      # Add the character to the text string and print it to the screen
      text+=$key
      printf "$key"
    fi
  done

}

read_input

