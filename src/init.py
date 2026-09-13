from methods.clear import clearscreen
from methods.read_user import get_username
from interface import login_screen, main_menu


def main():
    print("Loading puzzles data file, please wait! This can take a while.")
    # In the future, this will load the puzzles data file
    # The message is to make sure users know it's frozen for a reason
    clearscreen()
    # Check if there's already a username file, if not, display login screen
    username = get_username()
    if(username != None):
        main_menu(username)
    elif(username == None):
        login_screen()
    else:
        print("Something went wrong, our bad. Investigate and try again.")
        exit()
        
main()