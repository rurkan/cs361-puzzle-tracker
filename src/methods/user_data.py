# The file localdata/username exists solely as an unencrypted way to cache
# the current logged in user, so people don't have to sign back in every time
import os


def get_username():
    try:
        file = open("local_data/username", 'r', encoding = 'utf-8')
        usr = file.read()
        file.close()
        return usr
    except:
        return None
    
def user_signout():
    if(os.path.exists("local_data/username")):
        os.remove("local_data/username")
    else:
        print("ERROR, FILE COULD NOT BE DELETED")
        
def user_signin(usr):
    try:
        file = open("local_data/username", 'w', encoding = 'utf-8')
        file.write("rurkan")
        file.close()
    except:
        print("ERROR, FILE COULD NOT BE WRITTEN TO")
