from time import sleep

from data import login_create, make_dict
from methods.input_helper import get_screen_input
from methods.print_helper import centerprint_string
from methods.user_data import (
  generate_account,
  signin_valid,
  user_signin,
)


def login_home():
  userin = get_screen_input(login_create + "login_home.txt", make_dict())
  match userin:
    case "1":
      return ["login_input", None]
    case "2":
      return ["create_account_home", None]
    case _:
      return ["ex", None]


def login_input():
  userin = get_screen_input(login_create + "login_input.txt", make_dict())
  logged_in = signin_valid(userin)
  while logged_in != True:
    if logged_in == "cancel":
      centerprint_string("You input CANCEL. Cancelling signin attempt", "-")
      sleep(2)
      return ["login", None]
    else:
      error = "ERROR: INCORRECT USERNAME OR PASSWORD, TRY AGAIN"
      userin = get_screen_input("login_input.txt", make_dict(err=error))
      logged_in = signin_valid(userin)
  user_signin(userin[0])
  return ["menu", userin[0]]


def create_account_home():
  userin = get_screen_input(login_create + "create_account_home.txt", make_dict())

  match userin:
    case "1":
      return ["create_account_input", None]
    case "b":
      return ["login", None]
    case _:
      return ["ex", None]


def create_account_input():
  userin = get_screen_input(login_create + "create_account_input.txt", make_dict())
  created = generate_account(userin)
  while created is not True:
    if created == "cancel":
      centerprint_string("You input CANCEL. Cancelling account creation", "-")
      sleep(2)
      return ["login", None]
    match created:
      case "exists":
        error = "ERROR: ACCOUNT WITH THIS USERNAME ALREADY EXISTS"
      case "same":
        error = "ERROR: USERNAME AND PASSWORD CANNOT BE THE SAME"
    userin = get_screen_input("create_account_input.txt", make_dict(err=error))
    created = generate_account(userin)

  return ["login", None]
