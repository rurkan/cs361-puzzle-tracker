import pandas as pd
import chess

df = pd.read_csv("local_data/puzzles_library.csv")


def fen_to_list(fen):
  fen+="/"
  rows = []
  old_loc = 0
  new_loc = fen.find("/")
  for i in range(0, 8):
    board_scrap = fen[old_loc:new_loc]
    rows.append(board_scrap)
    old_loc = new_loc + 1
    new_loc = fen.find("/", old_loc)
  return rows


def board_to_list(game):
  fen = game.board_fen()
  return fen_to_list(fen)

def print_row(row, rownum):
  tiles = ['\u25a0', '\u25a1']
  # 25a0: ■, 25a1: □, unicode for black square and white square
  # I set background to black, so I'm using ■ as white square
  even = not bool(rownum%2)
  print("\x1B[40;37m", end =" ")
  # \x1B[{data};{data}m hex ansi excape sequence, data, delimiter, data, end escape sequence
  for element in row:
    if element.isnumeric():
      for i in range(int(element)):
        print(tiles[(even+i)%2],end=" ")
      even = bool((int(even)+int(element))%2)
      # really not my proudest code to be honest
    else:
      # If the piece belongs to white, make it red, if black, make it blue
      print(('\x1B[34m' if element.islower() else '\x1B[31m')+element, end = " \x1B[37m")
      even = not even # Invert
  print("\x1B[0m|  "+str(rownum)+"")
  # clears the ansi formatting set earlier for coloration

    

def print_board_list(rows):
  # if blank == None:
  #   # Large White Square = \u25FC
  #   # Large Black Square = \u25A0
  #   blank = '\u25a0'
  # row_count = 0
  for i in range(8):
    print_row(rows[i], i+1)
  print(18*"\u203E")
  print(" a b c d e f g h")
  
  # I found that my Windows Powershell doesn't support the ANSI overline
  # Replacing this section to maximize OS compatability
  # print('\033[53m'+" a b c d e f g h  "+'\u200b'+'\033[55m')
  # \033[53m begins overline, \u200b is a zero width space to make the overline continue
  # over the spaces, to make it line up with the row counts

def print_board(game):
  print_board_list(board_to_list(game))

# Testing area
"""

# Random Puzzle
# puzzle = df.sample(n=1).to_dict(orient='records')[0]

my_board = chess.Board()
# my_board.set_fen(puzzle['FEN'])

my_row = df[df["PuzzleId"] == "0000D"].to_dict(orient="records")[0]
# print(my_row)
my_board.set_fen(my_row["FEN"])
print_board(my_board)
print("Pushing move d3d6\n")

my_board.push_uci("d3d6")
print_board(my_board)
print("Flipping board\n")
flipped_board = my_board.transform(chess.flip_vertical).transform(chess.flip_horizontal)
print_board(flipped_board)
print("Pushing move f8d8\n")
my_board.push_uci("f8d8")
print_board(my_board)
# print(my_board.unicode())
# print(my_board.turn)
# print(chess.BLACK)
# chess.Board().turn = True when white is to play, False when black is to play

# rows = board_to_list(my_board)
# print(rows)
# print_board_list(rows)
# init(autoreset=True)
# print_row([])

# print('\x1B[40;31m'+('\u25a0')+' \x1B[34m'+('\u25a1'), end ='\x1B[0m\n')
"""
