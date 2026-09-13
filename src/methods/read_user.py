# The file localdata/username exists solely as an unencrypted way to cache
# the current logged in user, so people don't have to sign back in every time

def get_username():
    try:
        file = open("local_data/username", 'r', encoding='utf-8')
        return file.read()
    except:
        return None