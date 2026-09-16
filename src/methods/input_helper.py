from methods.clear import clearscreen
from methods.print_helper import print_with_modifiers, printwrap


def display_screen(lines, data=None):
  clearscreen()
  return_data = []
  for line in lines[1:]:
    # If the line is blank or has no modifiers, just print
    if len(line) == 0:
      printwrap(line)
      continue

    # If the line has modifiers. See modifiers belo
    # Start with " " for center, "-" for hyphen spacer, or ">" for user input
    # or begin a word (not line) with "$" for a variable
    modifiers = []

    if "$error" in line:
      modifiers.append("$error")
    if "$username" in line:
      modifiers.append("$username")
    if "$puzzleid" in line:
      modifiers.append("$puzzleid")
    if "$board" in line:
      modifiers.append("$board")
    if "$previous_move" in line:
      modifiers.append("$previous_move")
    if "$num_puzzles" in line:
      modifiers.append("$num_puzzles")
    if "$themes" in line:
      modifiers.append("$themes")
    if line[0] == "-":
      modifiers.append("-")
    if line[0] == " ":
      modifiers.append(" ")
    if line[0] == ">":
      modifiers.append(">")

    val = print_with_modifiers(line, modifiers, data)
    if ">" in modifiers:
      if val == "cancel":
        return val
      return_data.append(val)
  if not ">" in modifiers:
    return_data = input(
      "Input Move: " if "$board" in lines else "Option Select: "
    ).lower()
  return return_data


def get_screen_input(filepath, data):

  with open(filepath, "r", encoding="utf-8") as file:
    lines = file.read().splitlines()

  options = lines[0].split()
  userin = display_screen(lines, data)

  if type(userin) is not list:
    while userin.lower() not in options:
      if "cancel" in options:
        return userin
      data["$error"] = "PLEASE INPUT A SELECTION FROM THE OPTIONS AVAILABLE"
      userin = display_screen(lines, data)

  elif len(userin) > 2 and userin[1] != userin[2]:
    while "cancel" not in userin and userin[1] != userin[2]:
      data["$error"] = "PASSWORDS DO NOT MATCH. PLEASE TRY AGAIN"
      userin = display_screen(lines, data)

  return userin
