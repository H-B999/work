# urlib库的使用

# import urllib.request
# import urllib.parse
#
# response = urllib.request.urlopen('https://www.python.org')
# # print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))


# import urllib.request
# import urllib.parse
# import socket
# import urllib.error
#
# # https://www.httpbin.org  这个网址可以提供HTTP请求测试
#
# # data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
# # response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
# # print(response.read().decode('utf-8'))
#
# try:
#     response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
#     print(response)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')


# Request方法
# import urllib.request
#
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# from urllib import request, parse
#
# url = 'https://www.httpbin.org/post'
# # 火狐浏览器 ：Mozilla/4.0 (compatible; MSIE 5.5; Windoows NT
# headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windoows NT)',
#            'Host': 'www.httpbin.org'}
# dict = {'name': 'germey'}
# data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# https://ssr3.scrape.center/ 登录认证窗口
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError


# 解决登录认证
# username = 'admin'
# password = 'admin'
# url = 'https://ssr3.scrape.center/'
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)


# 代理
# from urllib.request import ProxyHandler, build_opener
# from urllib.error import URLError
#
# proxy_handler = ProxyHandler({
#     'http': 'http:/127.0.0.1:8080',
#     'https': 'https:/127.0.0.1:8080'
# })
# opener = build_opener(proxy_handler)
#
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)


# COOKIE  获取
# import http.cookiejar, urllib.request
#
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# for item in cookie:
#     print(item.name + "=" + item.value)

# 文本形式存储cookie
# import urllib.request, http.cookiejar
#
# filename = 'cookie.txt'
# # MozillaCookieJar，LWPCookieJar都是cookiejar的子类，它们俩都可以存储，读取，只不过存储格式不一样
# # cookie = http.cookiejar.MozillaCookieJar(filename)
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)


# 读取cookie
# import urllib.request, http.cookiejar
#
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# print(response.read().decode('utf-8'))


# 处理异常
# URLError
from urllib import request, error

# try:
#     response = request.urlopen('http://cuiqingcai.com/404')
# # except error.URLError as e:
# #     print(e.reason)
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')

try:
    response = request.urlopen('https://cuiqingcai.com/404')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
