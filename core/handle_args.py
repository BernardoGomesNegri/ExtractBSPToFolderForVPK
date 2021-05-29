import argparse
import sys
from core.check_folder_is_valid import check_input_dir, check_output_dir
from core.args import Args

def parse_args(inputarg: str, outputarg: str) -> Args:
    #Prepares arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-i', '--input', type=str)
    arg_parser.add_argument('-o', '--output', type=str)
    arg_parser.add_argument('-s', '--singlethread', action="store_true", default=False)
    cmd_args = arg_parser.parse_args()

    input_dir_str = ''
    output_dir_str = ''

    #If there is no input parameter, ask
    if inputarg != '':
        input_dir_str = inputarg
    elif not(cmd_args.input is None):
        input_dir_str: str = cmd_args.input
    else:
        input_dir_str = input('Where is your input folder, with the subfolder /maps? \n')
    
    print('Input folder: ', input_dir_str)

    #If there is no output parameter, ask
    if outputarg != '':
        output_dir_str = outputarg
    elif not(cmd_args.output is None):
        output_dir_str: str = cmd_args.output
    else:
        output_dir_str = input('Where is your output folder, preferably empty. \n')
    
    # Checks
    print('Output folder: ', output_dir_str)
    if(not(check_output_dir(output_dir_str))):
        sys.exit(2)
    if(not(check_input_dir(input_dir_str))):
        sys.exit(1)
    
    is_parallel = not cmd_args.singlethread
    
    return Args(input_dir_str, output_dir_str, is_parallel)
