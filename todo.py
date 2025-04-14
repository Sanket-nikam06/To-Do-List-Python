todo_list = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(todo_list):
            status = "✅" if task['done'] else "❌"
            print(f"{idx + 1}. {task['task']} [{status}]")

def add_task():
    task = input("Enter your new task: ")
    todo_list.append({'task': task, 'done': False})
    print("Task added successfully!")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        removed = todo_list.pop(index)
        print(f"Task '{removed['task']}' removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        todo_list[index]['done'] = True
        print(f"Task '{todo_list[index]['task']}' marked as done.")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_done()
    elif choice == '5':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
