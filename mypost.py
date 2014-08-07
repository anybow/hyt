#encoding:utf-8       #设置编码方式  
  
import urllib.request, urllib.parse, urllib.error

def ReadFileAsContent(filename):
    #print filename
    try:
        with open(filename, 'rb') as f:
            filecontent = f.read()
    except Exception as e:
        print('The Error Message in ReadFileAsContent(): ' + e.message) 
        return ''
    return filecontent


def get_content_type(filename):
    import mimetypes
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

def isfiledata(p_str): 
    import re
    
    r_c = re.compile("^f'(.*)'$")
    rert = r_c.search(str(p_str))
    #rert = re.search("^f'(.*)'$", p_str)
    if rert:
        return rert.group(1)
    else:
        return None
    
def encode_multipart_formdata(fields):
    '''
            该函数用于拼接multipart/form-data类型的http请求中body部分的内容
            返回拼接好的body内容及Content-Type的头定义
    '''
    import random
    import os
    BOUNDARY = '----------%s' % ''.join(random.sample('0123456789abcdef', 15))
    CRLF = '\r\n'
    L = []
    for (key, value) in fields:
        filepath = isfiledata(value)
        if filepath:
            L.append('--' + BOUNDARY)
            L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, os.path.basename(filepath)))
            L.append('Content-Type: %s' % get_content_type(filepath))
            L.append('')
#            L.append(ReadFileAsContent(filepath))
        else:
            L.append('--' + BOUNDARY)
            L.append('Content-Disposition: form-data; name="%s"' % key)
            L.append('')
            L.append(value)  
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def main():
    form_data = [('gShopID','489'),("addItems", r"f'D:\test.txt'"), ('validateString', '92c99a2a36f47c6aa2f0019caa0591d2')]
    form_data_re = encode_multipart_formdata(form_data)
    print(form_data_re)

if __name__=="__main__":
    main()

