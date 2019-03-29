import cv2
import os
import tkinter
import math
import numpy as np
import sys
import time
import threading
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkfont
from PIL import Image
from shutil import *
# import xlwt
import csv
from numpy import array
# from  skimage import transform
from tkinter import filedialog

#pyinstaller 打包
#pyinstaller -F -w main_run.py -p colordistance.py -p getname.py -p getpicfile.py -p lookdata.py -p outputresult.py --hidden-import colordistance --hidden-import getname --hidden-import getpicfile --hidden-import lookdata --hidden-import outputresult
#pyinstaller main_run.py -p colordistance.py -p getname.py -p getpicfile.py -p lookdata.py -p outputresult.py --hidden-import colordistance --hidden-import getname --hidden-import getpicfile --hidden-import lookdata --hidden-import outputresult


import getname
import getpicfile
import outputresult
import colordistance
import lookdata


class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.window_init()
        self.pack()
        self.createwidgets()
    def window_init(self):
        self.master.title('色差检测系统')
        self.master.geometry("740x490")
        self.master.resizable(False, False)  ## 规定窗口不可缩放
        #界面最大化，此处锁定界面
        # width,height=self.master.maxsize
        # self.master.geometry("{}x{}".format(width,height))

    def createwidgets(self):
        # #fm1
        # self.fm1=Frame(self,bg="black").grid(row=0,column=0)
        # self.lab1=Label(self.fm1,bg='black',text='拍摄系统',width=10,height=240,anchor='w').grid()
        # #self.fm1.grid(column=1)
        #
        #
        # #fm2
        # self.fm2=Frame(self,bg='black').grid(row=1,column=1)
        # change to use grid rather than pack
        self.lab_catalog1=Label(self,text="拍\n摄\n系\n统",justify=LEFT,background="lightblue",width=5,height=10).grid(row=0,column=0,rowspan=6,pady=25,padx=0)
        self.lab_catalog2=Label(self,text="色\n差\n计\n算\n系\n统",justify=LEFT,background='lightblue',width=5,height=12).grid(row=7,column=0,rowspan=5,pady=0)

        # def opencarema():
        #     t_son=son_thread()
        #     t_son.run()

        self.button_open_camera=ttk.Button(self,text="启动",command=self.getpic).grid(row=2,column=1,columnspan=3,padx=40,ipadx=5)

        self.button_close_camera=ttk.Button(self,text="按’q‘退出拍照").grid(row=3,column=1,columnspan=3,padx=40,ipadx=5)
        self.lab3=Label(self,text="----------------------------------------").grid(row=6,column=0,columnspan=5)
        self.lab_intro1=Label(self,text="请启动相机后键盘\n长按功能键拍摄，在弹窗中输入\n图片名字,图像默认保存到\n程序根目录下,",width=20).grid(row=4,column=1,rowspan=2,columnspan=2,padx=10)
        self.lab_image_name =PhotoImage(file='cant_be_deleted.gif')
        self.lab_pic1=Label(self,image=self.lab_image_name,background="lightgray",width=210,height=160)#210*160的图片
        self.lab_pic1.grid(row=1,column=5,rowspan=4,columnspan=5,pady=10,padx=20)
        self.lab_pic2=Label(self,image=self.lab_image_name,background="lightgray",width=210,height=160)
        self.lab_pic2.grid(row=1,column=11,rowspan=4,columnspan=5,pady=10,padx=10)
        self.button_capture1=ttk.Button(self,text="按‘p’获取参照图").grid(row=5,column=5,columnspan=5)
        self.button_capture2=ttk.Button(self,text="按‘k’获取处理图").grid(row=5,column=11,columnspan=5)
        self.button_input_pic1=ttk.Button(self,text="input1",command=self.input1).grid(row=8,column=1,columnspan=3,padx=10,ipadx=20)
        self.button_input_pic2 = ttk.Button(self, text="input2",command=self.input2).grid(row=10, column=1, columnspan=3,padx=10,ipadx=20)
        self.button6=ttk.Button(self,text="颜色修复",command=self.color_repair).grid(row=9,column=7,pady=10)
        self.button7=ttk.Button(self,text="图像对齐",command=self.align).grid(row=9,column=9)
        self.button8=ttk.Button(self,text="色差计算",command=self.color_distance).grid(row=9,column=14,columnspan=2,ipadx=15,padx=20)
        self.button9=ttk.Button(self,text="结果导出",command=self.output).grid(row=10,column=14,columnspan=2,ipadx=15)
        self.button9 = ttk.Button(self, text="色差检视", command=lookdata.lookwindows).grid(row=11, column=14, columnspan=2,
                                                                               ipadx=15)
        # self.lab_input_pic1 = Label(self,image=self.pic1, background="lightgreen", width=110,height=70)
        # self.lab_input_pic1.grid(row=7, rowspan=2,column=4,columnspan=3)
        # self.lab_input_pic2 = Label(self, image=self.pic1, background="lightgreen", width=110,height=70)
        # self.lab_input_pic2.grid(row=9, column=4, rowspan=2,columnspan=3)
        # self.lab_pic_color_1 = Label(self,image=self.pic1,background="lightgreen", width=110,height=70)
        # self.lab_pic_color_1.grid(row=7, column=7, rowspan=2, columnspan=3,pady=10)
        # self.lab_pic_color_2 = Label(self,image=self.pic1,background="lightgreen", width=110,height=70)
        # self.lab_pic_color_2.grid(row=9, column=7, rowspan=2, columnspan=3)
        # self.lab_pic_situation1 = Label(self,image=self.pic1,background="lightgreen", width=110,height=70)
        # self.lab_pic_situation1.grid(row=7, column=11, rowspan=2, columnspan=3)
        # self.lab_pic_situation2= Label(self,image=self.pic1,background="lightgreen", width=110,height=70)
        # self.lab_pic_situation2.grid(row=9, column=11, rowspan=2, columnspan=3)
        self.stage_massage= StringVar()
        self.lab_showstage=Label(self,text="运行状态",anchor="w").grid(row=7,column=14,columnspan=2)
        self.lab_showstage = Label(self, textvariable=self.stage_massage, anchor="w").grid(row=8, column=14,
                                                                                           columnspan=2)
        outro=tkfont.Font(family='Fixdsys', size=5)
        self.lab_outro=Label(self,text="Powered by python tkinter & seclee",justify=LEFT).grid(row=13,column=0,columnspan=5)


    # def pic_valid(self,pic):
    #     valid=True
    #     try:
    #         Image.open(pic).verity()
    #     except:
    #         valid=False
    #     return valid
    #
    # def convert_pic_to_show(self,pic):
    #     if self.pic_valid(pic):
    #         try:
    #

    def getpic(self):

    ###主函数切勿调用
        cap=cv2.VideoCapture(0)
        while(True):
            global seclee
            global aimg1
            global aimg2
            ret,img=cap.read()
            cv2.imshow('cam',img)
            if cv2.waitKey(1) == ord('p'):
                getpicname=getname.getname()
                getpicname.wait_window() #弹窗传输数据 核心语句
                filename = str(getpicname.userinfo).split("'")[1]
                if filename=='':
                    continue
                path=os.path.abspath('main_run.py')
                outFilename = filename+".jpg"
                print("Saving  image : ", outFilename)
                self.stage_massage.set('运行状态\n' + filename + '.gif' + '\n已保存')
                cv2.imwrite(outFilename, img)
                # 生成缩略图
                a_open = Image.open(filename + '.jpg')
                gifpreview = a_open.resize((210, 160), Image.ANTIALIAS)
                gifpreview.save(filename + '_preview.jpg')
                a_open.close()

                #yuantu转化成gif
                im = Image.open(filename + '.jpg')
                im.save(filename+'.gif')
                # os.remove(filename+'.jpg')
                im.close()

                a = filename + '.gif'
                    #缩略图sheng cheng gif
                im_prew = Image.open(filename + '_preview.jpg')
                im_prew.save(filename + '_preview.gif')
                os.remove(filename+'_preview.jpg')
                os.remove(filename + '.gif')
                    #im_prew.close()

                a_prew=filename+'_preview.gif'
                aimg1=PhotoImage(file=a_prew)
                self.lab_pic1.configure(image=aimg1)

                ##此处涉及到一个问题 ，创建控件的时候直接 在后面.grid(),会使得此处传值出现问题
                continue

            if cv2.waitKey(1)==ord('k'):
                getpicname = getname.getname()
                getpicname.wait_window()  # 弹窗传输数据 核心语句
                filename = str(getpicname.userinfo).split("'")[1]
                if filename=='':
                    continue
                path = os.path.abspath('main_run.py')
                outFilename = filename + ".jpg"
                print("Saving  image : ", outFilename)
                self.stage_massage.set('运行状态\n' + filename + '.gif' + '\n已保存')
                cv2.imwrite(outFilename, img)
                # 生成缩略图
                a_open = Image.open(filename + '.jpg')
                gifpreview = a_open.resize((210, 160), Image.ANTIALIAS)
                gifpreview.save(filename + '_preview.jpg')
                a_open.close()

                # yuantu转化成gif
                im = Image.open(filename + '.jpg')
                im.save(filename + '.gif')
                im.close()

                a = filename + '.gif'
                # 缩略图sheng cheng gif
                im_prew = Image.open(filename + '_preview.jpg')
                im_prew.save(filename + '_preview.gif')
                os.remove(filename + '_preview.jpg')
                os.remove(filename + '.gif')
                #im_prew.close()

                a_prew = filename + '_preview.gif'
                aimg2 = PhotoImage(file=a_prew)
                self.lab_pic2.configure(image=aimg2)

                ##此处涉及到一个问题 ，创建控件的时候直接 在后面.grid(),会使得此处传值出现问题
                continue

            if cv2.waitKey(1)==ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

        n = 0
        for root, dirs, files in os.walk('.'):
            for name in files:
                if ("_preview" in name):
                    n += 1
                    print(n)
                    print(name)
                    os.remove(os.path.join(root, name))




##多线程方案pass
#opencv子线程无法使用imshow等函数

    #各个控件的逻辑实现
    #使用多线程，本工程线程统一命名t+num
    #定义一个类内局域量seclee，作为控制相机的参数 默认值seclee==0,seclee=-1 shutdown,seclee==1 capture1，seclee==2 capture2
#     def capture_pic_1(self):
#         seclee=1
#         print(seclee)
#     def capture_pic_2(self):
#         seclee=2
#         print(seclee)
#     def cam_shundown(self):
#         seclee=-1
#     # def father_thread(self):
#     #     while(True):
#     #         if seclee=0
#     #
#     #获取名字的过程放到子线程里面
#     def showcam(self):
#         global img
#         son_thread.run(self)
#
#         cv2.imshow('cam', img)
# class son_thread(threading.Thread):
#     def __init__(self):  #
#         threading.Thread.__init__(self)
#         self.thread_stop=FALSE
#         print('start')
#     def run(self):
#         global seclee
#         global img
#         cap = cv2.VideoCapture()

#         while (True):
#             ret,self.img=cap.read()
#             #cv2.imshow('cam',img)
#             if seclee==1:
#                 filename=getname.dropwindows.userinfo
#                 ##get char name
#                 outFilename = filename+".jpg"
#                 print("Saving  image : ", outFilename)
#                 cv2.imwrite(outFilename, img)
#                 #图像显示在lab_pic_1
#                 #self.
#                 ######
#                 seclee=0
#                 continue
#             if seclee==2:
#                 filename=getname.dropwindows.userinfo
#                 ##get char name
#                 outFilename = filename+".jpg"
#                 print("Saving  image : ", outFilename)
#                 cv2.imwrite(outFilename, img)
#                 #图像显示在lab_pic_2
#                 #self.
#                 ######
#                 seclee=0
#                 continue
#             if seclee==-1:
#                 seclee=0
#                 break
#         cap.release()
#         cv2.destroyAllWindows()
#     def stop(self):
#         self.thread_stop=True

        #father thread ：启动相机，关闭相机，拍照
        #son thread ：接受参数变化，执行行为
        #启动摄像机，即创建son线程
        #子线程关闭，则主线程无法执行
        #父线程关闭，则全关闭
        #相机开机=子线程开始，所以command-启动对应camera.t2.start
        #t1=threading.Thread(target=self.father_thread,args=("thread_father"))
        ####改写为上面的类实例化，重写run的方法

# def run():
#     global seclee
#     cap = cv2.VideoCapture()
#     while (True):
#         ret, img = cap.read()
#         cv2.imshow('cam', img)
#         if cv2.waitKey(1) == ord('q'):
#             break
#     while (True):
#         ret, img = cap.read()
#         # cv2.imshow('cam',img)
#         if seclee == 1:
#             filename = getname.dropwindows.userinfo
#             ##get char name
#             outFilename = filename + ".jpg"
#             print("Saving  image : ", outFilename)
#             cv2.imwrite(outFilename, img)
#             # 图像显示在lab_pic_1
#             # self.
#             ######
#             seclee = 0
#             continue
#         if seclee == 2:
#             filename = getname.dropwindows.userinfo
#             ##get char name
#             outFilename = filename + ".jpg"
#             print("Saving  image : ", outFilename)
#             cv2.imwrite(outFilename, img)
#             # 图像显示在lab_pic_2
#             # self.
#             ######
#             seclee = 0
#             continue
#         if seclee == -1:
#             seclee = 0
#             break
#     cap.release()
#     cv2.destroyAllWindows()
# t1=threading.Thread(target=run)


    def getfilepath(self):
        filepath=getpicfile.getpicfile().file_path
        return filepath
    def input1(self):
        global aimg_input_1
        filepath=self.getfilepath()
        self.colorfilepath1 = filepath
        self.stage_massage.set('图片1已导入')
        # 生成缩略图
        # print(filepath)
        # a_open = Image.open(filepath)
        # gifpreview = a_open.resize((110, 70), Image.ANTIALIAS)
        # name=filepath.split('/')[-1]
        # print(name)
        # gifpreview.save(name.split('.')[0]+'_preview.gif')
        # a_open.close()
        # picprename=name.split('.')[0]+'_preview.gif'
        # print(picprename)
        ####莫名官方 bug，同样的更新方式 此处报错
        ##TypeError: object of type 'PhotoImage' has no len()
        # aimg_input_1=PhotoImage(file=picprename)
        # self.lab_input_pic1.configure(aimg_input_1)

    def input2(self):
        global aimg_input_2
        filepath = self.getfilepath()
        self.stage_massage.set('图片2已导入')
        # 生成缩略图
        self.colorfilepath2=filepath
        print('图片2已经导入')
        # print(filepath)
        # a_open = Image.open(filepath)
        # gifpreview = a_open.resize((110, 70), Image.ANTIALIAS)
        # name = filepath.split('/')[-1]
        # print(name)
        # gifpreview.save(name.split('.')[0] + '_preview.gif')
        # a_open.close()
        # picprename = name.split('.')[0] + '_preview.gif'
        # print(picprename)
        # aimg_input_2=PhotoImage(file=picprename)
        # self.lab_input_pic2.configure(a_input_2)

    def color_repair1(self):
        global aimg_color_1
        self.stage_massage.set('图片1修复中')
        filepath=self.colorfilepath1
        ##颜色修复
        #输入图片路径 输出修复后的图片
        file = Image.open(filepath)
        pic_array = file.load()
        repaired_pic=colordistance.repair(filepath,pic_array)
        self.pic1_after_repair_name=(filepath.split('/')[-1]).split('.')[0]+'_repaired.jpg'
        # repaired_pic.save(self.pic1_after_repair_name)  bug无法直接处理jpg，先转化成RGB图
        print(repaired_pic)
        # new_im = Image.fromarray(repaired_pic)
        # new_im.save(self.pic1_after_repair_name)
        cv2.imwrite(self.pic1_after_repair_name, repaired_pic)
        self.stage_massage.set('图片1已经修复')

        # repaired_pic.convert('RGB').save(self.pic1_after_repair_name)
        ##另存为新图片
        #解决显示问题之后 此处需要补全 转化缩略图的过程,jpg2gif & show
        # aimg_color_1=PhotoImage(file=self.pic1_after_repair_name_preview)
        # self.lab_pic_color_1.configure(aimg_color_1)

    def color_repair2(self):
        global aimg_color_2
        filepath=self.colorfilepath2

        self.stage_massage.set('图片1已经修复\n图片2修复中')
        ##颜色修复
        #输入图片路径 输出修复后的图片
        file=Image.open(filepath)
        pic_array=file.load()
        repaired_pic=colordistance.repair(filepath,pic_array)
        self.pic2_after_repair_name=(filepath.split('/')[-1]).split('.')[0]+'_repaired.jpg'
        cv2.imwrite(self.pic2_after_repair_name, repaired_pic)

        self.stage_massage.set('图片已经修复')
        ##另存为新图片
        # 解决显示问题之后 此处需要补全 转化缩略图的过程
        # aimg_color_2=PhotoImage(file=self.pic2_after_repair_name_preview)
        # self.lab_pic_color_2.configure(aimg_color_2)
    def color_repair(self):
        print('图片1修复中')
        self.stage_massage.set('图片1修复中')
        self.color_repair1()
        print('图片1已经修复')
        self.stage_massage.set('图片1已经修复\n图片2修复中')
        print('图片1已经修复\n图片2修复中')
        self.color_repair2()
        print('图片2已经修复')

    def align(self):
        global aimg_align_1
        global aimg_align_2
        #
        # filepath1=self.pic1_after_repair_name #jpg
        # filepath2=self.pic2_after_repair_name
        #色差修复功能删去后的调用
        filepath1=self.colorfilepath1
        filepath2 =self.colorfilepath2
        # pic1=Image.open(filepath1)
        # pic2=Image.open(filepath2)
        colordistance.alignimages(filepath1,filepath2)
        copyfile(filepath1,'refpic.jpg')
        self.stage_massage.set('图像对齐完成，分别保存为refpic和aligned')
        print('图像对齐完成，分别保存为refpic和aligned')
        ###缩略图显示
        # aimg_align_1=filepath1.split('_')[0]+filepath1.split('.')[1]
        # print(aimg_align_1)
        # aimg_align_2

    def color_distance(self):
        print('色差计算中')
        self.stage_massage.set('色差计算中')
        global outresult
        filepath1='refpic.jpg'
        filealigned='aligned.jpg'
        pic1=Image.open(filepath1)
        pic2=Image.open(filealigned)
        pic1_array=pic1.load()
        pic2_array=pic2.load()
        outresult = [[0 for col in range(pic1.size[0])] for row in range(pic1.size[1])]
        outresult=np.array(outresult)
        for i in range(pic1.size[1]):
            for j in range(pic1.size[0]):
                # print(i,j)
                a=round(colordistance.colourdistance(pic1_array[j,i],pic2_array[j,i]),6)
                # print(a)
                outresult[i,j]=a

        pic1.close()
        pic2.close()
        print('色差计算完成！')
        self.stage_massage.set('色差计算完成！')
        print(outresult)
        return outresult
        #这个return用来传给lookdata

    def output(self):
        print('结果导出中')
        self.stage_massage.set('结果导出中')
        global outresult
        print('output:',outresult)
        #保存txt，文件太大 打开太慢
        # fname=outputresult.creat_result_file().file_path
        # np.savetxt(fname,outresult,fmt='%s',newline='\n')
        #保存为excel(xlwt缺陷不能大于256行)
        # fname='result.xls'
        # f=xlwt.Workbook()
        # sheet1=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
        # filepath1 = 'refpic.jpg'
        # pic1 = Image.open(filepath1)
        # for i in range(pic1.size[0]):
        #     for j in range(pic1.size[1]):
        #         sheet1.write(i,j,float(outresult[i,j]))
        # f.save(fname)
        csvfile=open('result.csv','w')
        file=csv.writer(csvfile)
        filepath1 = 'refpic.jpg'
        pic1 = Image.open(filepath1)
        #print(pic1.size[0],pic1.size[1]) 列 行 640 480
        for line in outresult[0:pic1.size[1]-1]:
            file.writerow(line)
        print('结果已导出至result.csv')
        self.stage_massage.set('结果已导出至result.csv')
        csvfile.close()


if __name__=="__main__":
    aimg1=None
    aimg2=None
    aimg_input_1=None
    aimg_input_2=None
    aimg_color_1=None
    aimg_color_2=None
    aimg_align_1=None
    aimg_align_2=None
    test=None
    outresult=[]
    app=Application()
    app.mainloop()

