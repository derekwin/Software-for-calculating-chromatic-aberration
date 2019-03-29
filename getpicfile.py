from tkinter import *
from tkinter import filedialog

#获取并返回文件目录

class getpicfile(Toplevel):
    def __init__(self,master=None):
        Toplevel.__init__(self,master)
        self.withdraw()
        self.file_path = filedialog.askopenfilename()#返回文件的绝对路径