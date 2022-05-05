"""Menu implementation"""

import re
from inspect import signature

from tasks.tasks import *


data_dict = locals()


def pretify_doc(doc: str) -> str:
    """
    This makes code beautiful
    """
    if doc[-1] == '\n':
        return doc
    return doc + '\n'


def main(data_dict: dict):
    """
    Menu implementation
    """
    # Dictionary of tasks. Key - task number, value - function of that task
    tasks_dict = data_dict

    # Main loop
    while True:

        print("Type 'exit' to stop program execution")
        # Print available tasks
        print("*" * 24, "MAIN MENU", "*" * 25)
        print("Available tasks: ")
        for key, value in enumerate(tasks_dict):
            if value.startswith("task_"):
                print(value, end=", ")
                if not key % 5:
                    print()
        print("\n")
        print("*" * 60)

        try:
            task_number = input("Input task`s number: ")
            # Exit from main loop
            if task_number == "exit":
                break

            # Get the module by input
            func = tasks_dict[f"task_{task_number}"]

        except KeyError as ex:
            print(f"Input correct task`s number, task {ex} does not exist: ")
            continue

        # Task loop
        while True:
            try:
                # Get number of arguments needed for task run() function
                expected_args_count = len(signature(func).parameters)
                if expected_args_count < 1:
                    # Show module info & call function without arguments
                    print("-" * 60)
                    print(func.info.replace("    ", ""))
                    print("-" * 60)
                    print("Result: ", func())
                    break
                else:
                    # Show module info & get arguments (or "exit" key)
                    print("-" * 60)
                    print("Type 'return' to return to the main menu")
                    user_input = input(pretify_doc(func.info.replace("    ", "")))
                    # Exit from task loop
                    if user_input == "return":
                        break
                    # Get arguments (you validation function could be here)
                    args = [int(arg) for arg in user_input.split(" ")
                            if (arg.isnumeric() and (int(arg) > 0))]
                    # Validate number of parameters
                    # assert(expected_args_count == len(args))

                    print("-" * 60)

                    # Get the result
                    print("Result: ", func(*args))

            except (TypeError, AssertionError):
                print("-" * 60)
                print(f"The type or number of arguments is not suitable"
                      f" for this task. Pleas try again.")
                continue


if __name__ == "__main__":
    main(data_dict)
