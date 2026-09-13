import os
import textwrap
from math import floor

# Terminal centering code from Bill A Brown (2023), https://medium.com/@bill.a.brown90/cli-formatting-center-text-in-terminal-6d476cf7d148
# With slight modifications
terminal_size = os.get_terminal_size()
terminal_width = terminal_size[0]

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