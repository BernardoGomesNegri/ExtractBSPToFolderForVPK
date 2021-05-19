import tkinter
import tkinter.constants

def button_click():
    pass

def start():
    pass

if __name__ == '__main__':
    top = tkinter.Tk()
    top.title('Extract BSP to folder for VPK')
    # Setup icons
    icon = tkinter.PhotoImage(file='./images/logo.ico')
    top.iconphoto(True, icon)

    # Add elements
    choose_input_btn = tkinter.Button(top, command=button_click, text='Choose input file')
    text_input = tkinter.Label(top, height=1, text='Input file is: ')
    choose_output_btn = tkinter.Button(top, command=button_click, text='Choose output file')
    text_output = tkinter.Label(top, height=1, text='Output file is: ')
    start_btn = tkinter.Button(top, command=start, text='Start process')

    # Pack everything
    choose_input_btn.pack(side=tkinter.constants.TOP, anchor=tkinter.constants.NW)
    text_input.pack(side=tkinter.constants.TOP, anchor=tkinter.constants.NW)
    choose_output_btn.pack(side=tkinter.constants.TOP, anchor=tkinter.constants.NW)
    text_output.pack(side=tkinter.constants.TOP, anchor=tkinter.constants.NW)
    start_btn.pack(side=tkinter.constants.TOP, anchor=tkinter.constants.NW)

    
    top.mainloop()