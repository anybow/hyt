__author__ = 'syber'
#会易通结算处理主序
#初始化工作目录，检验工作目录完整性
import os
import tkinter.filedialog
import globalv

def init_work_dir():    #选择工作根目录，并创建工作所需子目录结构
    hytworkdir = tkinter.filedialog.askdirectory()
    globalv.HYT_WORKDIR = hytworkdir
    os.chdir(hytworkdir)  #切换到选择的目录作为工作目录
    if not verify_dir(): #如果工作目录不完整则创建新目录
        if not os.path.exists(hytworkdir+"\北京文件"):
            os.mkdir(hytworkdir+"\北京文件")
        if not os.path.exists(hytworkdir+"\七文件"):
            os.mkdir(hytworkdir+"\七文件")
            os.mkdir(hytworkdir+"\七文件\非集团")
            os.mkdir(hytworkdir+"\七文件\集团")
            os.mkdir(hytworkdir+"\七文件\解压文件")
        if not os.path.exists(hytworkdir+"\新billid"):
            os.mkdir(hytworkdir+"\新billid")
        if not os.path.exists(hytworkdir+"\原始四文件"):
            os.mkdir(hytworkdir+"\原始四文件")
    if globalv.DEBUG:  print(os.listdir(hytworkdir))

def verify_dir():  #检验工作目录是否完成，缺任何一个就返回false
    hytworkdir=globalv.HYT_WORKDIR
    hytdirlist={hytworkdir+"\北京文件",hytworkdir+"\七文件",hytworkdir+"\七文件\非集团",hytworkdir+"\七文件\集团",hytworkdir+"\七文件\解压文件",hytworkdir+"\新billid",hytworkdir+"\原始四文件"}
    for x in hytdirlist:
        if not os.path.exists(x):
            globalv.V_WORKDIR = False
            return False
            break
    globalv.V_WORKDIR = True
    return True

def select_dir():
    hytworkdir = tkinter.filedialog.askdirectory()
    globalv.HYT_WORKDIR = hytworkdir

if __name__ == "__main__":  #初始化工作目录
    print(globalv.HYT_WORKDIR)