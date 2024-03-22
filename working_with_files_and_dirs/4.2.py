import os.path


def grep(path):
    dirs, files = [], []
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)):
            dirs.append(f)
        else:
            files.append(f)
    return dirs, files


def del_dir(path):
    if os.path.isdir(path) == False:
        return False
    dirs, files = grep(path)
    if len(dirs) != 0:
        return False
    for fi in files:
        os.remove(path + '/' + fi)
    os.rmdir(path)
    if os.path.isdir(path) == False:
        return True
    return False

print(del_dir('/home/andreewanya/Документы/Bobrovsky/py1/graduate-programming-school/working_with_files_and_dirs/New-folder'))         # Вернет Fasle, так как есть вложенная директория New-folder2
print(del_dir('/home/andreewanya/Документы/Bobrovsky/py1/graduate-programming-school/working_with_files_and_dirs/New-folder/New-folder2'))         # Вернет True, так как нет вложенных директорий, но есть вложенные файлы


