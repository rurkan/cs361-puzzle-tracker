from time import sleep

from data import make_dict, settings
from methods.input_helper import get_screen_input
from methods.print_helper import (
  centerprint_string,
  incomplete_screen,
)
from methods.user_data import (
  get_cancel_time,
  get_completed_puzzles,
  set_cancel_time,
  user_signout,
)


def account_settings(username):
  data = get_completed_puzzles(make_dict(usr=username))
  userin = get_screen_input(settings + "account_settings.txt", data)
  match userin:
    case "1":
      return confirmation_screen("user_history_reset", username)
    case "2":
      return confirmation_screen("user_signout", username)
    case "3":
      return change_cancel_time(username)
    case "m":
      return ["menu", username]
    case _:
      return ["ex", None]


def change_cancel_time(username):
  data = make_dict(usr=username)
  userin = [None]
  while type(userin) is not int:
    userin = get_screen_input(settings + "change_cancel_time.txt", data)
    if userin == "cancel":
      centerprint_string("You input CANCEL. Going back to account settings.", "-")
      sleep(get_cancel_time(username))
      return ["settings", username]
    try:
      userin = int(userin[0])
    except ValueError:
      data["$error"] = "ERROR: Please input an integer or decimal cancellation delay."
      continue
    set_cancel_time(username, userin)
    centerprint_string(
      "Successfully modified cancel delay, new delay: " + str(userin), "-"
    )
    return ["settings", username]


def confirmation_screen(confirmation_type, username):
  userin = get_screen_input(
    settings + "" + confirmation_type + ".txt", make_dict(usr=username)
  )
  if confirmation_type == "user_history_reset":
    if userin == "confirm_reset":
      incomplete_screen("DELETED HISTORY")
      return ["ex", None]
    centerprint_string(
      "You did not input one of the available options, auto-cancelling.", "-"
    )
    sleep(get_cancel_time(username))
    return ["settings", username]
  elif confirmation_type == "user_signout":
    if userin == "y":
      user_signout()
      return ["login", None]
    else:
      # This feels safer
      return ["settings", username]
