#Find the path of this file
def find_save_file():
    import os
    #path = os.path.dirname(os.path.abspath(__file__))
    path = __file__
    path = str(path)
    print('1', path)
    path = path.replace('/Smartie/Smart/Data/uninstall.py', '')
    print('2', path)
    os.path.join(path)
    print('3', path)
    return path

#find actual file path for delete_code.py
def find_delete_file():
    import os
    print('4', __file__)
    path = __file__
    #path = os.path.dirname(os.path.abspath(__file__))
    path = str(path)
    print('5', path)
    path.replace('uninstall.py', 'deleted_code.py')
    print('6', path)
    path = os.path.join(path)
    print('7', path)
    return path

def copy_file(file, new_file):
    import shutil
    shutil.copy(file, new_file)
    
save_path = find_save_file()
delete_file_path = find_delete_file()
print('8', save_path)
print('9', delete_file_path)
print(f'#####################\n{save_path}\n#####################\n{delete_file_path}\n#####################')
try:
    copy_file(delete_file_path, save_path)
except:
    print('error 1')
    

copy_file(save_path, delete_file_path)


