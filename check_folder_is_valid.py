import os
import sys

#Check to see if the folder exists and is writable
def check_folder_is_valid(folder):
    if not os.path.isdir(folder):
        print('The specified folder does not exist. Please create it')
        sys.exit(1)
    if not os.access(folder, os.W_OK):
        print('The specified folder cannot be written')
        sys.exit(2)

#Check that it has a maps subfolder and a .bsp file.
def check_input_dir(folder):
    check_folder_is_valid(folder)
    folder_files = os.listdir(folder)
    has_maps_subfolder = False
    for file in folder_files:
        full_file = os.path.join(folder, file)
        if os.path.isdir(full_file) and file.lower() == 'maps':
            has_maps_subfolder = True
            #No need to keep searching
            break
    if not has_maps_subfolder:
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
        