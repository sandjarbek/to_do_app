FILEPATH = 'todos.txt'
import os
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_org, filepath=FILEPATH):
    """Write todos in the list"""
    with open(filepath, 'w') as file:
        file.writelines(todos_org)


print("I am outside")
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
