from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def view_all(task_list):
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling) 
    '''
    for i,t in enumerate(task_list):
        disp_str = str(i + 1) + "." + f"Task: \t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Complete: \t {t['completed']}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)