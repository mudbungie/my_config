#!/usr/bin/env python3

from os import path
from shutil import copy, move

local_path = path.dirname(path.realname(__file__))

# Dict of files and where they go.
files = {
    '.vimrc':path.expanduser('~/.vimrc'),
    '.sqliterc':path.expanduser('~/.sqliterc'),
    '.bashrc':path.expanduser('~/.bashrc'),
    }

# Appends .bak to filename. Recursive.
def backup_file(filename):
    while path.exists(filename):
        backup_file(filename + '.bak')
        move(filename, filename + '.bak')

# Back up original, and then deploy the file.
def place_file(filename, destination):
    backup_file(destination)
    copy(local_path + filename, path)
    
if __name__ == '__main__':
    for filename, destination in files.items():
        place_file(filename, destination)
        print('Placed {}'.format(filename))
