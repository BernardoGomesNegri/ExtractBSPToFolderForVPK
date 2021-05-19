import tkinter

def button_click():
    print('asking for file input')

if __name__ == '__main__':
    print('Hello world')
    top = tkinter.Tk(screenName='Extract BSP To folder for VPK', baseName='Extract BSP To folder for VPK')
    icon = tkinter.PhotoImage(file='./images/logo.ico')
    top.iconphoto(True, icon)
    choose_file_btn = tkinter.Button(top, command=button_click, text='Choose file')
    choose_file_btn.pack()

    top.mainloop()