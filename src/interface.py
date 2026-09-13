# Commit number 2 for Assignment 2
# ohhhh slight changes very scary 
import os
import textwrap
import chess
from math import ceil, floor

# Test Strings
char54 = "this is an extra long string that is 54 chars long wow"
char50 = "this is a long string that is 50 chars long thanks"
char48 = "this is a long string that is 48 chars long yay!"
char46 = "this is a long string that is 46 chars long :)"

# strings = [char46, char48, char50, char54]
# for mystr in strings:
#   print(len(mystr))

# Terminal centering code from Bill A Brown (2023), https://medium.com/@bill.a.brown90/cli-formatting-center-text-in-terminal-6d476cf7d148
terminal_size = os.get_terminal_size()
terminal_width = terminal_size[0]

def print_centered(string_in):
  input_length = len(string_in)
  empty_space_requried = int((terminal_width-input_length)/2)
  empty_space = " " * empty_space_requried
  print(empty_space + string_in)
  
def centerprint_string(string_in):
  input_length = len(string_in)
  
  if(input_length>terminal_width):
    strings = textwrap.wrap(string_in, width = floor(terminal_width*9/10))
    for string in strings:
      print_centered(string)
  else:
    print_centered(string_in)

def login_screen():
  board = chess.Board()
  print(board)
  # print("Terminal width: " + str(terminal_width))
  centerprint_string("Welcome to the Chess CLI Puzzles App")
  print()
  # print_centered("This application is a lightweight and offline terminal based chess puzzle practice app.")
  # print_centered_multiline("Test")
  centerprint_string("This application is a lightwepight and offline terminal based chess puzzle practice app.")
  # centerprint_string(char46)
  # print()
  # centerprint_string(char48)
  # print()
  # centerprint_string(char50)
  # print()
  # centerprint_string(char54)
  # print()

def main():
  # print("Hello, CS361!")
  login_screen()


main()