import json, sys, os

def getSMTPUsernamePassword(config_file_paths=[]):
    config_dict = {}
    for i in config_file_paths:
        try:
            file = open(i)
            config_dict = json.load(file)
            break
        except FileNotFoundError:
            continue

    if len(config_dict)==0:
        sys.exit("Proper config file not found. Make sure you have a sportsRoom.conf file, and also pass its proper path")
    if not 'smtp' in config_dict:
        sys.exit("No SMTP configs found in the configure file")
    if not (('username' in config_dict['smtp']) and ('password' in config_dict['smtp'])):
        sys.exit("Username or password not found in 'smtp' in config file")
    if ((config_dict['smtp']['username']=="") or (config_dict['smtp']['password']=="")):
        sys.exit("Empty username or password, in config file")

    return (config_dict['smtp']['username'],config_dict['smtp']['password'])

def getDataBasePath(db_paths_list=[]):
    is_available = False
    is_avail = 0
    for i in db_paths_list:
        try:
            is_avail += 1
            file = open(i)
            is_available = True
            break
        except FileNotFoundError:
            continue
        except:
            sys.exit("Unknown exception while reading database")
    if not is_available:
        print("No valid DB found at any of the given paths, trying to create new DB")
        try:
            file = open(db_paths_list[0],'w')
            os.system("python3 manage.py makemigrations")
            os.system("python3 manage.py migrate")
        except:
            os.remove(db_paths_list[0])
            sys.exit("Cannot create a new database")
        return db_paths_list[0]
    return db_paths_list[is_avail-1]
