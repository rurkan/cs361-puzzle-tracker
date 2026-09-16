from sys import exit
from methods.clear import clearscreen
from methods.user_data import get_username
from interface import screen_select_handler
from methods.puzzle_manager import read_puzzles


def main():
  screen_code = None
  print("Loading puzzles data file, please wait! This can take a while.")
  read_puzzles()
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
