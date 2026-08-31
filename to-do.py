tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Add Task
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, item in enumerate(tasks, start=1):
                status = "✓" if item["completed"] else "✗"
                print(f"{i}. [{status}] {item['task']}")

    # Complete Task
    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']}")

            try:
                task_number = int(input("Enter task number to complete: "))

                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["completed"] = True
                    print("Task completed!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Delete Task
    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']}")

            try:
                task_number = int(input("Enter task number to delete: "))

                if 1 <= task_number <= len(tasks):
                    deleted_task = tasks.pop(task_number - 1)
                    print(f"Deleted: {deleted_task['task']}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Exit
    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please select 1-5.")