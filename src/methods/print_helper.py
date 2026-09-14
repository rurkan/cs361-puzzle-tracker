import os
import textwrap
from math import floor

# Terminal centering code from Bill A Brown (2023), https://medium.com/@bill.a.brown90/cli-formatting-center-text-in-terminal-6d476cf7d148
# With slight modifications
terminal_size = os.get_terminal_size()
terminal_width = terminal_size[0]

def printwrap(line):
  print(textwrap.fill(line, width = floor(terminal_width*9/10)))

# Spacer modification by me, to make center printed errors stand out
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
    
    
def incomplete_screen(screen_name):
  centerprint_string("DISPLAY "+screen_name+" SCREEN, INCOMPLETE", "-")
  

  
def replace(line, data, modifier):
  modifier_loc = line.find(modifier)
  if(data is not None):
    return(line[:modifier_loc]+data+line[modifier_loc+len(modifier):])
  else:
    placeholder = ("NullUser" if modifier == "$username" else "")
    return(line[:modifier_loc]+placeholder+line[modifier_loc+len(modifier):])
  
def apply_replacements(line, modifiers, error = None, username = None):
  if "$error" in modifiers:
    line = replace(line, error, "$error")
  if "$username" in modifiers:
    line = replace(line, username, "$username")
  return line

def print_with_modifiers(line, modifiers, error = None, username = None):
  line = apply_replacements(line, modifiers, error, username)
  if "-" in modifiers or ("$error" in modifiers and error != None):
    centerprint_string(line, "-")
    return
  if " " in modifiers:
    centerprint_string(line)
    return
  if ">" in modifiers:
    userin = "__INVALID__"
    while not userin.isalnum():
      userin = input(line[1:])
    return userin
    # centerprint_string(line, ">")
    # Currently don't have the actual verison of this implemented
    return
  print(line)
  



