from methods.clear import clearscreen
from methods.print_helper import (
  centerprint_string,
  incomplete_screen,
  print_with_modifiers,
  printwrap
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
      printwrap(line)
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
      return(login_screen())
    case "menu":
      return(main_menu(username))
    case "create_account":
      return(account_creation())
    case "settings":
      return(account_settings(username))
  
      
    
def login_screen():
  userin = get_screen_input(screen_path+"login_home.txt")
  match userin:
    case "1":
      centerprint_string("PROMPT USER FOR LOGIN INFO, INCOMPLETE", "-")
      username = input("Username (no pass for testing): ")
      user_signin(username)
      return(["menu", username])
    case "2":
      return(["create_account", None])
    case _:
      return(["ex", None])
      
  
def main_menu(username):
  userin = get_screen_input(screen_path+"main_menu.txt", None, username)
  match userin:
    case "1":
      incomplete_screen("PUZZLE")
      return(["ex", None])
    case "2":
      incomplete_screen("HISTORY")
      return(["ex", None])
    case "3":
      return(["settings", username])
    case "p":
      incomplete_screen("PUZZLE")
      return(["ex", None])
    case _:
      return(["ex", None])


def account_creation():
  userin = get_screen_input(screen_path+"create_account_home.txt")
  
  match userin:
    case "1":
      centerprint_string("Usernames and passwords must be alphanumeric.")
      info = get_account_info("creation")

###########################################################



    case "b":
      return(["login", None])
    case _:
      return(["ex", None])


def account_settings(username):
  userin = get_screen_input(screen_path+"account_settings.txt", None, username)
  match userin:
    case "1":
      return(confirmation_screen("user_history_reset", username))
    case "2":
      return(confirmation_screen("user_signout", username))
    case "m":
      return(["menu", username])
    case _:
      return(["ex"])
      
def confirmation_screen(confirmation_type, username):
  userin = get_screen_input(screen_path+""+confirmation_type+".txt")
  if(confirmation_type == "user_history_reset"):
    if(userin == "confirm_reset"):
      incomplete_screen("DELETED HISTORY")
      return(["ex", None])
    return(["settings", username])
  elif(confirmation_type == "user_signout"):
    if(userin == "y"):
      user_signout()
      return(["login", None])
    else:
      return(["settings", username])
  

def get_account_info(infotype):
  if(infotype == "login"):
    print("Nothing to do currently")
  elif(infotype == "creation"):
    index = 0
    username = get_simple_info("Username")
    user_data = ["_INVALID_", "_INVALID_", "_INVALID_"]
        

def get_simple_info(infotype):
  information = "_INVALID_"
  while not information.isalnum():
    information = input(infotype+": ")
  return information