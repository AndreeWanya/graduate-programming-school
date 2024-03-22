import os.path
import logging


def grep(path):
    dirs, files = [], []
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)):
            dirs.append(f)
        else:
            files.append(f)
    return dirs, files


def if_flag(path, file_extension, flag):
    my_list = list(grep(path))
    logging.warning(f'dirs = {my_list[0]}, files = {my_list[1]}')
    if flag == True:
        dirs, files = [], []
        for di in my_list[0]:
            dirs_list, files_list = grep(path + '/' + di)
            logging.warning(f'new dirs = {dirs_list}, new files = {files_list}')
            dirs += dirs_list
            files += files_list
        my_list[0] += dirs
        my_list[1] += files
    my_list[1] = [fi for fi in my_list[1] if fi.split('.')[-1] == file_extension or file_extension == '*']
    return my_list


def del_dir(path):
    if os.path.isdir(path) == False:
        return False
    dir_list = if_flag(path, '*', False)
    if len(dir_list[0]) != 0:
        return False
    for fi in dir_list[1]:
        os.remove(path + '/' + fi)
    os.rmdir(path)
    return True

print(del_dir('/home/andreewanya/Документы/Bobrovsky/py1/graduate-programming-school/working_with_files_and_dirs/New-folder'))         # Вернет Fasle, так как есть вложенная директория New-folder2
print(del_dir('/home/andreewanya/Документы/Bobrovsky/py1/graduate-programming-school/working_with_files_and_dirs/New-folder/New-folder2'))         # Вернет True, так как нет вложенных директорий, но есть вложенные файлы


