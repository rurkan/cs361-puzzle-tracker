from methods.clear import clearscreen
from methods.user_data import get_username
from interface import screen_select_handler


def main():
    screen_code = None
    print("Loading puzzles data file, please wait! This can take a while.")
    # In the future, this will load the puzzles data file
    # The message is to make sure users know it's frozen for a reason
    clearscreen()
    # Check if there's already a username file, if not, display login screen
    if(username != None):
        screen_code = "menu"
    elif(username == None):
        screen_code = "login"
    else:
        print("Something went wrong, our bad. Investigate and try again.")
        exit()
    data = [screen_code, username]
    while(True):
    # for i in range(0,10):
        data = screen_select_handler(data[0], data[1])


        

username = get_username()
main()