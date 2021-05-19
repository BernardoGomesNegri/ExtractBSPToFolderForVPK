from os import error
import tkinter
import tkinter.constants
from tkinter import filedialog
from core.check_folder_is_valid import *
from core.core import main
import multiprocessing

class GuiHandler:
    def __init__(self):
        self.top = tkinter.Tk()
        self.top.title('Extract BSP to folder for VPK')

        # Setup icons
        icon = tkinter.PhotoImage(file='./images/logo.ico')
        self.top.iconphoto(True, icon)

        # Setup variables
        self.input = ''
        self.output = ''
        self.running = False

        # Add elements
        self.choose_input_btn = tkinter.Button(self.top, command=self.input_click, text='Choose input folder')
        self.text_input = tkinter.Label(self.top, height=1, text='Input folder is: ')
        self.choose_output_btn = tkinter.Button(self.top, command=self.output_click, text='Choose output folder')
        self.text_output = tkinter.Label(self.top, height=1, text='Output folder is: ')
        self.start_btn = tkinter.Button(self.top, command=self.start, text='Start process')
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
        self.input = filedialog.askdirectory()
        print(f'The input directory is: {self.input}')
        if((self.input != None) and (self.input != '')):
            # Make sure it is valid
            if(check_input_dir(self.input)):
                self.text_input.configure(text=f'The input directory is: {self.input}')
            else:
                self.text_input.configure(text='Select a folder which has a maps/ subfolder and bsp files')
                self.input = ''
                self.status_indicator.configure(text='Select a valid input folder')

    def output_click(self):
        self.output = filedialog.askdirectory()
        print(f'The output directory is: {self.output}')
        if((self.output != None) and (self.output != '')):
            # Make sure it is valid
            if(check_folder_is_valid(self.output)):
                self.text_output.configure(text=f'The input directory is: {self.output}')
            else:
                self.text_output.configure(text='Select a folder which has a maps/ subfolder')
                self.output = ''
                self.status_indicator.configure(text='Select a valid output folder')

    def main_error_callback(self, err):
        self.status_indicator.configure(text='There was an error')
        print(f'There was an error. The error was: {err}')
        self.running = False

    def main_callback(self, nonearg):
        self.running = False

    def start(self):
        if (self.input != '') and (self.output != '') and (self.running == False):
            # Start main on a separate process
            self.mainpool = multiprocessing.Pool(processes=1)
            self.mainpool.apply_async(func=main,
                args=(self.input, self.output),
                callback=self.main_callback,
                error_callback=self.main_error_callback)
            self.status_indicator.configure(text='Running. No error yet')
            self.running = True
        else:
            self.status_indicator.configure(text='Either the program is already running or the input or output are not valid')

if __name__ == '__main__':
    gui_main = GuiHandler()