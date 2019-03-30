import cv2
from tkinter import _flatten
import math
import numpy as np
from PIL import Image
from sympy import solve
from sympy.abc import x,y,z



# 算法区域
##frist 利用opencv拍照获取图像，补充查看界面实况
######函数bug main启动时 直接调用getpic
# def getpic():
# ###主函数切勿调用
#     cap=cv2.VideoCapture(0)
#     while(True):
#         ret,img=cap.read()
#         cv2.imshow('cam',img)
#         if cv2.waitKey(1) == ord('p'):
#             ##get char name
#             outFilename = "name.jpg"
#             print("Saving  image : ", outFilename)
#             cv2.imwrite(outFilename, img)
#             continue
#         if cv2.waitKey(1)==ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#放到run——main ，方便调用弹窗。

###图像标准色修复
def repair(filepath,file):
    ##处理算法,后得到 repaired_pic
    #导出 一个数组
    # pic_array=np.array(pic_array)
    just_for_pixnum=Image.open(filepath)
    print(just_for_pixnum.size[0],just_for_pixnum.size[1])
    outpic = [[[0 for rgb in range(3)]for col in range(just_for_pixnum.size[1])] for row in range(just_for_pixnum.size[0])]
    for i in range(just_for_pixnum.size[0]):
        for j in range(just_for_pixnum.size[1]):
            print(just_for_pixnum.size[0])
            print(file[i,j])
            print(i,j)
            r, g, b = file[i,j]
            Y=[r**2,g**2,b**2,r*g,r*b,b*g,r,g,b,1]
            Y_array=np.mat(Y)
            Kr=np.mat([[-0.0002],[0.0033],[0.0057],[0.0031],[0.0043],[-0.0109],[1.3309],[-0.4423],[-0.4569],[35.2079]])
            Kg=np.mat([[0.0024],[0.0083],[-0.0005],[-0.0060],[0.0069],[-0.0065],[-0.5964],[1.2572],[-0.2699],[46.1584]])
            Kb=np.mat([[0.0040],[-0.0123],[-0.0054],[-0.0056],[0.0006],[0.0250],[-0.5630],[-0.4003],[0.9376],[41.1212]])
            Yr=Y_array*Kr
            Yr=float(str(Yr).split('[')[2].split(']')[0])
            Yg=Y_array*Kg
            Yg = float(str(Yg).split('[')[2].split(']')[0])
            Yb=Y_array*Kb
            Yb=float(str(Yb).split('[')[2].split(']')[0])

            a = solve(-1.236e-07 * x ** 4 + 5.987e-05 * x ** 3 - 0.00907 * x ** 2 + 1.448 * x - 4.617 - Yr, x,
                      real=True)
            for k in a:
                if k.is_real:
                    if k > 0:
                        if k < 256:
                            R = k
                            print(int(round(R)))
                else:
                    continue

            b=solve(-1.834e-07*y**4+0.0001069*y**3-0.02093*y**2+2.55*y-33.56-Yb, y)
            for k in b:
                if k.is_real:
                    if k > 0:
                        if k < 256:
                            B = k
                else:
                    continue

            c=solve(5.863e-08*z**4-2.341e-05*z**3+0.003252*z**2+0.7967*z+4.788-Yg, z)
            for k in c:
                if k.is_real:
                    if k > 0:
                        if k < 256:
                            G = k
                else:
                    continue

            outpic[i][j][0] = int(round(R))
            outpic[i][j][1] =int(round(G))
            outpic[i][j][2] =int(round(B))
    repaired_pic=np.array(outpic)
    return repaired_pic


def repair_pix(pix):
    r, g, b = pix
    Y = [r ** 2, g ** 2, b ** 2, r * g, r * b, b * g, r, g, b, 1]
    Y_array = np.mat(Y)
    Kr = np.mat(
        [[-0.0002], [0.0033], [0.0057], [0.0031], [0.0043], [-0.0109], [1.3309], [-0.4423], [-0.4569], [35.2079]])
    Kg = np.mat(
        [[0.0024], [0.0083], [-0.0005], [-0.0060], [0.0069], [-0.0065], [-0.5964], [1.2572], [-0.2699], [46.1584]])
    Kb = np.mat(
        [[0.0040], [-0.0123], [-0.0054], [-0.0056], [0.0006], [0.0250], [-0.5630], [-0.4003], [0.9376], [41.1212]])
    Yr = Y_array * Kr
    Yr = float(str(Yr).split('[')[2].split(']')[0])
    Yg = Y_array * Kg
    Yg = float(str(Yg).split('[')[2].split(']')[0])
    Yb = Y_array * Kb
    Yb = float(str(Yb).split('[')[2].split(']')[0])
    r_R=0
    r_G=0
    r_B=0
    a = solve(-1.236e-07 * x ** 4 + 5.987e-05 * x ** 3 - 0.00907 * x ** 2 + 1.448 * x - 4.617 - Yr, x,
              real=True)
    for k in a:
        if k.is_real:
            if k > 0:
                if k < 256:
                    r_R = k
        else:
            continue

    b = solve(-1.834e-07 * y ** 4 + 0.0001069 * y ** 3 - 0.02093 * y ** 2 + 2.55 * y - 33.56 - Yb, y)
    for k in b:
        if k.is_real:
            if k > 0:
                if k < 256:
                    r_G = k
        else:
            continue

    c = solve(5.863e-08 * z ** 4 - 2.341e-05 * z ** 3 + 0.003252 * z ** 2 + 0.7967 * z + 4.788 - Yg, z)
    for k in c:
        if k.is_real:
            if k > 0:
                if k < 256:
                    r_B = k
        else:
            continue
    return int(round(r_R)),int(round(r_G)),int(round(r_B))

#------------------------------------------------------#
###用第一张图片做参考图像，对第二张图像进行对齐
#####基于图像特征对齐，利用ORB寻找对应点
########https://blog.csdn.net/yuanlulu/article/details/82222119
MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 0.15
def align(pic1,pic2):
    # Convert images to grayscale
    im1Gray = cv2.cvtColor(pic1, cv2.COLOR_BGR2GRAY)
    im2Gray = cv2.cvtColor(pic2, cv2.COLOR_BGR2GRAY)

    # Detect ORB features and compute descriptors.
    orb = cv2.ORB_create(MAX_FEATURES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

    # Match features.
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = matcher.match(descriptors1, descriptors2, None)

    # Sort matches by score
    matches.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    # Draw top matches
    imMatches = cv2.drawMatches(pic1, keypoints1, pic2, keypoints2, matches, None)
    cv2.imwrite("matches.jpg", imMatches)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = pic1.shape
    im1Reg = cv2.warpPerspective(pic1, h, (width, height))

    return im1Reg, h
def alignimages(pic1,pic2):
    # Read reference image
    refFilename = pic1
    print("Reading reference image : ", refFilename)
    imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)

    # Read image to be aligned
    imFilename = pic2
    print("Reading image to align : ", imFilename)
    im = cv2.imread(imFilename, cv2.IMREAD_COLOR)

    print("Aligning images ...")
    # Registered image will be resotred in imReg.
    # The estimated homography will be stored in h.
    imReg, h = align(im, imReference)

    # Write aligned image to disk.
    outFilename = "aligned.jpg"
    print("Saving aligned image : ", outFilename)
    cv2.imwrite(outFilename, imReg)

    # Print estimated homography
    print("Estimated homography : \n", h)


###LAB色差计算,计算两个像素点的色差
#####https://blog.csdn.net/qq_16564093/article/details/80698479
def colourdistance(pix1,pix2):
    r1,g1,b1=pix1
    r2, g2, b2 = pix2
    r=(r1+r2)/2
    R=r1-r2
    G=g1-g2
    B=b1-b2
    A=float((r/256+2)*(R**2))
    AA=float(4*(G**2))
    AAA=float((2+(255-r)/256)*(B**2))
    print(A,AA,AAA)
    a=math.sqrt(A+AA+AAA)
    print('a',a)
    return a
# GUI区域
#    class GUI:

# if __name__=='__main__':
#     getpic()

