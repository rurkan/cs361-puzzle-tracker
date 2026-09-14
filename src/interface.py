from methods.clear import clearscreen
from methods.print_helper import (
  centerprint_string,
  incomplete_screen,
  print_with_modifiers
)
from methods.user_data import (
  user_signout,
  user_signin
)

screen_path = "src/screens/"

def display_screen(lines, error = None, username = None):
  clearscreen()
  for line in lines[1:]:
    
    # If the line is blank or has no modifiers, just print
    if (len(line) == 0 or line[0].isalnum()):
      print(line)
      continue
      
    # If the line has modifiers. See modifiers belo
    # Start with " " for center, "-" for hyphen spacer, or ">" for user input
    # or begin a word (not line) with "$" for a variable
    modifiers = []

    if("$error" in line):
      modifiers.append("$error")
    if("$username" in line):
      modifiers.append("$username")
    if(line[0] == "-"):
      modifiers.append("-")
    if(line[0] == " "):
      modifiers.append(" ")
    if(line[0] == ">"):
      modifiers.append(">")
      
    print_with_modifiers(line, modifiers, error, username)
  if not ">" in modifiers:
    return(input("Option Select: ").lower())

def get_screen_input(filepath, data = None, username = None):

  file = open(filepath, 'r', encoding='utf-8')
  lines = file.read().splitlines()
  file.close()
  
  options = lines[0].split()
  userin = display_screen(lines, data, username)
  while userin.lower() not in options:
    print(userin.lower())
    print(options)
    userin = display_screen(lines, "PLEASE INPUT A SELECTION FROM THE OPTIONS AVAILABLE", username)
  return userin
  
def screen_select_handler(screen_code, username = None):
  match screen_code:
    case "ex":
      clearscreen()
      print("Thanks for playing the Chess CLI Puzzles app!\n")
      exit()
    case "login":
      login_screen()
    case "menu":
      main_menu(username)
    case "create_account":
      # account_creation()
      incomplete_screen("ACCOUNT CREATION")
    case "settings":
      account_settings(username)
      
    
def login_screen():
  userin = get_screen_input(screen_path+"login.txt")
  match userin:
    case "1":
      centerprint_string("PROMPT USER FOR LOGIN INFO, INCOMPLETE", "-")
      username = input("Username (no pass for testing): ")
      user_signin(username)
      screen_select_handler("menu", username)
    case "2":
      screen_select_handler("create_account")
    case _:
      screen_select_handler("ex")
      
  
def main_menu(username):
  userin = get_screen_input(screen_path+"main_menu.txt", None, username)
  match userin:
    case "1":
      incomplete_screen("PUZZLE")
      screen_select_handler("ex")
    case "2":
      incomplete_screen("HISTORY")
      screen_select_handler("ex")
    case "3":
      screen_select_handler("settings", username)
    case "p":
      incomplete_screen("PUZZLE")
      screen_select_handler("ex")
    case _:
      screen_select_handler("ex")


def account_settings(username):
  userin = get_screen_input(screen_path+"account_settings.txt", None, username)
  match userin:
    case "1":
      confirmation_screen("user_history_reset", username)
    case "2":
      confirmation_screen("user_signout", username)
    case "m":
      screen_select_handler("menu", username)
    case _:
      screen_select_handler("ex")
      
def confirmation_screen(confirmation_type, username):
  userin = get_screen_input(screen_path+""+confirmation_type+".txt")
  if(confirmation_type == "user_history_reset"):
    if(userin == "confirm_reset"):
      incomplete_screen("DELETED HISTORY")
    screen_select_handler("settings", username)
  elif(confirmation_type == "user_signout"):
    if(userin == "y"):
      user_signout()
      screen_select_handler("login")
  
  