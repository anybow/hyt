__author__ = 'syber'

# -*- coding:utf-8 -*-
# python3.3.3
import  os, re, urllib.parse, urllib.request, http.cookiejar,globalv,subprocess,MultipartPostHandler
"""cookie"""
cookie=http.cookiejar.LWPCookieJar()
chandle=urllib.request.HTTPCookieProcessor(cookie)
"""获取数据"""
def getData(url,headers={}):
    r=urllib.request.Request(url)
    r.add_header('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)')
    r.add_header('Content-Type', 'application/x-www-form-urlencoded')
    r.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    for k,v in headers.items(): r.add_header(k, v) # 为特定的 request 添加指定的 headers
    opener=urllib.request.build_opener(chandle)
    u=opener.open(r)
    data=u.read()
    try:
        data=data.decode('utf-8')
    except:
        data=data.decode('gbk','ignore')
    return data

def downloadData(url):
    r=urllib.request.Request(url)
    r.add_header('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)')
    r.add_header('Content-Type', 'application/x-www-form-urlencoded')
    r.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    r.add_header('Accept-Encoding','header_gzip = None')
    opener=urllib.request.build_opener(chandle)
    u=opener.open(r)
    data=u.read()
    return data

def postData(url,data):
    data=urllib.parse.urlencode(data);data=bytes(data,'utf-8')
    r=urllib.request.Request(url,data)
    opener=urllib.request.build_opener(chandle)
    u=opener.open(r)
    data=u.read()
    try:
        data=data.decode('utf-8')
    except:
        data=data.decode('gbk','ignore')
    return data


def login(name,pwd):
    url='http://10.100.8.38:8080/crm/'
    getData(url)      #访问网站
    par={
        "pwd":'',
        "usr":'',
    }
    par.update({"usr":name,"pwd":pwd})
    url='http://10.100.8.38:8080/crm/userLogin.do'
    postData(url,par)    #登录系统
    url ='http://10.100.8.38:8080/crm/meeting/initClearlong.do'    #营销部—>会易通出账 —> 全球会议通挑拣长话单
    getData(url)
    posturl ='http://10.100.8.38:8080/crm/meeting/clearlong.do'
    pdata={

    }
    globalv.HYT_WORKDIR = os.getcwd()
#下载挑拣后话单文件，并且解压处理
    downloadurl = 'http://10.100.8.38:8080/crm/HYT/downloadfile.jsp?filename=/usr/local/tomcat5/webapps/crm/uploadfile/meeting/%cc%f4%bc%f0%ba%f3%bb%b0%b5%a5.zip'
#    data = downloadData(downloadurl)
#    with open(globalv.HYT_WORKDIR+"\新billid\\挑拣后话单.zip", 'wb') as f:
#       f.write(data)
    print("download success")
    os.chdir("新billid")
    retcode =subprocess.call(r"WinRAR e 挑拣后话单.zip",shell=True)
    if retcode:
        print("挑拣后话单解压缩成功，生成新的billid.txt文件")
    else:
        print("挑拣后话单文件解压失败，请仔细检查......")
    os.system("pause")

"""------输入帐号密码------"""
if __name__ == "__main__":  #调用菜单主循环
    login('0530','355570')
