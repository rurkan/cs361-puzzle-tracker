from methods.clear import clearscreen
from methods.print_helper import (
  centerprint_string,
  incomplete_screen,
  print_with_modifiers,
  printwrap
)
from methods.user_data import (
  user_signout,
  user_signin,
  generate_account,
  signin_valid
)
from time import sleep

screen_path = "src/screens/"

def display_screen(lines, error = None, username = None):
  clearscreen()
  data = []
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
    
    val = print_with_modifiers(line, modifiers, error, username)
    if ">" in modifiers:
      if val == "cancel":
        return val
      data.append(val)

  if not ">" in modifiers:
    data = input("Option Select: ").lower()
  return data


def get_screen_input(filepath, error = None, username = None):

  file = open(filepath, 'r', encoding='utf-8')
  lines = file.read().splitlines()
  file.close()
  
  options = lines[0].split()
  userin = display_screen(lines, error, username)
  if type(userin) is not list:
    while userin.lower() not in options:
      userin = display_screen(lines, "PLEASE INPUT A SELECTION FROM THE OPTIONS AVAILABLE", username)
  elif(len(userin)>2 and userin[1] != userin[2]):
    while (userin[1] != userin[2]):
      userin = display_screen(lines, "PASSWORDS DO NOT MATCH. PLEASE TRY AGAIN")
    
  return userin
  
def screen_select_handler(screen_code, username = None):
  match screen_code:
    case "ex":
      clearscreen()
      print("Thanks for playing the Chess CLI Puzzles app!\n")
      exit()
    case "login":
      return(login_home())
    case "login_input":
      return(login_input())
    case "menu":
      return(main_menu(username))
    case "create_account_home":
      return(create_account_home())
    case "create_account_input":
      return(create_account_input())
    case "settings":
      return(account_settings(username))
      
    
def login_home():
  userin = get_screen_input(screen_path+"login_home.txt")
  match userin:
    case "1":
      # centerprint_string("PROMPT USER FOR LOGIN INFO, INCOMPLETE", "-")
      # username = input("Username (no pass for testing): ")
      # user_signin(username)
      return(["login_input",None])
      return(["menu", username])
    case "2":
      return(["create_account_home", None])
    case _:
      return(["ex", None])
      
      
def login_input():
  userin = get_screen_input(screen_path+"login_input.txt")
  logged_in = signin_valid(userin)
  while logged_in != True:
    if logged_in == "cancel":
      centerprint_string("You input CANCEL. Cancelling signin attempt","-")
      sleep(2)
      return(["login", None])
    else:
      error = "ERROR: INCORRECT USERNAME OR PASSWORD, TRY AGAIN"
      userin = get_screen_input(screen_path+"login_input.txt", error)
      logged_in = signin_valid(userin)
  user_signin(userin[0])
  return(["menu",userin[0]])
      
  
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


def create_account_home():
  userin = get_screen_input(screen_path+"create_account_home.txt")
  
  match userin:
    case "1":
      return(["create_account_input", None])
    case "b":
      return(["login", None])
    case _:
      return(["ex", None])

def create_account_input():
  userin = get_screen_input(screen_path+"create_account_input.txt")
  created = generate_account(userin)
  while created is not True:
    if created == "cancel":
      centerprint_string("You input CANCEL. Cancelling account creation","-")
      sleep(2)
      return(["login", None])
    match created:
      case "exists":
        error = "ERROR: ACCOUNT WITH THIS USERNAME ALREADY EXISTS"
      case "same":
        error = "ERROR: USERNAME AND PASSWORD CANNOT BE THE SAME"
    userin = get_screen_input(screen_path+"create_account_input.txt", error)
    created = generate_account(userin)

  return(["login", None])


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