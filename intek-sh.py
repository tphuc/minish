#!/usr/bin/env python3

import os.path
from os import environ
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PROMPT = "intek-sh$ "

def cd(directory):
    global CURRENT_DIR
    if directory == '.':
        pass
    elif directory == '..':
        CURRENT_DIR = CURRENT_DIR[:CURRENT_DIR.rfind('/')]
    elif os.path.isdir(CURRENT_DIR + '/' + directory):
        CURRENT_DIR += '/' + directory

def export(string):
    args = string.split('=')
    os.environ[args[0]] = args[1]

def unset(var):
    try:
        os.environ.pop(var)
    except (KeyError):
        return

def printenv(var='all'):
    if var == 'all':
        dict_ = dict(os.environ)
        for k,v in dict_.items():
            print(k+'='+v)
        return
    if var in os.environ.keys():
        print(os.environ[var])
    


def prompt_input():
    try:
        raw_input = input(PROMPT)
    except (EOFError):
        return None
    return raw_input

def main():
    while True:
        raw_input = prompt_input()

        if raw_input == None:
            break

        if raw_input == 'exit':
            print('exit')
            break


        args = raw_input.split()
        command = args[0]

        if command == 'cd':
            if len(args) > 1:
                cd(args[1])
            else:
                try:
                    CURRENT_DIR = os.environ['HOME']
                except (KeyError):
                    print("intek-sh: cd: HOME not set")
        elif command == 'pwd':
            print(CURRENT_DIR)
        elif command == 'export':
            export(args[1])
        elif command == 'unset':
            unset(args[1])
        elif command == 'printenv':
            try:
                printenv(args[1])
            except (IndexError):
                printenv()
        elif command == 'exit':
            print("exit")
            break
    


if __name__ == '__main__':
    main()