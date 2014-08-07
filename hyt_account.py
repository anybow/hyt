__author__ = 'syber'
#会易通结算处理主程序
#版本Version 0.11
#使用说明
import os
import textmenu
import globalv
globalv.HYT_WORKDIR = os.getcwd()   #主工作目录，缺省为脚本当前目录，运行后会让用户选择。


if __name__ == "__main__":  #调用菜单主循环
    os.system("mode con cols=60 lines=30 &color F0 &title=会易通结算处理")
    textmenu.main_menu()
    print("退回主程序")