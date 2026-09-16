# The file localdata/username exists solely as an unencrypted way to cache
# the current logged in user, so people don't have to sign back in every time
import os
from time import sleep

import pandas as pd


def get_username():
  try:
    with open("local_data/username", "r", encoding="utf-8") as file:
      usr = file.read()
    return usr
  except FileNotFoundError:
    return None


def user_signout():
  if os.path.exists("local_data/username"):
    os.remove("local_data/username")
  else:
    print("ERROR, FILE COULD NOT BE DELETED")


def user_signin(usr):
  try:
    with open("local_data/username", "w", encoding="utf-8") as file:
      file.write(usr)
  except PermissionError:
    print("ERROR, FILE COULD NOT BE WRITTEN TO")


def account_exists(username):
  all_user_data = pd.read_csv("local_data/users_plaintext.csv")
  return all_user_data["username"].eq(username).any()


def new_account_valid(user_data):
  if user_data == "cancel":
    return "cancel"
  if user_data[0] == user_data[1]:
    return "same"
  if account_exists(user_data[0]):
    return "exists"
  return True


def generate_account(user_data):
  valid_result = new_account_valid(user_data)
  if valid_result is not True:
    return valid_result
  else:
    formatted_data = {
      "username": [user_data[0]],
      "password_plaintext": [user_data[1]],
      "cancel_time": 2,
    }
    pandas_data = pd.DataFrame(formatted_data)
    pandas_data.to_csv(
      "local_data/users_plaintext.csv", mode="a", header=False, index=False
    )
    return True


def signin_valid(login_info):
  if login_info == "cancel":
    return "cancel"
  username = login_info[0].strip()
  password = login_info[1].strip()
  users = pd.read_csv("local_data/users_plaintext.csv")
  # Modification of Robin's answer to
  # https://stackoverflow.com/questions/24761133/pandas-check-if-row-exists-with-certain-values
  login_good = (
    ((users["username"] == (username)) & (users["password_plaintext"] == (password)))
    .any()
    .all()
  )
  return login_good


def add_to_history(data):
  username = data["$username"]
  PuzzleId = data["$puzzleid"]
  Rating = data["rating"]
  IncorrectMoves = data["incorrect_moves"]
  path = "local_data/puzzle_history/" + username + ".csv"
  df = pd.DataFrame(
    {"PuzzleId": [PuzzleId], "Rating": [Rating], "IncorrectMoves": [IncorrectMoves]}
  )
  if os.path.exists(path):
    current_history = pd.read_csv(path)
    df = pd.concat([current_history, df], ignore_index=True)
    df.drop_duplicates(subset=["PuzzleId"], keep="first", inplace=True)
    df.to_csv(path, mode="w", index=False)
  else:
    df.to_csv(path, mode="w", index=False)

  sleep(1.5)


def clear_history(data):
  username = data["$username"]
  path = "local_data/puzzle_history/" + username + ".csv"
  if os.path.exists(path):
    df = pd.DataFrame({"PuzzleId": [], "Rating": [], "IncorrectMoves": []})
    df.to_csv(path, mode="w", index=False)
    return True
  return False


def get_completed_puzzles(data):
  username = data["$username"]
  path = "local_data/puzzle_history/" + username + ".csv"
  if os.path.exists(path):
    user_history = pd.read_csv(path)
    data["$num_puzzles"] = str(len(user_history))
  else:
    data["$num_puzzles"] = "0"
  return data


def set_cancel_time(username, new_time):
  df = pd.read_csv("local_data/users_plaintext.csv")
  df.loc[df["username"] == username, "cancel_time"] = new_time

  df.to_csv("local_data/users_plaintext.csv", mode="w", index=False)


def get_cancel_time(username):
  df = pd.read_csv("local_data/users_plaintext.csv")
  return (df.loc[df["username"] == username, "cancel_time"]).to_list()[0]
