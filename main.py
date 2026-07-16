import json


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return tasks

    task_ids = [task.get("id", 0) for task in tasks]
    new_id = max(task_ids, default=0) + 1

    new_task = {
        "id": new_id,
        "title": title,
        "completed": False,
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return tasks


def update_task(tasks):
    if not tasks:
        print("No tasks to update.")
        return tasks

    task_id = input("Enter task ID to update: ").strip()
    try:
        target_id = int(task_id)
    except ValueError:
        print("Invalid task ID.")
        return tasks

    for task in tasks:
        if task.get("id") == target_id:
            new_title = input("Enter new title: ").strip()
            if not new_title:
                print("Task title cannot be empty.")
                return tasks
            task["title"] = new_title
            save_tasks(tasks)
            print("Task updated.")
            return tasks

    print("Task not found.")
    return tasks


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return tasks

    task_id = input("Enter task ID to delete: ").strip()
    try:
        target_id = int(task_id)
    except ValueError:
        print("Invalid task ID.")
        return tasks

    for index, task in enumerate(tasks):
        if task.get("id") == target_id:
            del tasks[index]
            save_tasks(tasks)
            print("Task deleted.")
            return tasks

    print("Task not found.")
    return tasks


def mark_task_completed(tasks):
    if not tasks:
        print("No tasks to mark as completed.")
        return tasks

    task_id = input("Enter task ID to mark as completed: ").strip()
    try:
        target_id = int(task_id)
    except ValueError:
        print("Invalid task ID.")
        return tasks

    for task in tasks:
        if task.get("id") == target_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
            return tasks

    print("Task not found.")
    return tasks


tasks = load_tasks()

while True:
    print("\nTask Manager Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice_input = input("Enter your choice (1-6): ")

    try:
        choice = int(choice_input)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        tasks = add_task(tasks)
    elif choice == 2:
        if tasks:
            print("Your tasks:")
            for task in tasks:
                status = "Done" if task.get("completed") else "Pending"
                print(f"- {task['id']}: {task['title']} [{status}]")
        else:
            print("No tasks yet.")
    elif choice == 3:
        tasks = update_task(tasks)
    elif choice == 4:
        tasks = delete_task(tasks)
    elif choice == 5:
        tasks = mark_task_completed(tasks)
    elif choice == 6:
        print("Exiting Task Manager...")
        break
    else:
        print("Invalid choice. Please select a number from 1 to 6.")