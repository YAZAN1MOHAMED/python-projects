#chat gpt refactor my code into a class and further explain it

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        """
        Adds a task to the list.

        Parameters:
        None

        Returns:
        None
        """
        task = input("Write the task you want to add:\n")
        self.tasks.append(task)
        print("The task added successfully")

    def view_list(self):
        """
        Displays the tasks in the list.

        Parameters:
        None

        Returns:
        None
        """
        if not self.tasks:
            print("You don't have any tasks yet")
        else:
            for task in self.tasks:
                print(task)

    def delete_task(self):
        """
        Deletes a task from the list.

        Parameters:
        None

        Returns:
        None
        """
        if not self.tasks:
            print("There are no tasks to delete")
        else:
            task = input("What is the task name? (Case sensitive)\n")
            if task in self.tasks:
                self.tasks.remove(task)
                print("The task deleted successfully")
            else:
                print("There is no such a task")


def main():
    my_todo_list = ToDoList()
    print("Welcome to your to-do list app")
    while True:
        command = input(
            "Select a command from the following:\n (add, view, delete, exit)\n"
        )
        if command == "add":
            my_todo_list.add_task()
        elif command == "view":
            my_todo_list.view_list()
        elif command == "delete":
            my_todo_list.delete_task()
        elif command == "exit":
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
