from tkinter import *
from tkinter import filedialog

#创建空白文件并返回文件目录

class outputresult(Toplevel):
    def __init__(self):
        Toplevel.__init__(self,master=None)
        self.withdraw()
        self.file_path_io =filedialog.asksaveasfile()
        # print(self.file_path_io)
        r=str(self.file_path_io)
        # print(r)
        self.file_path=r.split("'")[1]
    #   print(self.file_path)