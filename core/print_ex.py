import sys
import logging
from pathlib import Path
import os

def print_ex(e: Exception):
    print(e)
    type, value, traceback = sys.exc_info()
    logging.error("There was an exception: information below")
    logging.error(str(type))
    logging.error(str(value))
    frame = traceback.tb_frame
    while frame.f_back is not None:
        logging.error("Error on line: " + str(frame.f_lineno))
        logging.error(f"On method {frame.f_code.co_name}")
        logging.error(f"On file {frame.f_code.co_filename}")
        this_path = Path(frame.f_code.co_filename)

        # Do not log things that are not our fault
        if not this_path.is_relative_to(Path(__file__).parent):
            break

        for local in frame.f_locals:
            logging.error(f"Variable: {str(local)} had value {frame.f_locals[local]}")

        frame = frame.f_back

    # We can try to do more advanced stuff later
