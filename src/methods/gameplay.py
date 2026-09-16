import chess
from methods.puzzle_helper import board_to_string
from methods.puzzle_manager import get_puzzle


def puzzle_handler(data):
  # get_puzzle generates a dictionary with the puzzle information
  puzzle_dict = get_puzzle(PuzzleId=data["$puzzleid"], Theme=data["theme"])
  chess_board = chess.Board()
  chess_board.set_fen(puzzle_dict["FEN"])

  data["move_sequence"] = get_move_sequence(puzzle_dict)
  cpu_move = data["move_sequence"].pop(0)
  chess_board.push_uci(cpu_move)
  data["$previous_move"]=cpu_move

  # chess_board = chess_board.transform(
  #   chess.flip_vertical if chess_board.turn else chess.flip_horizontal
  # )

  data["$puzzleid"] = puzzle_dict["PuzzleId"]
  data["game"] = chess_board
  data["$board"] = board_to_string(chess_board)
  data["rating"] = puzzle_dict["Rating"]

  return data


def get_move_sequence(puzzle_dict):
  return puzzle_dict["Moves"].split()

def play_move(data, move_uci):
  game = data["game"]
  
  try:
    game.parse_uci(move_uci)
  except ValueError as err:
    errmsg = str(err)
    if "illegal uci" in errmsg:
      return "Your move, "+str(move_uci)+" was illegal (possibly putting self in check). Try again."
    else:
      return "Your move, "+str(move_uci)+" is not formatted in UCI. Try again."
    
  # If the player move is correct
  if(move_uci==data["move_sequence"][0]):
    # Push their move and remove it from the correct move sequence
    game.push_uci(move_uci)
    data["move_sequence"].pop(0)
    if(len(data["move_sequence"])==0):
      # Sequence contains no more moves, puzzle complete
      return "success"
    
    # Push the CPU's response and remove it from correct move sequence
    cpu_move = data["move_sequence"].pop(0)
    game.push_uci(cpu_move)
    data["$previous_move"]=cpu_move
    data["$board"] = board_to_string(game)
    return "Your move, "+str(move_uci)+" was correct. Move next."
  return "Your move, "+str(move_uci)+" was incorect. Try again."
    
    