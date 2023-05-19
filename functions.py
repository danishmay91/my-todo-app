FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def get_userinput():
    """ Asks users to input what activity they want to perform? """
    user_action_local = input("Type add, show, edit, complete or exit: ")
    user_action_local = user_action_local.strip()
    return user_action_local


def write_userinput(user_input, filepath=FILEPATH):
    """" Write to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(user_input)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())



