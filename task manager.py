# - prevents the generation of __pycache__ files
import sys
sys.dont_write_bytecode = True

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"
absolute_path = os.path.dirname(__file__) # - obtain absolute path for directory.

# - Create tasks.txt if it doesn't exist
if not os.path.exists("{}/tasks.txt".format(absolute_path)):
    with open("{}/tasks.txt".format(absolute_path), "w") as default_file:
        pass

with open("{}/tasks.txt".format(absolute_path), 'r') as task_file:
    '''count = 0
    for line in task_file:
        if line != "\n":
            count += 1'''
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

#task_number = print(int(0 if count is None else count))
task_list = []

for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if os.path.isfile("{}/user.txt".format(absolute_path)) == False:
    with open("{}/user.txt".format(absolute_path), "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("{}/user.txt".format(absolute_path), 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

#====Login section====
logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

#=====import functions==============
from functions import *

#========Task manager menu and functions========
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following options below:
r - Register a user
a - Add a task
va - View all tasks
vm - View my task
ds - Display statistics
e - Exit
: ''').lower()
    
    if menu == 'r':
        reg_user.reg_user(username_password, absolute_path)
    elif menu == 'a':
        while True:
            #print("There are currently {} tasks.".format(task_number)) # currently prints None even though there is one task. Fix feature or remove later.
            user_add_choice = input("Would you like to add a new task?: ")

            if user_add_choice == 'no' or user_add_choice == 'n':
                break
            elif user_add_choice == 'yes' or user_add_choice == 'y':
                add_task.add_task(username_password, absolute_path, task_list)
                break
    elif menu == 'va':
        view_all.view_all(task_list)
    elif menu == 'vm':
        view_mine.view_mine(task_list, curr_user, absolute_path, task_file)