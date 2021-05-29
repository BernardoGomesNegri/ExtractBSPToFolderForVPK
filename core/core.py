import os
from pathlib import Path
from typing import Callable, List, Optional, Tuple
import time
import multiprocessing
from core.copy_map_contents import copy_map_contents
from core.copy_file import copy_file
from core.print_ex import print_ex
import core.handle_args

def main(
        inputarg: str='',
        outputarg: str='',
        callback: Optional[Callable[[], None]]=None,
        error_callback: Optional[Callable[[Exception], None]]=None) -> None:
    try:
        args = core.handle_args.parse_args(inputarg, outputarg)
        input_dir_str = args.input
        output_dir_str = args.output
        is_parallel = args.parallel

        # Start timer
        t0 = time.time()

        input_folder = Path(input_dir_str)

        #Start by searching all .bsp files in the maps subfolder
        maps_folder_str = os.path.join(input_dir_str, 'maps')
        maps = Path(maps_folder_str).rglob('*.bsp')
        maps_list = [x for x in maps]

        #Copy those map contents.
        arguments: List[Tuple[str, str]] = []
        for m in maps_list:
            if is_parallel:
                arguments.append((str(m), output_dir_str))
            else:
                copy_map_contents(str(m), output_dir_str)

        #If parallel, use Pool.starmap to run the copy files function
        if is_parallel:
            pool = multiprocessing.Pool()
            pool.starmap(copy_map_contents, arguments)
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
