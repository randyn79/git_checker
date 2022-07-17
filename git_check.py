#!/usr/bin/env python3

import os

def check_git(path):
    """Checks the sub-directories in the provided directory path to
determine if the sub-directory has a .git directory.  If it does, the
sub-directory name is added to the git_present list.  If it does NOT,
the sub-directory name is added to the git_not_present list."""

    git_present = []
    git_not_present = []


    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path,i)):
            if os.path.isdir(os.path.join(path,i,".git")):
                git_present.append(i)
            else:
                git_not_present.append(i)

    return git_present, git_not_present

def user_input():
    """Allows the user to input a path.  If no path is entered, the
current working directory will be used for the path."""

    print()
    print('=' * 11)
    print('git checker')
    print('=' * 11)
    print('Checks to see if the directories in the path contain a .git directory.')
    print()
    cwd = os.getcwd()
    print('Enter the path that you would like to check.')
    print('If no path is entered, the current working directory will be used.')
    print(f'Current Working Directory:  {cwd}')

    while True:
        print()
        path = input('Please enter the directory path:  ')

        if path == "":
            path = cwd

        if os.path.isdir(path):
            return path
        else:
            print()
            print('That is not a valid directory, please try again.')
            print()
            continue

def print_results(git_present, git_not_present):
    """Prints the contents of the git_present and git_not_present lists."""
    print()
    print('The following directories have a .git directory:  ')
    print(git_present)
    print()
    print('The following directories DO NOT have a .git directory:  ')
    print(git_not_present)
    print()

if __name__ == "__main__":

   
    path = user_input()
    
    
    git_present, git_not_present = check_git(path)

    print_results(git_present, git_not_present)


    
