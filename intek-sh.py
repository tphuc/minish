#!/usr/bin/env python3
import subprocess
import os.path
from os import environ
from os import access, scandir
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PROMPT = "intek-sh$ "


def execute(args):
    found = None
    filepath = " ".join(args)
    if filepath.startswith('./'):
        for file in os.scandir(CURRENT_DIR):
            file = file.name
            if file.endswith(filepath[2:]):
                found = filepath
    else:
        try:
            allpaths = os.environ['PATH'].split(':')
            for path in allpaths:
                for file in os.scandir(path):
                    file = file.name
                    if file.endswith(filepath):
                        found = file
        except (KeyError):
            pass
    

    if found is not None:
        if not os.access(found, os.X_OK):
<<<<<<< HEAD
            print("intek-sh:",filepath+':','Permission denied')
=======
            print("intek-sh:",found+':','Permission denied')
>>>>>>> 981045240c14840f8f4c4b59d29b6ae2df05f621
        else:
            subprocess.run(found)

    else:
        print("intek-sh:",filepath+':','command not found')
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
    args = string

    for arg in args:
        pair = arg.split('=')
        try:
            os.environ[pair[0]] = pair[1]
        except (IndexError):
            os.environ[pair[0]] = ''

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
                break
            else:
                execute(args)
        except (IndexError):
            pass


if __name__ == '__main__':
    main()