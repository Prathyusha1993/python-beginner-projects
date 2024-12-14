# program to create simple text editor
# allows to open an existing text file or create new
# edit the content and then save changes by typing save

import os
from importlib.resources import contents


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def write_file(filename, content):
    with open(filename, 'w') as file:
        return file.write(content)


def get_user_input():
    print('Enter your text (type SAVE on a new line to save and exist): ')

    lines= []
    while True:
        line = input()
        if line == 'SAVE':
            break
        lines.append(line)

    return '\n'.join(lines)


def main():
    filename = input('Enter the file to open or create: ').strip()
    try:
        if os.path.exists(filename):
            print(read_file(filename))
        else:
            write_file(filename, ' ')

        content = get_user_input()
        write_file(filename, content)
        print(f'{filename} saved.')
    except OSError:
        print(f'{filename} could not be opened.')


main()