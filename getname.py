from tkinter import *
#引入一个全局变量 辨识
#弹窗需要三个 1.获取pic的name 2.input的图片目录
class getname(Toplevel):
    def __init__(self,master=None):
        Toplevel.__init__(self,master)
        self.geometry("320x200")
        self.resizable(False, False)
        self.title('输入所要抓取参考图像的名字')
        # 弹窗界面
        #self.pack()  #目前不清楚为什么没这句，下面的不生效
        self.setup_UI()

    def setup_UI(self):
        # 第一行（两列）
        self.label_intro=Label(self,text="请输入图片名字").grid(row=1,column=2,columnspan=2,padx=105,pady=30)

        # 第二行
        self.name=StringVar()
        Entry(self,textvariable=self.name).grid(row=2,column=2,columnspan=2,pady=10)
        Button(self, text="提交并拍照", command=self.update).grid(row=3,column=2,columnspan=2)
        Button(self, text="取消", command=self.cancel).grid(row=4,column=2,columnspan=2)
    def update(self):
        self.userinfo = [self.name.get()]  # 设置数据
        self.destroy()  # 销毁窗口
        print(self.userinfo)

    def cancel(self):
        self.userinfo ="'"   # 空！
        self.destroy()
