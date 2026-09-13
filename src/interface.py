from methods.clear import clearscreen
from methods.centerprints import centerprint_string
from methods.user_data import user_signout, user_signin

def display_screen(lines, error = None, username = None):
  clearscreen()
  for line in lines[1:]:
    # If the line isn't blank, there are a few special character codes
    # " " for center and "-" for hyphen spacer at the beginning
    # or begin a word (not line) with "$" for a variable
    # Easiest way I could think of to designate special formatting
    if(len(line) != 0 and (not line[0].isalnum())):
      if(line[0] == "-"):
        centerprint_string(line, "-")
      elif("$error" in line):
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
    case "settings":
      account_settings(username)
      
    
def login_screen():
  userin = get_screen_input("src/screens/login.txt")
  match userin:
    case "1":
      centerprint_string("PROMPT USER FOR LOGIN INFO, INCOMPLETE", "-")
      username = input("Username (no pass for testing): ")
      user_signin(username)
      screen_select_handler("menu", username)
    case "2":
      centerprint_string("DISPLAY ACCOUNT CREATION SCREEN, INCOMPLETE", "-")
      screen_select_handler("ex")
    case _:
      screen_select_handler("ex")
      
  
def main_menu(username):
  userin = get_screen_input("src/screens/main_menu.txt", None, username)
  match userin:
    case "1":
      centerprint_string("DISPLAY PUZZLE SCREEN, INCOMPLETE", "-")
      screen_select_handler("ex")
    case "2":
      centerprint_string("DISPLAY HISTORY SCREEN, INCOMPLETE", "-")
      screen_select_handler("ex")
    case "3":
      screen_select_handler("settings", username)
    case "p":
      centerprint_string("DISPLAY PUZZLE SCREEN, INCOMPLETE" "-")
      screen_select_handler("ex")
    case _:
      screen_select_handler("ex")

def account_settings(username):
  userin = get_screen_input("src/screens/account_settings.txt", None, username)
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
  userin = get_screen_input("src/screens/"+confirmation_type+".txt")
  if(confirmation_type == "user_history_reset"):
    if(userin == "confirm_reset"):
      centerprint_string("PUZZLE HISTORY AND/OR HISTORY DELETION NOT IMPLEMENTED", "-")
    screen_select_handler("settings", username)
  elif(confirmation_type == "user_signout"):
    if(userin == "y"):
      user_signout()
      screen_select_handler("login")
  
  