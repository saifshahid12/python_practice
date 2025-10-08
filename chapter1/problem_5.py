
            # using chatgpt just change the path in last which is directory path

import os

def list_dir_contents(path="."):
    """
    Print the names of all entries (files + directories) in the directory given by path.
    If path is not given, use the current directory.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The directory {path} does not exist.")
        return

        # we give path as we want our own choice

    except NotADirectoryError:
        print(f"Error: {path} is not a directory.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access {path}.")
        return

        # the path here is also given in coding in variable entries for name 
        
    print(f"Contents of directory '{path}':")
    for name in entries:
        print(name)


if __name__ == "__main__":
    # You can replace "." with any path you like
    list_dir_contents("/")
