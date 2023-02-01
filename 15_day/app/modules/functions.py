def get_todos(filepath='files/todos.txt'):
    """ Read a text file and return the list of
        to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='files/todos.txt'):
    """ Write the to-do items list to a text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos('../files/todos.txt'))
