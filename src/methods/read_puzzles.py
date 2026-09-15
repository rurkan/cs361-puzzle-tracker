import pandas as pd
import chess

df = pd.read_csv("local_data/puzzles_library.csv")


def fen_to_list(fen):
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
  fen = game.board_fen() + "/"
  return fen_to_list(fen)


def print_board_list(rows, blank=None):
  if blank == None:
    blank = "."
  for row in rows:
    for element in row:
      if element.isnumeric():
        print((blank + " ") * int(element), end="")
      else:
        print(element, end=" ")

    print()


# Testing area

# Random Puzzle
# puzzle = df.sample(n=1).to_dict(orient='records')[0]
my_board = chess.Board()
# my_board.set_fen(puzzle['FEN'])

my_row = df[df["PuzzleId"] == "00008"].to_dict(orient="records")[0]
print(my_row)
my_board.set_fen(my_row["FEN"])

rows = board_to_list(my_board)
print(rows)
print_board_list(rows)
