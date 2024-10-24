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

tasks = []


def add_tasks():
    """
    Adds a new task to the task list.

    The function prompts the user to input tasks, checks if the input is valid (non-empty),
    and appends the task to the global 'tasks' list. It will continue to prompt the user
    to add another task until they choose 'n' for no.
    Args:
        None
    Returns:
        None
    Raises:
        ValueError: If an error occurs during input handling.
    """
    while True:
        try:
            new_task = input("Please add a task: ").strip()
            if not new_task:
                print("Invalid input. Task cannot be empty. Try again!")
                continue

            tasks.append(new_task)
            print(f"{new_task} successfully added.")

            while True:
                another_task = input("Would you like to add another task? y/n: ").strip().lower()
                if another_task == "y":
                    break
                elif another_task == "n":
                    return
                else:
                    print("Invalid choice. Try again!")
        except ValueError:
            print("An error occurred. Please try again!")


def view_tasks():
    """
    Displays all tasks currently in the task list.

    If no tasks are present, it informs the user that there are no tasks available.
    Otherwise, it enumerates and prints the list of tasks.
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
            print(f"{index}. {task}")


def mark_task_complete():
    """
    Marks a specified task as complete by adding a checkmark (✅) next to it.

    The user is prompted to input the task number they wish to mark as complete.
    The function validates the task number and updates the task with the checkmark.
    Args:
        None
    Returns:
        None
    Raises:
        ValueError: If the user input cannot be converted to an integer.
    """
    view_tasks()

    try:
        task_to_complete = int(input("\nWhich task do you want to complete? ")) - 1

        if 0 <= task_to_complete < len(tasks):
            tasks[task_to_complete] = f"{tasks[task_to_complete]} ✅"
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
        other errors occur during input handling.
    """
    view_tasks()

    while True:
        try:
            task_to_delete = input("\nWhich task do you want to delete? ").strip()

            if not task_to_delete.isdigit():
                print(f"Invalid input. Enter a valid number from 1 to {len(tasks)}.")
                continue

            task_index = int(task_to_delete) - 1

            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                print(f"'{deleted_task}' successfully deleted.")
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
