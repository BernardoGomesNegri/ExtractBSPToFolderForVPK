from os import error
import tkinter
import tkinter.constants
import tkinter.messagebox
from tkinter import filedialog
from typing import Callable, Optional
from core.check_folder_is_valid import *
from core.core import main
from core.print_ex import print_ex
import threading

def askdirwrapper() -> Optional[str]:
    return filedialog.askdirectory(mustexist=True)

class GuiHandler:
    """Creates the GUI. Also contains all the methods for said GUI"""

    def __init__(self):
        """Starts everything. Also starts mainloop."""

        self.top = tkinter.Tk()
        self.top.title('Extract BSP to folder for VPK')

        # Setup icons
        icon = tkinter.PhotoImage(file='./images/logo.ico')
        self.top.iconphoto(True, icon)

        # Setup variables
        self.input: Optional[str] = ''
        self.output: Optional[str] = ''
        self.running = False

        # Add elements
        self.choose_input_btn = tkinter.Button(self.top, command=self.input_click, text='Choose input folder')
        self.text_input = tkinter.Label(self.top, height=1, text='Input folder is: ')
        self.choose_output_btn = tkinter.Button(self.top, command=self.output_click, text='Choose output folder')
        self.text_output = tkinter.Label(self.top, height=1, text='Output folder is: ')
        self.start_btn = tkinter.Button(self.top, command=self.start_click, text='Start process')
        self.status_indicator = tkinter.Label(self.top, height=1, text='Select input and output folders')

        # Pack everything
        self.choose_input_btn.pack(side=tkinter.constants.TOP, anchor=tkinter.constants.NW)
        self.text_input.pack(side=tkinter.constants.TOP, anchor=tkinter.constants.NW)
        self.choose_output_btn.pack(side=tkinter.constants.TOP, anchor=tkinter.constants.NW)
        self.text_output.pack(side=tkinter.constants.TOP, anchor=tkinter.constants.NW)
        self.start_btn.pack(side=tkinter.constants.TOP, anchor=tkinter.constants.NW)
        self.status_indicator.pack(side=tkinter.constants.TOP, anchor=tkinter.constants.NW)

        self.top.mainloop()

    def input_click(self) -> None:
        self.input = askdirwrapper()
        print(f'The input directory is: {self.input}')
        self.__path_check__(path=self.input,
            error_status_text="Select a valid input folder",
            text_element=self.text_input,
            text_prefix="The input directory is: ",
            error_text="Select a folder which has a maps/ subfolder and bsp files",
            checkfn=check_input_dir)

    def output_click(self):
        self.output = askdirwrapper()
        print(f'The output directory is: {self.output}')
        self.__path_check__(path=self.output,
            error_status_text="Select a valid output folder",
            text_element=self.text_output,
            text_prefix="Output folder is: ",
            error_text="Select a writable folder that exists",
            checkfn=check_output_dir)    

    def main_error_callback(self, err: Exception):
        self.status_indicator.configure(text='There was an error')
        tkinter.messagebox.showerror(title='There was an error', message='The error was: ' + str(err))
        print(f'There was an error. The error was: {err}')
        print_ex(err)
        self.running = False

    def main_callback(self):
        self.running = False
        self.status_indicator.configure(text='Files ready to be packaged using VPK. You can close the program now.')
        
    def start_click(self):
        if (self.input != '') and (self.output != '') and (self.running == False):
            # Start main on a separate process
            self.core_thread = threading.Thread(target=self.start, name='corethread')
            self.core_thread.start()
            self.status_indicator.configure(text='Running. No error yet, this may take a while')
            self.running = True
        else:
            self.status_indicator.configure(text='Either the program is already running or the input or output are not valid')

    def __path_check__(self, path: Optional[str], error_status_text: str, text_element: tkinter.Label, text_prefix: str, error_text: str, checkfn: Callable[[Optional[str]], bool]) -> None:
        """Warning: mutates path and text_element!"""
        if checkfn(path) and path is not None:
            text_element.configure(text=text_prefix + path)
        else:
            text_element.configure(text=error_text)
            self.status_indicator.configure(text=error_status_text)
            path = ''

    """Wrapper for main method"""
    def start(self):
        if self.input is not None and self.output is not None:
            main(self.input, self.output, self.main_callback, self.main_error_callback)

if __name__ == '__main__':
    gui_main = GuiHandler()
