def reg_user(username_password, absolute_path):
    while True:
        new_username = input("New Username: ")

        with open("{}/user.txt".format(absolute_path), "r") as out_file:
            # - read file content
            contents = out_file.read()
            # - check if username already present
            if new_username in contents:
                print("That username is already in use.")
                continue
            # - breaks loop if username not found.
            else:
                break
    
    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")
    
    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added.")
        username_password[new_username] = new_password
            
        with open("{}/user.txt".format(absolute_path), "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))
    # - Otherwise you present a relevant message.
    else:
        print("Passwords do not match.")