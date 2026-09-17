import chess  # noqa: F401


def fen_to_list(fen):
  fen += "/"
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


# For build_row to not wrap text, the terminal
# Must be a minimum of 21 characters wide
def build_row_string(board_row, rownum):
  row = ""
  tiles = ["\u25a0", "\u25a1"]
  # 25a0: ■, 25a1: □, unicode for black square and white square
  # I set background to black, so I'm using ■ as white square
  even = not bool(rownum % 2)
  row += "\x1b[40;37m "
  # \x1B[{data};{data}m hex ansi excape sequence, data, delimiter, data, end escape sequence
  for element in board_row:
    if element.isnumeric():
      for i in range(int(element)):
        row += tiles[(even + i) % 2] + " "
      even = bool((int(even) + int(element)) % 2)
      # really not my proudest code to be honest
    else:
      # If the piece belongs to white, make it red, if black, make it blue
      row += ("\x1b[34m" if element.islower() else "\x1b[31m") + element + " \x1b[37m"
      even = not even  # Invert
  row += "\x1b[0m|  " + str(rownum) + "\n"
  # clears the ansi formatting set earlier for coloration
  return row


def build_board_string(rows, turn):
  # if blank == None:
  #   # Large White Square = \u25FC
  #   # Large Black Square = \u25A0
  #   blank = '\u25a0'
  # row_count = 0
  fullboard = ""

  column_letters = "a b c d e f g h"
  if turn == False:  # Black is playing, reverse the markers
    column_letters = column_letters[::-1]
  disp = 9 if turn else 0
  for i in range(8) if turn else reversed(range(8)):
    disp += -1 if turn else 1
    row = rows[i] if turn else rows[i][::-1]
    fullboard += build_row_string(row, disp)

  fullboard += 18 * "\u203e" + "\n"
  fullboard += " " + str(column_letters)
  return fullboard

  # I found that my Windows Powershell doesn't support the ANSI overline
  # Replacing this section to maximize OS compatability
  # print('\033[53m'+" a b c d e f g h  "+'\u200b'+'\033[55m')
  # \033[53m begins overline, \u200b is a zero width space to make the overline continue
  # over the spaces, to make it line up with the row counts


def board_to_string(game):
  return build_board_string(board_to_list(game), game.turn)


def string_from_fen(fen):
  game = chess.Board()
  try:
    game.set_fen(fen)
    return build_board_string(board_to_list(game), game.turn)
  except ValueError:
    return None
