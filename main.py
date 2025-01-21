MENU = """
*****TASKS MENU*****
--------------------
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Exit the program
--------------------
"""

tasks = []  # A list of dictionaries to store tasks and their priorities


def add_tasks():
    """
    Adds a new task with a priority level to the tasks list.

    The function prompts the user to input tasks and their priority level.
    Tasks are stored in the global 'tasks' list as dictionaries containing the task description and priority.
    Args:
        None
    Returns:
        None
    Raises:
        ValueError: If an error occurs during input handling.
    """
    while True:
        try:
            # Get task description
            new_task = input("Please add a task: ").strip()
            if not new_task:
                print("Invalid input. Task cannot be empty. Try again!")
                continue

            # Get priority level and validate
            while True:
                priority = input("Please specify the priority level: High, Medium, or Low: ").strip().capitalize()
                if priority in {"High", "Medium", "Low"}:
                    break
                else:
                    print("Invalid priority level. Please enter High, Medium, or Low.")

            # Add task to the global list
            tasks.append({"task": new_task, "priority": priority})
            print(f"Task '{new_task}' with priority '{priority}' successfully added.")

            # Ask if the user wants to add another task
            another_task = input("Would you like to add another task? y/n: ").strip().lower()
            if another_task == "n":
                return
            elif another_task != "y":
                print("Invalid choice. Returning to the menu.")
                return
        except ValueError:
            print("An error occurred. Please try again!")


def view_tasks():
    """
    Displays all tasks currently in the task list.

    If no tasks are present, it informs the user that there are no tasks available.
    Otherwise, it enumerates and prints the list of tasks, with the checkmark (✅)
    displayed after the priority for completed tasks.
    Args:
        None
    Returns:
        None
    Raises:
        None
    """
    if not tasks:
        print("There are no tasks available.")
    else:
        print("TO-DO List")
        print("-" * 11)
        for index, task in enumerate(tasks, 1):
            task_display = task["task"]
            priority_display = f"({task['priority']})"

            # Append ✅ after the priority if the task is complete
            if "✅" in task_display:
                print(f"{index}. {task_display.replace(' ✅', '')} {priority_display} ✅")
            else:
                print(f"{index}. {task_display} {priority_display}")


def mark_task_complete():
    """
    Marks a specified task as complete by adding a checkmark (✅) next to it.

    The user is prompted to input the task number they wish to mark as complete.
    The function validates the task number and updates the corresponding task.
    Args:
        None
    Returns:
        None
    Raises:
        ValueError: If the user input cannot be converted to an integer.
    """
    view_tasks()  # Display tasks

    if not tasks:
        print("No tasks to mark as complete.")
        return

    try:
        # Prompt the user to select a task
        task_to_complete = int(input("\nWhich task do you want to complete? ")) - 1

        if 0 <= task_to_complete < len(tasks):
            # Check if the task is already marked as complete
            if "✅" in tasks[task_to_complete]["task"]:
                print(f"Task {task_to_complete + 1} is already marked as complete.")
            else:
                # Mark the task as complete
                tasks[task_to_complete]["task"] += " ✅"
                print(f"Task {task_to_complete + 1} marked as complete!")
        else:
            print("Invalid task number! Please try again.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    """
    Deletes a specified task from the task list.

    The user is prompted to input the task number they wish to delete.
    The function validates the task number and removes the corresponding task from the list.
    Args:
        None
    Returns:
        None
    Raises:
        ValueError: If the user input cannot be converted to an integer or
        if other errors occur during input handling.
    """
    if not tasks:
        print("There are no tasks to delete.")
        return

    view_tasks()  # Display the current tasks

    while True:
        try:
            task_to_delete = input("\nWhich task do you want to delete? ").strip()

            if not task_to_delete.isdigit():
                print(f"Invalid input. Enter a valid number from 1 to {len(tasks)}.")
                continue

            task_index = int(task_to_delete) - 1

            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                print(f"Task '{deleted_task['task']}' successfully deleted.")
                break
            else:
                print(f"Invalid number. Please enter a number from 1 to {len(tasks)}.")
        except ValueError:
            print("An error occurred. Please try again.")


def main():
    """
    Main function that runs the To-Do List program.

    It displays a menu of options to the user and processes their choice accordingly.
    The user can add tasks, view tasks, mark tasks as complete, delete tasks, or exit the program.
    Args:
        None
    Returns:
        None
    Raises:
        ValueError: If the user input cannot be converted to an integer when selecting a menu option.
    """
    while True:
        try:
            print(MENU)
            choice = int(input("Please choose a number (1-5): "))
            print()

            if choice == 1:
                add_tasks()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
