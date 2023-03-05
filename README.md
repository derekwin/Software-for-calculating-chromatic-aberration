# -
基于python，tkinter，opencv，pillow，numpy实现的一个色差计算系统界面程序


- 利用opencv实现图像采集，pillow进行图像处理，tkinter实现软件界面，numpy进行数据处理，实现进行色差计算样本的采集，色差矫正，图像对齐（基于LAB特征点检测对齐），色差计算，结果可视化。

- 最后利用pyinstaller打包生成exe执行文件，命令在main_run.py文件里面。

- 打包时，python环境推荐使用 3.5，更高的版本打包过程会出现意料之外的报错。

- 软件操作说明见word文档

###打包时候的一个问题以及解决方法
直接打包 -F 为桌面应用程序时候，会出现一系列api调用错误

- 解决方法 先不加-F生成终端程序编译文件，然后再-F

第一步pyinstaller main_run.py -p colordistance.py -p getname.py -p getpicfile.py -p lookdata.py -p outputresult.py --hidden-import colordistance --hidden-import getname --hidden-import getpicfile --hidden-import lookdata --hidden-import outputresult

第二步pyinstaller -F -w main_run.py -p colordistance.py -p getname.py -p getpicfile.py -p lookdata.py -p outputresult.py --hidden-import colordistance --hidden-import getname --hidden-import getpicfile --hidden-import lookdata --hidden-import outputresult


##### 2019.3.30更新
- 修复色差恢复一元四次方程求解错误，另解决了复数根的筛选
在结果预览界面增加了修复后的rgb的显示

- 问题,色差恢复计算量巨大，故采用点哪点，计算哪点的方式（相当不严谨）

