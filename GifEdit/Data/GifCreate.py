from asyncio.windows_events import NULL
from cProfile import label
from cgitb import text
from fileinput import filename
from textwrap import fill
import tkinter
from turtle import end_fill, left, speed
from PIL import Image as PILImage
import os
from tkinter import * 
from PIL import ImageSequence
import random


def GetFirstFile(firstdir):
    pathdir = os.listdir(firstdir)#获取所在路径下的所有文件
    file01 = pathdir[0]#剔除最下级
    return file01

deskPath=os.path.join(os.path.expanduser('~'),"Desktop")
print(deskPath)
print(GetFirstFile(f"{deskPath}\\GifEdit\\GifSrc\\"))
def gifBreak():
    rFile=GetFirstFile(f"{deskPath}\\GifEdit\\GifSrc\\")
    with PILImage.open(f"{deskPath}\\GifEdit\\GifSrc\\{rFile}") as im:
        index = 1
        ze=''
        for frame in ImageSequence.Iterator(im):
            if index < 10 :
                ze='0'
            else:
                ze=''
            frame.save(f"{deskPath}\\GifEdit\\GifFrames\\{ze}{index}.png")
            index += 1



def fightingCreate():
    global inputField
    speed=inputField.get()
    if speed == '':
        return
    print(speed)
    # 初始化图片地址文件夹
    image_path =f"{deskPath}\\GifEdit\\ImgSrc"
    # 获取文件列表
    files = os.listdir(image_path)
    # 定义第一个文件的全局路径
    file_first_path = os.path.join(image_path, files[0])
    # 获取Image对象
    img = PILImage.open(file_first_path)
    # 初始化文件对象数组
    images = []
    for image in files[1:]:
        # 获取当前图片全量路径
        img_path = os.path.join(image_path, image)
        # 将当前图片使用Image对象打开、然后加入到images数组
        curImg=PILImage.open(img_path)
        images.append(curImg)
    # 保存并生成gif动图
    img.save(f"{deskPath}\\GifEdit\\NewGif.gif", save_all=True, append_images=images, loop=0, duration=int(speed))

ImgList  = []
GifList = []
def freshImgList():
    global ImgList
    global GifList
    global ImgListBox
    global GifListBox
    image_path =f"{deskPath}\\GifEdit\\ImgSrc\\"
    gif_path =f"{deskPath}\\GifEdit\\GifSrc\\"
    files = os.listdir(image_path)
    files2 = os.listdir(gif_path)
    ImgListBox.delete(first=0,last=len(ImgList))
    GifListBox.delete(first=0,last=len(GifList))
    ImgList=files
    GifList=files2

    global frames
    global numIdx
    frames=files
    numIdx=len(files)


    for item in ImgList:                 # 第一个小部件插入数据
        ImgListBox.insert(END,item)
    for item in GifList:                 # 第一个小部件插入数据
        GifListBox.insert(END,item)


def freshImgListStart():
    global ImgList
    global GifList
    global ImgListBox
    global GifListBox
    image_path =f"{deskPath}\\GifEdit\\ImgSrc\\"
    gif_path =f"{deskPath}\\GifEdit\\GifSrc\\"
    files = os.listdir(image_path)

    global frames
    global numIdx
    #f"{deskPath}\\ImgSrc\\"


    numIdx=len(files)

    files2 = os.listdir(gif_path)
    ImgList=files
    GifList=files2
    for item in files:                 # 小部件插入数据
        ImgListBox.insert(END,item)
    for item in files2:                 
        GifListBox.insert(END,item)






root = Tk()   

numIdx = 0
frames = []




label02=Label(root,text=f'Png资源文件夹中的图片\n-双击查看选中帧-',justify=CENTER)
label03=Label(root,text=f'Gif资源文件夹中的图片',justify=CENTER)
label04=Label(root,text=f'帧间时间间隔')
ImgListBox  = Listbox(root)
GifListBox  = Listbox(root,height=1)
inputField = Entry(root)
label04.pack()
inputField.pack() 
btn=Button(text='创建Gif',command=fightingCreate)
btn.pack()
bBtn=Button(text='拆解Gif',command=gifBreak)
bBtn.pack()
fBtn=Button(text='刷新资源文件显示',command=freshImgList)
fBtn.pack()       
freshImgListStart()
# 创建一个Canvas，设置其背景色为白色

label02.pack()
ImgListBox.pack()
label03.pack()
GifListBox.pack()


# def update(idx):  # 定时器函数
#     global inputField
#     speed=inputField.get()
#     frame = frames[idx]
#     idx += 1  # 下一帧的序号：在0,1,2,3,4,5之间循环(共6帧)
#     label00.configure(image=frame)  # 显示当前帧的图片
#     root.after(int(speed), update, idx % numIdx)  # 0.1秒(100毫秒)之后继续执行定时器函数(update)


label00 = Label(root)

# root.after(1000, update, 0)  # 立即启动定时器函数(update)


label01=Label(root,text=f'当前桌面路径：{deskPath}\\GifEdit\n资源文件路径：{deskPath}\\GifEdit\\ImgSrc',justify=LEFT)
label01.pack()
label00.pack()
frame=None
def showImg(event):
    global label00
    global frame
    thisImgName=ImgListBox.get(ImgListBox.curselection())
    frame=PhotoImage(file=f"{deskPath}\\GifEdit\\ImgSrc\\{str(thisImgName)}")
    label00.config(image=frame)  # 显示当前帧的图片
    print(thisImgName)
ImgListBox.bind("<Button-1>", showImg)




root.mainloop()                 # 进入消息循环


