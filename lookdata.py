from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from sys import exit
import os
# import pygame
import numpy
import colordistance

class lookwindows(Toplevel):
    def __init__(self):
        Toplevel.__init__(self,master=None)
        self.withdraw
        self.getpic()
        picsize=Image.open(self.picpath)
        self.framesize_x=picsize.size[0]
        self.framesize_y=picsize.size[1]+50
        self.getresult_array()
        self.geometry(str(self.framesize_x)+"x"+str(self.framesize_y))
        self.resizable(False, False)
        # pygame.init()
        self.UI()

#获取色差值
#事件绑定
        filename = (self.picpath.split('/')[-1]).split('.')[0]
        im = Image.open(self.picpath)
        pic_array = im.load()
        def callback(event):
            print('当前位置为：', event.x, event.y)
            if event.y <= self.framesize_y-50:
                if event.x <= self.framesize_x:
                    self.cecha.set(self.result_array[event.y,event.x])
                    print(pic_array[event.x,event.y])
                    R,G,B=colordistance.repair_pix(pic_array[event.x,event.y])
                    self.cecha1.set(str(R)+','+str(G)+','+str(B))
                else:
                    pass
            else:
                pass

        self.picshow.bind('<Button-1>', callback)
        # if x <= self.framesize_y & y <= self.framesize_x:
        #     self.cecha.set(self.result_array[x, y])
        # else:
        #     pass

        # self.getcechadata()
        os.remove((self.picpath.split('/')[-1]).split('.')[0] + '.gif')



#tkinter缺陷，得先转化为gif图片
    def UI(self):
        #
        filename=(self.picpath.split('/')[-1]).split('.')[0]
        im = Image.open(self.picpath)
        im.save(filename + '.gif')
        # os.remove(filename+'.jpg')
        im.close()
        #
        picpath=filename + '.gif'
        self.frame=Frame(self,background='lightgreen',width=self.framesize_x,height=self.framesize_y-50)

        self.frame.grid(row=0,column=0)
        self.pic=PhotoImage(file=picpath)
        self.picshow=Label(self,image=self.pic,background='lightgray',width=self.framesize_x,height=self.framesize_y-50)
        self.picshow.grid(row=0,column=0)
        self.cecha=StringVar()
        self.cechadata=Label(self,textvariable=self.cecha)
        self.cechadata.grid(row=1,column=0)
        self.cecha1 = StringVar()
        self.cechadata1 = Label(self, textvariable=self.cecha1)
        self.cechadata1.grid(row=2, column=0)


    #选择基准图片
    def getpic(self):
        self.picpath=filedialog.askopenfilename()

    # def getcechadata(self):
    #      x, y = self.picshow.bind('<Button-1>',callback)
    #      if x<=self.framesize_y & y<=self.framesize_x:
    #             self.cecha.set(self.result_array[x,y])
    #      else:
    #         pass
    #
    # def callback(event):
    #     print('当前位置为：', event.x, event.y)
    #     return event.x, event.y

    def getresult_array(self):
        try:
            self.result_array = numpy.loadtxt(open("result.csv","rb"),delimiter=",",skiprows=0)
            self.result_array=numpy.array(self.result_array)
            print(self.result_array)
        except:
            messagebox.showwarning('警告', '没有发现result.csv')
