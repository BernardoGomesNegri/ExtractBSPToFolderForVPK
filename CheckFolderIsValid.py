import os
import sys

def CheckFolderIsValid(folder):
    if not os.path.isdir(folder):
        print('The specified folder does not exist. Please create it')
        sys.exit(1)
    if not os.access(folder, os.W_OK):
        print('The specified folder cannot be written')
        sys.exit(2)