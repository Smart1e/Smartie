import os

#Find the path of this file
def find_file():
    

    import os
    path = os.path.dirname(os.path.abspath(__file__))
    path = str(path)
    path.replace('/delete_code.py', '')
    os.path(path)
    return path


