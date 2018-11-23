#!/usr/bin/env python3
import subprocess
import os.path
from os import environ
from os import access, scandir
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PROMPT = "intek-sh$ "

def get_tree(current_dir=None):
        """ create a list of all files """
        tree = []
        for entry in os.scandir(current_dir):
            entry = entry.name
            tree.append(current_dir + '/' + entry)
            "Check if entry is a Sub Directory"
            if os.path.isdir(current_dir + '/' + entry) is True:
                for entry in get_tree(current_dir + '/' + entry):
                    tree.append(entry)
        return tree

def execute(filepath):
    fileExe = None
    if filepath.startswith('./'):
        for file in get_tree(CURRENT_DIR):
            if file[file.rfind('/'):] == filepath[1:]:
                if os.access(file, os.X_OK):
                    fileExe = file
    else:
        allpaths = os.environ['PATH'].split(':')
        for path in allpaths:
            for file in get_tree(path):
                if file[file.rfind('/')+1:] == filepath:
                    if os.access(file, os.X_OK):
                        fileExe = file

    if fileExe == None:
        print("bash:",filepath+':','command not found')
    else:
        popen = subprocess.Popen(fileExe)
        popen.wait()
    return


def cd(args):
    global CURRENT_DIR
    try:
        directory = args[1]
        if directory == '.':
            pass
        elif directory == '..':
            CURRENT_DIR = CURRENT_DIR[:CURRENT_DIR.rfind('/')]
        elif os.path.isdir(CURRENT_DIR + '/' + directory):
            CURRENT_DIR += '/' + directory
    except (IndexError):
        try:
            CURRENT_DIR = os.environ['HOME']
        except (KeyError):
            print("intek-sh: cd: HOME not set")

def export(string):
    args = string.split()
    for arg in args:
        pair = arg.split('=')
        os.environ[pair[0]] = pair[1]

def unset(var):
    try:
        os.environ.pop(var)
    except (KeyError):
        return

def printenv(args):
    if len(args) == 1:
        dict_ = dict(os.environ)
        for k,v in dict_.items():
            print(k+'='+v)
        return
    if args[1] in os.environ.keys():
        print(os.environ[args[1]])
    
def exits(args):
    try:
        if args[1].isalpha():
            print('exit')
            print('intek-sh: exit:')
        else:
            print('exit')
    except (IndexError):
        print('exit')
    

def prompt_input():
    try:
        raw_input = input(PROMPT)
    except (EOFError):
        return None
    return raw_input

def main():
    while True:
        try:
            raw_input = prompt_input()

            if raw_input == None:
                break


            args = raw_input.split()
            command = args[0]

            if command == 'cd':
                cd(args)
            elif command == 'pwd':
                print(CURRENT_DIR)
            elif command == 'export':
                export(args[1:])
            elif command == 'unset':
                unset(args[1])
            elif command == 'printenv':
                printenv(args)
            elif command == 'exit':
                exits(args)
            else:
                pass
        except (IndexError):
            pass


if __name__ == '__main__':
    main()
