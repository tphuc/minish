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
    os.environ.pop(var) 
def printenv(var):
    if var in os.environ.keys():
        print(os.environ[var])
while True:
    raw_input = input(PROMPT)
    if raw_input == 'exit':
        break

    args = raw_input.split()
    command = args[0]

    if command == 'cd':
        if len(args) > 1:
            cd(args[1])
        else:
            CURRENT_DIR = os.environ['HOME']
    elif command == 'pwd':
        print(CURRENT_DIR)
    elif command == 'export':
        export(args[1])
    elif command == 'unset':
        unset(args[1])
    elif command == 'printenv':
        printenv(args[1])
    elif command == 'exit':
        print("exit")
        break
    

    


