from services.TaskManager import TaskManager

def main():
    manager = TaskManager([
        {'name': 'task1', 'completed': False},
        {'name': 'task2', 'completed': True},
        # {'namee': 'task3', 'completed': True} # KeyError: 'name'
        # {'name': 'task4', 'completed': true} # NameError: name 'true' is not defined.
    ])

    while True:
        print("\nPyTask Manager")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            manager.add_task(task_name)
        elif choice == "2":
            try:
                task_index = int(input("Enter task index to mark as completed: "))
                manager.complete_task(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            manager.view_tasks()
        elif choice == "4":
            print("Exiting PyTask Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()