import os
# We import sys for the function sys.exit to exit the program at any given point
import sys


def getFileSafely(path):
    '''
    Function to safely return a file object. If `path` does not exist, the program exits by calling `sys.exit(1)` after warning the user
    '''
    if os.access(path, os.F_OK):
        goodFile = open(path)
        return goodFile
    else:
        print("The file you have specified does not exist.")
        return exit(0)

if __name__ == '__main__':
    cwd = os.getcwd()
    print(f"Please enter a file path relative to {cwd}")
    filename = input("File Path: ")
    file = getFileSafely(filename)
    # The following line should *NEVER* get executed if `filename` is invalid
    print("Congratulations! You've specified a file that exists!")
    file.close()