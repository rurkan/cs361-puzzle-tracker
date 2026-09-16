from sys import exit

from methods.clear import clearscreen
from screens_py.login_create import (
  create_account_home,
  create_account_input,
  login_home,
  login_input,
)
from screens_py.main_menu import main_menu
from screens_py.puzzles import play_puzzle, puzzle_by_id, puzzle_by_theme, puzzle_main
from screens_py.settings import account_settings


def screen_select_handler(screen_code, username=None):
  match screen_code:
    case "ex":
      clearscreen()
      print("Thanks for playing the Chess CLI Puzzles app!\n")
      exit()
    case "login":
      return login_home()
    case "login_input":
      return login_input()
    case "menu":
      return main_menu(username)
    case "create_account_home":
      return create_account_home()
    case "create_account_input":
      return create_account_input()
    case "puzzle_main":
      return puzzle_main(username)
    case "play_puzzle":
      return play_puzzle(username)
    case "puzzle_theme":
      return puzzle_by_theme(username)
    case "puzzle_id":
      return puzzle_by_id(username)
    case "settings":
      return account_settings(username)
    case _:
      print("The screen " + screen_code + " does not currently exist. We apologize.")
      exit()
