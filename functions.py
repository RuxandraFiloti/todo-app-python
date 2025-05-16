FILEPATH = 'todos.txt'

def get_todos(filepath = FILEPATH):
    """Read the texe file and return the list of to-do items""" #docstrings
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

#print(help(get_todos)) #arata ce am scris in docstrings

def write_todos(todos_arg, filepath = FILEPATH):
      with open(filepath, 'w') as file:
                file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos()) 