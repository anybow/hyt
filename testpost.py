__author__ = 'syber'
import MultipartPostHandler,http.cookiejar,urllib.parse,urllib.request,urllib.error
cookies = http.cookiejar.LWPCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookies),
                                MultipartPostHandler.MultipartPostHandler)
params = { "username" : "bob", "password" : "riviera",
             "file" : open("test.txt", "rb") }
opener.open("http://wwww.bobsite.com/upload/", params)