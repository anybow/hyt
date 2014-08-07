__author__ = 'syber'
import initworkspace
import hyt_ftp
import crm_billid
import globalv
import os
def main_menu():
    one=" "
    while True:
        print("\n                 会易通结算处理系统\n\n")
        print(" [0]创建工作目录  ",end="")
        if initworkspace.verify_dir():
            print("     。。。。。。已完成工作目录创建\n")
        else:
            print("\n")
        print(" [1]下载FTP文件   ",end="")
        if hyt_ftp.veryfy_ftpfile(globalv.HYT_WORKDIR):
            print("     。。。。。。已完成FTP文件下载")
        else:
            print("\n")

        print(" [2]CRM数据处理\n")
        print(" [X]退出\n\n")
        print(" 工作根目录：%s\n"%globalv.HYT_WORKDIR+" 按[S]重新选择目录\n")
        one = input('     请输入菜单编号:')
        if one == 'x'or one == 'X':
            print('成功退出')
            break
        if one == 's'or one == 'S':
            initworkspace.select_dir()
            os.system("cls")
        elif one.isdigit()and int(one)==0:
          if globalv.V_WORKDIR:
            print( "工作目录已存在，请勿重复操作")
          else:
            initworkspace.init_work_dir()   #根据用户选择初始化工作目录
          os.system("pause &cls")
        elif  one.isdigit()and int(one)==1:
          os.system("cls")
          print( "  抓取FTP数据......\n")
          hyt_ftp.hytaccountftp(globalv.HYT_WORKDIR)
          os.system("pause  &cls")
        elif  one.isdigit()and int(one)==2:
           print( "CRM数据处理....")
           crm_billid.login('0530','355570')
           os.system("pause  &cls")
        else:
            print( '输入错误，请重新选择菜单对应的数字')
            os.system("pause  &cls")
            if not initworkspace.verify_dir():
                print("工作目录缺失")




