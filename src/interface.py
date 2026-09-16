from time import sleep
from sys import exit
from methods.clear import clearscreen
from methods.gameplay import puzzle_handler, play_move
from methods.print_helper import (
  centerprint_string,
  incomplete_screen,
  print_with_modifiers,
  printwrap,
)
from methods.user_data import (
  user_signout,
  user_signin,
  generate_account,
  signin_valid,
  add_to_history,
  get_completed_puzzles,
)

screen_path = "src/screens/"
  
def make_dict(
  err=None,
  usr=None,
  brd=None,
  id=None,
  prev_move=None,
  move_corr=None,
  num_puzzles=None,
):
  data = {
    "$error": err,
    "$username": usr,
    "$board": brd,
    "$puzzleid": id,
    "$previous_move": prev_move,
    "$move_correct": move_corr,
    "$num_puzzles": num_puzzles,
  }
  return data
  
def display_screen(lines, data = None):
  clearscreen()
  return_data = []
  for line in lines[1:]:
    # If the line is blank or has no modifiers, just print
    if (len(line) == 0):
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
    if("$puzzleid" in line):
      modifiers.append("$puzzleid")
    if("$board" in line):
      modifiers.append("$board")
    if("$previous_move" in line):
      modifiers.append("$previous_move")
    if("$num_puzzles" in line):
      modifiers.append("$num_puzzles")
    if(line[0] == "-"):
      modifiers.append("-")
    if(line[0] == " "):
      modifiers.append(" ")
    if(line[0] == ">"):
      modifiers.append(">")
    
    val = print_with_modifiers(line, modifiers, data)
    if ">" in modifiers:
      if val == "cancel":
        return val
      return_data.append(val)
  if not ">" in modifiers:
    return_data = input("Input Move: " if "$board" in lines else "Option Select: ").lower()
  return return_data


def get_screen_input(filepath, data):

  with open(filepath, 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()
  
  options = lines[0].split()
  userin = display_screen(lines, data)
  
  if type(userin) is not list:
    while userin.lower() not in options:
      if "cancel" in options:
        return userin
      data["$error"]="PLEASE INPUT A SELECTION FROM THE OPTIONS AVAILABLE"
      userin = display_screen(lines,  data)
      
  elif(len(userin)>2 and userin[1] != userin[2]):
    while ("cancel" not in userin and userin[1] != userin[2]):
      data["$error"]="PASSWORDS DO NOT MATCH. PLEASE TRY AGAIN"
      userin = display_screen(lines, data)
    
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
    case "puzzle_main":
      return(puzzles_main(username))
    case "play_puzzle":
      return(play_puzzle(username))
    case "settings":
      return(account_settings(username))
    case _:
      print("The screen "+screen_code+" does not currently exist. We apologize.")
      exit()
      
    
def login_home():
  userin = get_screen_input(screen_path+"login_home.txt", make_dict())
  match userin:
    case "1":
      # centerprint_string("PROMPT USER FOR LOGIN INFO, INCOMPLETE", "-")
      # username = input("Username (no pass for testing): ")
      # user_signin(username)
      return(["login_input",None])
    case "2":
      return(["create_account_home", None])
    case _:
      return(["ex", None])
      

def login_input():
  userin = get_screen_input(screen_path+"login_input.txt", make_dict())
  logged_in = signin_valid(userin)
  while logged_in != True:
    if logged_in == "cancel":
      centerprint_string("You input CANCEL. Cancelling signin attempt","-")
      sleep(2)
      return(["login", None])
    else:
      error = "ERROR: INCORRECT USERNAME OR PASSWORD, TRY AGAIN"
      userin = get_screen_input(screen_path+"login_input.txt", make_dict(err=error))
      logged_in = signin_valid(userin)
  user_signin(userin[0])
  return(["menu",userin[0]])
      
  
def main_menu(username):
  userin = get_screen_input(screen_path+"main_menu.txt", make_dict(usr=username))
  match userin:
    case "1":
      return(["puzzle_main", username])
    case "2":
      return(["history",username])
    case "3":
      return(["settings", username])
    case "p":
      return(["play_puzzle", username])
    case _:
      return(["ex", None])


def create_account_home():
  userin = get_screen_input(screen_path+"create_account_home.txt", make_dict())
  
  match userin:
    case "1":
      return(["create_account_input", None])
    case "b":
      return(["login", None])
    case _:
      return(["ex", None])

def create_account_input():
  userin = get_screen_input(screen_path+"create_account_input.txt", make_dict())
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
    userin = get_screen_input(screen_path+"create_account_input.txt", make_dict(err=error))
    created = generate_account(userin)

  return(["login", None])

def puzzles_main(username):
  userin = get_screen_input(screen_path+"puzzles_main.txt", make_dict(usr=username))
  match userin:
    case "1":
      return(["play_puzzle",username])
    case "2":
      return(["puzzle_theme",username])
    case "3":
      return(["puzzle_id",username])
    case "m":
      return(["menu",username])
    case _:
      return(["ex", None])

def play_puzzle(username, PuzzleId=None, Theme=None):
  data = make_dict(usr=username, id=PuzzleId)
  data["theme"]=Theme
  data = puzzle_handler(data)

  play_result = False
  while play_result != "success":
    userin = get_screen_input(screen_path+"play_puzzle.txt", data)
    if userin == "cancel":
      centerprint_string("You input CANCEL. Going back to the puzzle menu.","-")
      sleep(2)
      return(["puzzle_main", username])
    else:
      play_result = play_move(data, userin)
      if play_result == "success":
        print("Writing puzzle to player history, please wait.")
        add_to_history(data)
        return(["puzzle_main", username])
      else:
        data["$error"] = play_result
  exit()
  
  

def account_settings(username):
  data = get_completed_puzzles(make_dict(usr=username))
  userin = get_screen_input(screen_path+"account_settings.txt", data)
  match userin:
    case "1":
      return(confirmation_screen("user_history_reset", username))
    case "2":
      return(confirmation_screen("user_signout", username))
    case "m":
      return(["menu", username])
    case _:
      return(["ex", None])
      
def confirmation_screen(confirmation_type, username):
  userin = get_screen_input(screen_path+""+confirmation_type+".txt", make_dict(usr=username))
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