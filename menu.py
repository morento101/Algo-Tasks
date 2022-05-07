"""Menu implementation"""

from inspect import signature
from sys import exit
from os import system

from tasks.tasks import *


data_dict = {key: func for key, func in locals().items()
             if key.startswith("task_")}

logo_str = "     __   __     ___   __   ____   __   ____  __ _  ____ \n" + \
           "    / _\ (  )   / __) /  \ (_  _) / _\ / ___)(  / )/ ___)\n" + \
           "   /    \/ (_/\( (_ \(  O )  )(  /    \\\\___ \ )  ( \___ \\\n" + \
           "   \_/\_/\____/ \___/ \__/  (__) \_/\_/(____/(__\_)(____/"


def pretify_func_name(func_name: str) -> str:
    """
    Make name of the function prettier
    """
    return func_name[5:]


def pretify_doc(doc: str) -> str:
    """
    Make description of the function prettier
    """
    if doc[-1] == '\n':
        return doc.replace("    ", "")
    return doc.replace("    ", "") + '\n'


def clear_screen() -> None:
    """
    Clear screen from symbols
    """
    system('cls||clear')


def print_logo() -> None:
    """
    Print app logo
    """
    print(logo_str)
    print("*" * 60)


def print_task_desc(func) -> None:
    """
    Print task description
    """
    print_logo()
    print(pretify_doc(func.info))


def print_result(result) -> None:
    """
    Print answer of the function
    """
    if not result:
        print("Result: -")
    else:
        print("Result:", *result)


def print_menu(data_dict: dict) -> None:
    """
    Print the main menu with logo
    """
    print_logo()
    print("Choose one of the available tasks:")
    for key, value in enumerate(data_dict, 1):
        print(pretify_func_name(value), end=" \t ")
        if not key % 7:
            print()
    print("\nOr type 'exit' or 'e' to terminate app.")



def main(data_dict: dict):
    """
    Main function for menu implementation
    """

    while True:
        clear_screen()
        print_menu(data_dict)

        while True:

            try:
                user_input = input(">>> ")

                if user_input == "e" or user_input == "exit":
                    exit()

                func = data_dict[f"task_{user_input}"]
                break

            except KeyError as ex:
                if user_input:
                    print(f"Input correct task number, task {ex} does not exist: ")
                continue

        while True:
            clear_screen()
            expected_args_count = len(signature(func).parameters)
            if expected_args_count < 1:
                print_task_desc(func)
                print_result(func())
                print("\nPress any key to return back")
                input(">>> ")
                break
            else:
                while True:
                    print_task_desc(func)
                    print("Enter the arguments to get the answer. Type")
                    print("'return' or 'r' to get back to the menu.")
                    print("Or type 'exit' or 'e' to terminate app.\n")

                    while True:
                        try:
                            user_input = input(">>> ")

                            if user_input == "exit" or user_input == "e":
                                exit()


                            args = [int(arg) for arg in user_input.split(" ")
                                    if (arg.isnumeric() and (int(arg) > 0))]
                            print_result(func(*args))

                        except (TypeError, AssertionError):
                            if user_input:
                                print(f"The type or number of arguments is not suitable"
                                f" for this task. Please, try again.")
                            continue

                        finally:
                            if user_input == "return" or user_input == "r":
                                break
                    break
                break


if __name__ == "__main__":
    main(data_dict)
