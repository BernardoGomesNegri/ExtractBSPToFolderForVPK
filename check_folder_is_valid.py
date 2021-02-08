import os
import sys

def check_folder_is_valid(folder):
    if not os.path.isdir(folder):
        print('The specified folder does not exist. Please create it')
        sys.exit(1)
    if not os.access(folder, os.W_OK):
        print('The specified folder cannot be written')
        sys.exit(2)

def check_input_dir(folder):
    check_folder_is_valid(folder)
    files = os.listdir(folder)
    HasMapsSubfolder = False
    for file in files:
        f = os.path.join(folder, file)
        if os.path.isdir(f) and file.lower() == 'maps':
            HasMapsSubfolder = True
    if not HasMapsSubfolder:
        print('Make sure there is a /maps subfolder')
        sys.exit(3)
    
    HasMapFiles = False
    for dir, subdirs, fs in os.walk(folder):
        for file_ in fs:
            if file_.lower().endswith('.bsp'):
                HasMapFiles = True
                break
        if HasMapFiles:
            break
    if not HasMapFiles:
        print('Make sure there are .bsp files')
        sys.exit(4)
        