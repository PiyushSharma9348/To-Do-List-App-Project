import json

class Task:
  def __init__(self, description):
      self.description = description
      self.completed = False

  def mark_completed(self):
      self.completed = True

  def __str__(self):
      status = "Completed" if self.completed else "Not Completed"
      return f"{self.description} - {status}"

import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Invalid task number")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task number")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            tasks_data = [{'description': task.description, 'completed': task.completed} for task in self.tasks]
            
            json.dump(tasks_data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(task['description']) for task in tasks_data]
                for task, data in zip(self.tasks, tasks_data):
                    if data['completed']:
                        task.mark_completed()
        except FileNotFoundError:
            print("No saved tasks found.")

def main():
    todo_list = ToDoList()
    todo_list.load_from_file('tasks.json')

    while True:
        print("\nTo-Do List Application")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Save tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == '4':
            todo_list.view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.save_to_file('tasks.json')
            print("Tasks saved successfully.")
        elif choice == '6':
            todo_list.save_to_file('tasks.json')
            print("Tasks saved. Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
