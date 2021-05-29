"""Checks to see if the folder is a valid input/output"""
import os

def check_folder_exists(folder: str) -> bool:
    """Check to see if the folder exists"""

    if not os.path.isdir(folder):
        print('The specified folder does not exist. Please create it')
        return False
    return True

def check_folder_writable (folder: str) -> bool:
    if not os.access(folder, os.W_OK):
        print('The specified folder cannot be written')
        return False
    return True

def check_input_dir(folder: str) -> bool:
    """Check that it has a maps subfolder and a .bsp file."""

    if not (check_folder_exists(folder)):
        return False
    
    has_maps_subfolder = False
    
    has_map_files = False
    for dir, subdirs, fs in os.walk(folder):

        for file_ in fs:
            if file_.lower().endswith('.bsp') and not(has_map_files):
                has_map_files = True
        
        for subdir in subdirs:
            full_folder = os.path.join(folder, subdir)
            if os.path.isdir(full_folder) and (subdir.lower() == 'maps') and not(has_maps_subfolder):
                has_maps_subfolder = True
        
        if has_map_files and has_maps_subfolder:
            break

    if not has_map_files:
        print('Make sure there are .bsp files')
        return False
    if not has_maps_subfolder:
        print('Make sure there is a /maps subfolder')
        return False
    
    return True

def check_output_dir(folder: str) -> bool:
    """Checks the folder exists and is writable"""
    
    if not (check_folder_exists(folder)):
        return False
    if not (check_folder_writable(folder)):
        return False
    return True
