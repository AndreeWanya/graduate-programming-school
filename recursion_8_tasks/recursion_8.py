import os.path

def grep(path: str) -> list:
    dirs, files = [], []
    return grep_recursion(path, dirs, files, -1)

def grep_recursion(path: str, dirs: list, files: list, ind: int) -> list:
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)):
            dirs.append(os.path.join(path, f))
        else:
            files.append(f)
    ind += 1
    if ind == len(dirs):
        return files
    return grep_recursion(dirs[ind], dirs, files, ind)

# print(grep('./'))
