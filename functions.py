FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """Read our todo list from the current directory"""    
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the todo items to the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Yep")