__author__ = 'syber'
import os
#from ftplib import FTP
import  ftplib
def hytaccountftp(ftpfilepath):
    """
    FTP下载文件
    :param ftpfilepath:
    """
    ftp=ftplib.FTP()
#    ftp.set_debuglevel(2) #打开调试级别2，显示详细信息
    ftp.connect("118.85.207.176",21,600) #连接
    ftp.login('monthbill','Ya2G26TV') #登录，如果匿名登录则用空串代替即可
    try:
        list = ftp.nlst()       # 获得目录列表
        fileno=1
        for ftpfilename in list:
            filesize = ftp.size(ftpfilename)
            print("   [%s]"%fileno+ftpfilename+"文件大小：%s Kb   \n      下载中......"%(filesize//1024),end="")
            path = ftpfilepath+"\\原始四文件\\" + ftpfilename    # 文件保存路径
            f = open(path,'wb')         # 打开要保存文件
            filename = 'RETR ' + ftpfilename   # 保存FTP文件
            ftp.retrbinary(filename,f.write) # 保存FTP上的文件
            print("OK\n")
            fileno+=1
    except ftplib.error_perm:
        print("FTP文件不存在")

#    ftp.set_debuglevel(0) #关闭调试
    ftp.quit() #退出ftp服务器

def veryfy_ftpfile(ftpfilepath):
    """
     检验FTP远程文件与本地文件的大小，如果相同返回True，有任何一个差异返回False
    :param ftpfilepath:
    :return:
    """
    ftp=ftplib.FTP()
    ftp.connect("118.85.207.176",21,600) #连接
    ftp.login('monthbill','Ya2G26TV') #登录，如果匿名登录则用空串代替即可
    sizeflag = False
    try:
        list = ftp.nlst()       # 获得目录列表
        for ftpfilename in list:
            filesize = ftp.size(ftpfilename)
            localfilepath = ftpfilepath+"\\原始四文件\\" + ftpfilename    # 文件保存路径
            if  os.path.isfile(localfilepath):
                localsize=os.stat(localfilepath).st_size#获取本地文件的大小
                if filesize == localsize:
                    sizeflag = True
                else:
                    sizeflag = False
                    return sizeflag
                    break
            else:    #文件不存在返回False
                    sizeflag = False
                    return sizeflag
                    break
        return  sizeflag
        ftp.quit()
    except ftplib.error_perm:
        print("     FTP文件不存在",end="")
        ftp.quit()
        return sizeflag

if __name__ == '__main__':
    hytaccountftp(os.getcwd())