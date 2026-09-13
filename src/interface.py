# Commit number 2 for Assignment 2
# ohhhh slight changes very scary 
from methods.clear import clearscreen
from methods.centerprints import centerprint_string

from methods.read_user import get_username #TEMP FOR TESTING

username = get_username()

def display_screen(lines, error = None):
  clearscreen()
  for line in lines[1:]:
    # If the line isn't blank, there are a few special character codes
    # " " for center and "-" for hyphen spacer at the beginning
    # or begin a word (not line) with "$" for a variable
    # Easiest way I could think of to designate special formatting
    if(len(line) != 0 and (not line[0].isalnum())):
      if("$error" in line):
        if(error is not None): # error should never be none if we reach this
          centerprint_string(error, "-")
      elif("$username" in line):
        if(username is not None):
          centerprint_string(line[1:line.find("$")]+username)
        else:
          centerprint_string("NullUser")
      else:
        centerprint_string(line[1:])
    else:
      print(line)
  return(input("Option Select: ").lower())


def get_screen_input(filepath, data = None):

  file = open(filepath, 'r', encoding='utf-8')
  lines = file.read().splitlines()
  file.close()
  
  options = lines[0].split()
  userin = display_screen(lines, data)
  while userin.lower() not in options:
    print(userin.lower())
    print(options)
    userin = display_screen(lines, "PLEASE INPUT A SELECTION FROM THE OPTIONS AVAILABLE")
  return userin
  
def screen_select_handler(screen_code):
  match screen_code:
    case "ex":
      clearscreen()
      print("Thanks for playing the Chess CLI Puzzles app!\n")
      exit()
    case "m":
      # username = get_username() #TEMP FOR TESTING
      # print(username)
      main_menu(username)
      
    

def login_screen():
  userin = get_screen_input("src/screens/login.txt")
  print(userin)
  match userin:
    case "1":
      centerprint_string("PROMPT USER FOR LOGIN INFO, INCOMPLETE", "-")
      centerprint_string("")
      screen_select_handler("m")
    case "2":
      centerprint_string("DISPLAY ACCOUNT CREATION SCREEN, INCOMPLETE", "-")
      screen_select_handler("ex")
    case _:
      screen_select_handler("ex")
      
  
def main_menu(signed_in_user):
  username = signed_in_user
  userin = get_screen_input("src/screens/main_menu.txt")
  screen_select_handler(userin)
