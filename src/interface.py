# Commit number 2 for Assignment 2
# ohhhh slight changes very scary 
import os
import textwrap
import chess
from math import floor


# Code for clearing screen across OS from stackoverflow:
# Source - https://stackoverflow.com/a/5369197
# Posted by Acorn, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-13, License - CC BY-SA 4.0

import subprocess
import os

if os.name == 'nt':
    def clearscreen():
        subprocess.call("cls", shell=True)
        return
else:
    def clearscreen():
        subprocess.call("clear", shell=True)
        return

# End stackoverflow post


# Terminal centering code from Bill A Brown (2023), https://medium.com/@bill.a.brown90/cli-formatting-center-text-in-terminal-6d476cf7d148
# With slight modifications
terminal_size = os.get_terminal_size()
terminal_width = terminal_size[0]

# Overloading modification of method for my personal sake
def print_centered(string_in, spacer):

  input_length = len(string_in)
  empty_space_requried = int((terminal_width-input_length)/2)
  empty_space = spacer * empty_space_requried
  print(empty_space + string_in + empty_space)

# End centering code from Bill


def centerprint_string(string_in, spacer = None):
  if(spacer is None):
    spacer = " "
  input_length = len(string_in)
  
  if(input_length>terminal_width):
    strings = textwrap.wrap(string_in, width = floor(terminal_width*9/10))
    for string in strings:
      print_centered(string, spacer)
  else:
    print_centered(string_in, spacer)


def display_screen(lines, error = None):
  clearscreen()
  for line in lines[1:]:
    # If the line isn't blank and starts with a space, center it
    # Easiest was I could think of to designate if something should be centerd
    if(len(line) != 0 and line[0] == ' '):
      if(line[1:] == "error"):
        if(error is not None):
          centerprint_string(error, "-")
      else:
        centerprint_string(line[1:])
    else:
      print(line)
  return(input("Option Select: "))


def get_screen_input(filepath):

  file = open(filepath, 'r', encoding='utf-8')
  lines = file.read().splitlines()
  file.close()
  
  options = lines[0].split()
  userin = display_screen(lines)
  while userin.lower() not in options:
    userin = display_screen(lines, "PLEASE INPUT A SELECTION FROM THE OPTIONS AVAILABLE")
  return userin
  

  


def login_screen():
  userin = get_screen_input("src/screens/login_screen.txt")
  print("You selected: "+str(userin))
  

def main():
  login_screen()


main()