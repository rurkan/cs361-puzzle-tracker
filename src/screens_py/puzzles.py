from sys import exit
from time import sleep

from data import make_dict, puzzles
from methods.gameplay import play_move, puzzle_handler
from methods.input_helper import get_screen_input
from methods.print_helper import centerprint_string
from methods.puzzle_helper import string_from_fen
from methods.puzzle_manager import get_themes
from methods.user_data import add_to_history, get_cancel_time


def puzzle_main(username):
  userin = get_screen_input(puzzles + "puzzle_main.txt", make_dict(usr=username))
  match userin:
    case "1":
      return ["play_puzzle", username]
    case "2":
      return ["puzzle_theme", username]
    case "3":
      return ["puzzle_id", username]
    case "4":
      return ["display_board", username]
    case "m":
      return ["menu", username]
    case _:
      return ["ex", None]


def puzzle_by_theme(username):
  data = make_dict(usr=username)
  themes = get_themes()
  result = False
  while result in ["cancel", "themes", False]:
    userin = get_screen_input(puzzles + "puzzle_by_theme.txt", data)
    if userin == "cancel":
      centerprint_string("You input CANCEL. Cancelling search by theme", "-")
      sleep(get_cancel_time(username))
      return ["puzzle_main", username]
    elif userin[0] == "themes":
      data["$themes"] = "List of all themes: " + (", ".join(themes))
      continue
    else:
      if userin[0] not in themes:
        data["$error"] = (
          'ERROR: Please input a valid theme. Type "themes" for a list of themes'
        )
        continue
      return play_puzzle(username, Theme=userin[0])


def puzzle_by_id(username):
  data = make_dict(usr=username)
  puzzle = None
  while puzzle is None:
    userin = get_screen_input(puzzles + "puzzle_by_id.txt", data)
    if userin == "cancel":
      centerprint_string("You input CANCEL. Cancelling search by theme", "-")
      sleep(get_cancel_time(username))
      return ["puzzle_main", username]
    else:
      result = play_puzzle(username, PuzzleId=userin[0])
      if result is None:
        data["$error"] = "ERROR: Please input a valid PuzzleID"
        continue
      else:
        return result


def play_puzzle(username, PuzzleId=None, Theme=None):
  data = make_dict(usr=username, id=PuzzleId)
  data["theme"] = Theme
  data = puzzle_handler(data)
  if (data) is None:
    return None

  play_result = False
  while play_result != "success":
    userin = get_screen_input(puzzles + "play_puzzle.txt", data)
    if userin == "cancel":
      centerprint_string("You input CANCEL. Going back to the puzzle menu.", "-")
      sleep(get_cancel_time(username))
      return ["puzzle_main", username]
    else:
      play_result = play_move(data, userin)
      if play_result == "success":
        print("Puzzle complete! Writing puzzle to player history, please wait.")
        print("Puzzle history is currently only accessible through the files.")
        add_to_history(data)
        return ["puzzle_main", username]
      else:
        data["$error"] = play_result
  exit()


def display_board_fen(username):
  data = make_dict(usr=username)
  while True:
    userin = get_screen_input(puzzles + "display_board.txt", data)
    data["$error"] = None
    if userin == "cancel":
      centerprint_string("You input CANCEL. Going back to the puzzle menu.", "-")
      sleep(get_cancel_time(username))
      return ["puzzle_main", username]
    else:
      board = string_from_fen(userin[0])
      if board is not None:
        data["$board"] = board
        continue
      else:
        print("error side")
        data["$error"] = "ERROR: Not valid FEN formatting, please try again."
