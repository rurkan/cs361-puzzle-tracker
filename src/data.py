screen_path = "src/screens_text/"
login_create = screen_path + "login_create/"
settings = screen_path + "settings/"
puzzles = screen_path + "puzzles/"


def make_dict(
  err=None,
  usr=None,
  brd=None,
  id=None,
  prev_move=None,
  move_corr=None,
  num_puzzles=None,
  themes=None,
):
  data = {
    "$error": err,
    "$username": usr,
    "$board": brd,
    "$puzzleid": id,
    "$previous_move": prev_move,
    "$move_correct": move_corr,
    "$num_puzzles": num_puzzles,
    "$themes": themes,
  }
  return data
