from decorators.log_action import log_action

class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = tasks if tasks is not None else [] 
        if not isinstance(self.tasks, list):
            raise ValueError("Tasks should be a list!")
        
    @log_action("Add Task")
    def add_task(self, task_name):
        self.tasks.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added.")

    @log_action("Mark Task as Completed")
    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Task '{self.tasks[task_index]['name']}' marked as completed.")
        else:
            print("Invalid task index.")
            raise ValueError("Task index out of range.")

    @log_action("View Tasks")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for idx, task in enumerate(self.tasks):
                status = "✓" if task["completed"] else "✗"
                print(f"{idx}. {task['name']:5} [{status}]")