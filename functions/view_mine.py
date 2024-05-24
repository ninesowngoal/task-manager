DATETIME_STRING_FORMAT = "%Y-%m-%d"

def view_mine(task_list, curr_user, absolute_path, task_file):
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        for i,t in enumerate(task_list):
            if t['username'] == curr_user:
                disp_str = str(i + 1) + "." + f"Task: \t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Complete: \t {t['completed']}\n"
                disp_str += f"Task Description: \n {t['description']}\n"
                print(disp_str)
        
        while True:
             user_choice = input("Would you like to mark the task as complete or edit the task? Please type 'complete' or 'edit':")

             if user_choice == "complete":
                task_number = input("Which task would you like to mark as complete?: ")
                task_number = int(task_number)
                task_number = task_number - 1
                task_list[task_number]["completed"] = True
                with open("{}/tasks.txt".format(absolute_path), "w+") as task_file:
                    task_list_to_write = []
                    for t in task_list:
                        str_attrs = [
                        t['username'],
                        t['title'],
                        t['description'],
                        t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if t['completed'] else "No"
                        ]
                    task_list_to_write.append(";".join(str_attrs))
                    task_file.write("\n".join(task_list_to_write))
                break