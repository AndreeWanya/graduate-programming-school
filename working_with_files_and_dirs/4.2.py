import os.path

def del_dir(path):
    if os.path.isdir(path) == False:
        return False
    counter = 0
    for root, dirs, files in os.walk(path):
        counter += 1
        if counter == 2:
            return False
        files = files
    for fi in files:
        os.remove(path + '/' + fi)
    os.rmdir(path)
    if os.path.isdir(path) == False:
        return True
    return False

print(del_dir('/home/andreewanya/Документы/Bobrovsky/py1/graduate-programming-school/working_with_files_and_dirs/New-folder'))         # Вернет Fasle, так как есть вложенная директория New-folder2
print(del_dir('/home/andreewanya/Документы/Bobrovsky/py1/graduate-programming-school/working_with_files_and_dirs/New-folder/New-folder2'))         # Вернет True, так как нет вложенных директорий, но есть вложенные файлы


