import todo_modules

my_list = []
print("welcom to your to-do list app")
while True:
    command = input(
        "select a command from the following:\n (add, view, delete, exit)\n"
    )
    if command == "add":
        todo_modules.add_task(my_list)
    elif command == "view":
        todo_modules.view_list(my_list)
    elif command == "delete":
        todo_modules.delete_task(my_list)
    elif command == "exit":
        break
    else:
        print("invalid command")
"""
test cases I have checked:
use add command
use view command on a not empty list
use view command on an empty list
use delete command on a not existed element
use delete command on an existed element
use delete command on an empty list
use exit command

"""
