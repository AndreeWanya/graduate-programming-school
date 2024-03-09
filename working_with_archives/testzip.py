import os.path
from zipfile import ZipFile

def zip_file(zip_name, ext):
    with ZipFile(zip_name, 'w') as zipf:
        for root, dirs, files in os.walk('.'):
            for f in files:
                if f.endswith(ext):
                    zipf.write(f)
    return zipf

zip_file('testzip.zip', '.txt')
with ZipFile('testzip.zip', 'r') as zipf:
    print(zipf.namelist())
