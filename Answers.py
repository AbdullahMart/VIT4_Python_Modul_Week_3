# Task list
tasks = []
deleted_tasks = []

# Function to add a task
def add_task(task_name, status="Pending"):
    if status not in ["Pending", "Completed"]:
        print("Invalid status!")
        return
    task = {
        "Sequence Number": len(tasks) + 1,
        "Task Name": task_name,
        "Status": status
    }
    tasks.append(task)
    print("New task added:", task_name, "- Status:", status)
    
# Function to mark a task as completed
def complete_task(task_number):
    if task_number <= len(tasks):
        tasks[task_number - 1]["Status"] = "Completed"
        print("Task completed:", tasks[task_number - 1]["Task Name"])
    else:
        print("Invalid task number")

# Function to delete a task
def delete_task(task_number):
    if task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        deleted_tasks.append(deleted_task)
        print("Task deleted:", deleted_task["Task Name"])
    else:
        print("Invalid task number")

# Function to list all tasks
def list_all_tasks():
    if tasks:
        print("All Tasks:")
        for task in tasks:
            print(task["Sequence Number"], "-", task["Task Name"], "-", task["Status"])
    else:
        print("No tasks found.")

# Function to list deleted tasks
def list_deleted_tasks():
    if deleted_tasks:
        print("Deleted Tasks:")
        for task in deleted_tasks:
            print(task["Sequence Number"], "-", task["Task Name"], "-", "Deleted")
    else:
        print("No deleted tasks found.")

# Main loop
while True:
    print("\nTask Manager\n")
    print("1. Add a new task")
    print("2. Mark a task as completed")
    print("3. Delete a task")
    print("4. List all completed tasks")
    print("5. List all tasks (including deleted ones)")
    print("6. Exit")


    choice = input("Please select an action: ")

    if choice == "1":
        task_name = input("Enter the name of the new task: ")
        status_input = input("Enter the status of the task 'Completed' or 'Pending' (default is 'Pending'): ").capitalize()
        if status_input:
            add_task(task_name, status_input)
        else:
            add_task(task_name)
    elif choice == "2":
        task_number = int(input("Enter the number of the completed task: "))
        complete_task(task_number)
    elif choice == "3":
        task_number = int(input("Enter the number of the task to be deleted: "))
        delete_task(task_number)
    elif choice == "4":
        list_completed_tasks()
    elif choice == "5":
        list_all_tasks()
        list_deleted_tasks()  # Include deleted tasks in the list
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid action. Please try again.")
