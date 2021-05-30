import argparse
import sys
from typing import List
from core.check_folder_is_valid import check_input_dir, check_output_dir
from core.args import Args

def interpret_arg(args: List[str], question: str) -> str:
    for a in args:
        if (a is not None) and (a != ''):
            return a
    return input(question + '\n')

def parse_args(inputarg: str, outputarg: str) -> Args:
    #Prepares arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-i', '--input', type=str)
    arg_parser.add_argument('-o', '--output', type=str)
    arg_parser.add_argument('-s', '--singlethread', action="store_true", default=False)
    cmd_args = arg_parser.parse_args()

    input_dir_str = interpret_arg([inputarg, cmd_args.input], 'Where is your input folder, with the subfolder /maps?')
    output_dir_str = interpret_arg([outputarg, cmd_args.output], 'Where is your output folder, preferably empty?')

    print('Input folder: ', input_dir_str)
    print('Output folder: ', output_dir_str)
    
    # Checks
    if not check_output_dir(output_dir_str):
        print('Make sure the output exists and is writable')
        sys.exit(2)
    if not check_input_dir(input_dir_str):
        print('Make sure the input exists and has a maps/ subfolder and .bsp files')
        sys.exit(1)
    
    is_parallel = not cmd_args.singlethread
    
    return Args(input_dir_str, output_dir_str, is_parallel)
