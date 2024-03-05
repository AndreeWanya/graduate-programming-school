from random import randint

def create_files():
    for i in range(1, 10):
        file_name = 'new_files/' + str(i) + '.txt'
        fi = open(file_name, 'wt')
        for j in range(3):
            fi.write(str(randint(1, 100)) + '\n')
        fi.close()

create_files()
