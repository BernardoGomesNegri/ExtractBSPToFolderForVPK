import os
import sys
from pathlib import Path
from typing import Callable
from core.check_folder_is_valid import check_folder_is_valid, check_input_dir
from core.copy_map_contents import copy_map_contents
from core.copy_file import copy_file
from core.print_ex import print_ex
import multiprocessing
import time
import argparse

def main(inputarg='', outputarg='', callback: Callable=None, error_callback: Callable=None) -> None :
    try:

        #Prepares arguments
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('-i', '--input', type=str)
        arg_parser.add_argument('-o', '--output', type=str)
        arg_parser.add_argument('-s', '--singlethread', action="store_true", default=False)
        cmd_args = arg_parser.parse_args()

        #If there is no input parameter, ask
        if inputarg != '':
            input_dir_str = inputarg
        elif not(cmd_args.input is None):
            input_dir_str = cmd_args.input
        else:
            input_dir_str = input('Where is your input folder, with the subfolder /maps? \n')
        
        print('Input folder: ', input_dir_str)
        check_input_dir(input_dir_str)
        
        #If there is no output parameter, ask
        if outputarg != '':
            output_dir_str = outputarg
        elif not(cmd_args.output is None):
            output_dir_str = cmd_args.output
        else:
            output_dir_str = input('Where is your output folder, preferably empty. \n')
        
        t0 = time.time() #Starts timer
        
        print('Output folder: ', output_dir_str)
        if(not(check_folder_is_valid(output_dir_str))):
            sys.exit(2)
        if(not(check_input_dir(input_dir_str))):
            sys.exit(1)

        is_parallel = not cmd_args.singlethread

        input_folder = Path(input_dir_str)
        temp_dir = Path(output_dir_str)

        #Start by searching all .bsp files in the maps subfolder
        maps_folder_str = os.path.join(input_dir_str, 'maps')
        maps = Path(maps_folder_str).rglob('*.bsp')
        maps_list = [x for x in maps]

        #Copy those map contents.
        Arguments = []
        for m in maps_list:
            if is_parallel:
                Arguments.append((str(m), output_dir_str))
            else:
                copy_map_contents(str(m), output_dir_str)

        #If parallel, use Pool.starmap to run the copy files function
        if is_parallel:
            pool = multiprocessing.Pool()
            pool.starmap(copy_map_contents, Arguments)
            pool.close()

        #Puts the original assets in our output folder folder
        print('Copying original files')
        for src_dir, dirs, files in os.walk(input_folder):
                for file_ in files:
                    copy_file(file_, src_dir, input_dir_str, output_dir_str)

        #Ends the timer.
        t1 = time.time()
        print('Operation complete in ', round(t1 - t0, 2), ' seconds')
        print('Files ready to be packaged in VPK')
        if(callback is not None):
            callback()
    except Exception as e:
        if(error_callback is not None):
            error_callback(e)
        else:
            print_ex(e)