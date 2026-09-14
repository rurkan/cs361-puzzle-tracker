# The file localdata/username exists solely as an unencrypted way to cache
# the current logged in user, so people don't have to sign back in every time
import os
import pandas as pd
from time import sleep

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

def account_exists(username):
    all_user_data = pd.read_csv('local_data/users_plaintext.csv')
    return all_user_data['username'].eq(username).any()

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
            'username': [user_data[0]],
            'password_plaintext': [user_data[1]]
        }
        pandas_data = pd.DataFrame(formatted_data)
        pandas_data.to_csv(
                            'local_data/users_plaintext.csv',
                            mode='a',
                            header=False,
                            index=False
                          )
        return True

def signin_valid(login_info):
    if login_info == "cancel":
        return "cancel"
    username = login_info[0].strip()
    password = login_info[1].strip()
    users = pd.read_csv('local_data/users_plaintext.csv')
    # Modification of Robin's answer to
    # https://stackoverflow.com/questions/24761133/pandas-check-if-row-exists-with-certain-values
    login_good = ((
            (users['username'] == (username)) & 
            (users['password_plaintext'] == (password))
            ).any().all())
    return(login_good)