tasks = ["Wash dishes", "Grocery shopping"]

def display_menu():
    print("To-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Quit")
    choice = input("Choose an option (1-4): ")
    return choice
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")
def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully.")
            else:
                print("Error: Invalid task number.")
        except ValueError:
            print("Error: Please enter a valid number.")
def quit_application():
    print("Exiting the To-Do List Application. Goodbye!")
    
def main():
    while True:
        choice = display_menu()
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            quit_application()
            break
        else:
            print("Error: Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()
            
            