import os

def check_git(path):

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


    
