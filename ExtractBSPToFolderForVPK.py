import os
from pathlib import Path
from check_folder_is_valid import check_folder_is_valid, check_input_dir
from copy_map_contents import copy_map_contents
from copy_file import copy_file
import multiprocessing
import time
import argparse

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-i', '--input', type=str)
    arg_parser.add_argument('-o', '--output', type=str)
    arg_parser.add_argument('-s', '--singlethread', action="store_true", default=False)
    args = arg_parser.parse_args()


    if args.input is None:
        input_dir_str = input('Where is your input folder, with the subfolder /maps? \n')
    else:
        input_dir_str = args.input
    
    print('Input folder: ', input_dir_str)
    check_input_dir(input_dir_str)
    
    if args.output is None:
        output_dir_str = input('Where should your output folder be? Preferrably empty \n')
    else:
        output_dir_str = args.output
    
    print('Output folder: ', output_dir_str)
    check_folder_is_valid(output_dir_str)

    is_parallel = not args.singlethread

    t0 = time.time() #Starts timer
    input_folder = Path(input_dir_str)
    temp_dir = Path(output_dir_str)

    #Start by extracting all the map files and putting them into our temporary directory
    maps_folder_str = os.path.join(input_dir_str, 'maps\\')
    maps = Path(maps_folder_str).rglob('*.bsp')
    maps_list = [x for x in maps]

    Arguments = []
    for m in maps_list:
        if is_parallel:
            Arguments.append((str(m), output_dir_str))
        else:
            copy_map_contents(str(m), output_dir_str)

    if is_parallel:
        pool = multiprocessing.Pool()
        pool.starmap(copy_map_contents, Arguments)
        pool.close()

    #Puts the original assets in our folder
    print('Copying original files')
    for src_dir, dirs, files in os.walk(input_folder):
            for file_ in files:
                copy_file(file_, src_dir, input_dir_str, output_dir_str)

    t1 = time.time()
    print('Operation complete in ', round(t1 - t0, 2), ' seconds')
    print('Files ready to be packaged in VPK')
