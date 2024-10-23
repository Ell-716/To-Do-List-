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

    if not tasks:
        print("There are no tasks available.")
    else:
        print("TO-DO List")
        print("-" * 11)
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
