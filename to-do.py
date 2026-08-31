tasks = []


# Add a task
def add_task():
    task = input("Enter a task: ")

    if task.strip():
        tasks.append(task)
        print("✅ Task added successfully!")
    else:
        print("❌ Task cannot be empty.")


# View all tasks
def view_tasks():
    if not tasks:
        print("📭 No tasks available.")
        return

    print("\n----- To-Do List -----")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


# Update a task
def update_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to update: "))

        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the new task: ")

            if new_task.strip():
                tasks[task_number - 1] = new_task
                print("✅ Task updated successfully!")
            else:
                print("❌ Task cannot be empty.")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


# Remove a task
def remove_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"✅ Removed: {removed_task}")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


# Main menu
while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        remove_task()

    elif choice == "5":
        print("👋 Thank you for using the To-Do List!")
        break

    else:
        print("❌ Invalid choice. Please select 1-5.")
