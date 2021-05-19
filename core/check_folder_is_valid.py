import os
import sys

#Check to see if the folder exists and is writable
def check_folder_is_valid(folder: str) -> bool:
    if not os.path.isdir(folder):
        print('The specified folder does not exist. Please create it')
        return False
    if not os.access(folder, os.W_OK):
        print('The specified folder cannot be written')
        return False
    return True

#Check that it has a maps subfolder and a .bsp file.
def check_input_dir(folder: str) -> bool:
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
        return False
    
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
        return False
    return True
