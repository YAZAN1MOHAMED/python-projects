def add_task(your_list: list):
    task = input("write the task you want to add:\n")
    your_list.append(task)
    print("the task added successfully")


def view_list(your_list: list):
    if not your_list:
        print("You don't have any tasks yet")
    else:
        for task in your_list:
            print(task)


def delete_task(your_list: list):
    if not your_list:
        print("there are no tasks to delete")
    else:
        task = input("What is the task name?(Case sensitive)\n")
        if your_list.__contains__(task):
            your_list.remove(task)
            print("the task deleted successfully")
        else:
            print("there is no such a task")
