from pathlib import Path
from sys import exit
from time import sleep

from interface import screen_select_handler
from methods.clear import clearscreen
from methods.print_helper import print_centered
from methods.puzzle_manager import read_puzzles
from methods.user_data import get_username


def main():
  screen_code = None
  if read_puzzles() is False:
    print("\nPlease input the path to your puzzle library.")
    print('Puzzle libraries paths should be formatted as such "local_data/{name}.csv"')
    path_str = input("Path: ")
    print("\nAttempting to load puzzles data file, please wait! This can take a while.")


    if read_puzzles(path_str) is False:
      exit()
    else:
      print("Renaming your puzzles file so that it loads automatically.")
      filepath = Path(path_str)
      filepath.rename("local_data/puzzles_library.csv")
      sleep(2)

  # read_puzzles("local_data/lichess_db_puzzle.csv")
  # 1GB database including 6 million puzzles o_O, loading takes forever

  # return()
  clearscreen()
  # Check if there's already a username file, if not, display login screen
  if username != None:
    screen_code = "menu"
  elif username == None:
    screen_code = "login"
  else:
    print("Something went wrong, our bad. Investigate and try again.")
    exit()
  data = [screen_code, username]
  while True:
    data = screen_select_handler(data[0], data[1])


username = get_username()
main()
