from data import make_dict, screen_path
from methods.input_helper import get_screen_input


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