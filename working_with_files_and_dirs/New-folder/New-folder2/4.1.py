import os.path
import logging

def grep(path):
    for root, dirs, files in os.walk(path):
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
    my_list[1] = [fi for fi in my_list[1] if fi.split('.')[-1] == file_extension]
    return my_list

print(if_flag('./', 'txt', False))
