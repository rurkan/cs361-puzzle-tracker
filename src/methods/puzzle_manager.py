import pandas as pd

df = None

def read_puzzles(path = None):
  if(path == None):
    path = "local_data/puzzles_library.csv"
  global df
  try:
    df = pd.read_csv(path)
  except FileNotFoundError:
      print("\nERROR: You do not currently have a puzzle library, please put it at:\n\t./local_data/puzzles_library.csv")
      print("\n A recommended puzzle database is the Lichess database, found at https://database.lichess.org/#puzzles\n")
      print("Alternatives are acceptable if they follow the Lichess database formatting\n")
      return False


def get_puzzles():
  return df


def get_puzzle(data_frame = None, PuzzleId = None, Theme = None):
  if(data_frame is None):
    data_frame = df
  if PuzzleId is not None:
    return data_frame[data_frame["PuzzleId"] == PuzzleId].to_dict(orient="records")[0]
  if Theme is not None:
    # Only allowing search by one theme because I'm lazy
    return get_puzzle(data_frame=puzzles_with_theme(Theme))
  # If neither theme or PuzzleId are selected, picks random puzzle from the df
  return data_frame.sample(n=1).to_dict(orient='records')[0]


def puzzles_with_theme(df, Theme):
  # Regex will prevent other themes that include the word
  # Ex. "verylong" includes "long"
  # But should still grab themes at the start and end of Themes category
  
  # I don't know Regex, so Regex help mostly from:
  # https://stackoverflow.com/questions/15863066/how-to-match-a-whole-word-with-a-regular-expression
  return df[df['Themes'].str.contains(r"\b"+Theme+r"\b", na=False, regex=True)]



