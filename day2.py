# from urllib.parse import urlparse
#
# result = urlparse('https://www.baidu.com/index.html;user?id=5#comment', scheme='https',allow_fragments=False)
# print(type(result))
# print(result)


# from urllib.parse import urlunparse
# 长度必须是六
# data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data))

# from urllib.parse import urlsplit
#
# result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
# print(result, result.scheme, result[1], sep='\n')


# from urllib.parse import urlunsplit
#
# # 这个方法长度必须是五
# data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6']
# print(urlunsplit(data))


# from urllib.parse import urljoin
#
# print(urljoin('http://www.baidu.com', 'FAQ.html'))
# print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
# print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
# print(urljoin('http://www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com#comment', '?category=2'))

# from urllib.parse import urlencode
#
# params = {
#     'name': 'germey',
#     'age': 22
# }
# base_url = 'https://www.baidu.com?'
# url = base_url + urlencode(params)
# print(url)

#
# from urllib.parse import parse_qs
#
# query = 'name=germey&age=22'
# print(parse_qs(query))

# from urllib.parse import parse_qsl
#
# query = 'name=germey&amp;age=22'
# print(parse_qsl(query))


# from urllib.parse import quote
#
# keyword = '壁纸 '
# url = 'https://www.baidu.com/s?wd=' + quote(keyword)
# print(url)


# from urllib.parse import unquote
#
# url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
# print(unquote(url))


# from urllib.robotparser import RobotFileParser
#
# rp = RobotFileParser()
# rp.set_url('http://www.baidu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('Baiduspider', 'http://www.baidu.com/'))
# print(rp.can_fetch('Baiduspider', 'http://www.baidu.com/homepage/'))
# print(rp.can_fetch('Googlebot', "http://www.baidu.com/homepage/"))


# import requests
#
# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)


# import requests
#
# r = requests.post('http://httpbin.org/post')
# r = requests.put('http://httpbin.org/put')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')


# import requests
#
# r = requests.get('http://httpbin.org/get')
# print(r.text)


# import requests
#
# data = {
#     'name': 'germey',
#     'age': 22
# }
# r = requests.get("https://httpbin.org/get", params=data)
# print(r.text)


# import requests
#
# r = requests.get("http://httpbin.org/get")
# print(type(r.text))
# print(r.json())
# print(type(r.json()))


# import requests
# import re
#
#
# r = requests.get("https://ssr1.scrape.center/")
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)


# import requests
#
# r = requests.get("https://scrape.center/favicon.ico")
# print(r.text)
# print(r.content)


# import requests
#
# r = requests.get("https://scrape.center/favicon.ico")
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)


# import requests
#
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get("https://ssr1.scrape.center/", headers=headers)
# print(r.text)


# import requests
#
# data = {'name': 'germey', 'age': '22'}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)


# import requests
#
# r = requests.get('https://ssr1.scrape.center/')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)


# import requests
#
# r = requests.get('https://ssr1.scrape.center/')
# print(requests.codes.created)
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')


# import requests
#
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('https://httpbin.org/post', files=files)
# print(r.text)


# import requests
#
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)


# import requests
# import urllib3
#
# urllib3.disable_warnings()
#
# headers = {
#     'Cookie': '_octo=GH1.1.1138974658.1657981201; _device_id=db16f441602df47573479a8bdf596c19; tz=Asia/Shanghai; preferred_color_mode=light; user_session=cPF-RJuN8uJNYfn6aizc6XeIE9wl7mMjZxRcWSrNU2AhQRCL; __Host-user_session_same_site=cPF-RJuN8uJNYfn6aizc6XeIE9wl7mMjZxRcWSrNU2AhQRCL; tz=Asia/Shanghai; color_mode={"color_mode":"auto","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}; logged_in=yes; dotcom_user=H-B999; has_recent_activity=1; _gh_sess=Vr/cVLdy9bXXVBQ6fuAuqJjWVd5LGFR5nRkF+xRWitoo/4EkFs9AV2MUKo+KQs7MWA/EGsNrBDBkst70BCX/c1YMC9gPYGDZEwYv1Kel1nw94d2Y2g5GWe5hvjXvXnikRNus8UdH5WBLJRwGGcFFATiTToyHqmqkPctW2nBS2WL7idb0sHRhKxLkS8JmZr4Juwuli9EAVykAIxxgoOKAw44+MF10q9lYye3YRwd1XLMdTBM7u42fGJaRbRKvtRaQj9TYYIaQp4dmz4TH3zh1/1HByx2VnK9a/Fe+ovYv6vPxCEH/zH2zl9Koj8Elhs1ZXb0KOIr/4I9SCpf/J6Za9QJhuTkviwICYQDcUq5vRRHrGWUjVQ9Z7IxZuffw8MLPIchuOi9+VdCyMmvGpi+3cS5N6Hp+Phw81p1yuQlMLNoMpBlmnkoZr4MdLVpkR+W4--FqofaCD/QGqos/xR--4YeXCzS9DndM+/Lfl9AXag==',
# }
# r = requests.get('https://github.com', headers=headers, verify=False)
# print(r.text)


# import requests
# import urllib3
#
# urllib3.disable_warnings()
#
# cookies = '_octo=GH1.1.1138974658.1657981201; _device_id=db16f441602df47573479a8bdf596c19; tz=Asia/Shanghai; preferred_color_mode=light; user_session=cPF-RJuN8uJNYfn6aizc6XeIE9wl7mMjZxRcWSrNU2AhQRCL; __Host-user_session_same_site=cPF-RJuN8uJNYfn6aizc6XeIE9wl7mMjZxRcWSrNU2AhQRCL; tz=Asia/Shanghai; color_mode={"color_mode":"auto","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}; logged_in=yes; dotcom_user=H-B999; has_recent_activity=1; _gh_sess=3KC+TJjsyQ/a/6s4RWyB4f1q+Zi6jdRCLhnUPMiTtCNdHbyN39EoZsf/NIWejyayBEy2bH4QzyCf4qaGor4qMe1Pyy6yPyD+YDV3Uw9Y+hcVIYHr9sP5dl0MSZCllSBH38u/Yn/M/GG3tr03T2EJY126qyo5LCp+qbHfQOUElrjbpHWpwsQc3hZvQv8Cuq9OawaF7lXYVchjGC2/ztHCSZNmc/gYYqLn6NknsXRbwbE5NGsWzowcJ5E2pK2ABJdtc+TijruoRLvgh32CSC8zjyprj4x3LiM64lD7nyvYwdQxlEgt9dmW67nu+J9AupomfbE+HvO3G8wKmSb8yF/gP54gFgkOtLaehmCxMMhmBnfjwTGoC/+rGZhgVlT0QjU5xklMcar6wuo/oHtKxjPjSXlgwfhScBe4NKRCe8D+OJs0jdt4vYLqX5qroz6DvqVC--GFlC9bOfmm66NLhR--u1ju09DAwmVeD+2tGO0pCA=='
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
#                   '53.0.2785.116 Safari/537.36'
# }
# for cookie in cookies.split(';'):
#     key, value = cookie.split('=', 1)
#     jar.set(key, value)
# r = requests.get('https://www.github.com', cookies=jar, headers=headers, verify=False)
# print(r.text)


# import requests
#
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)


# import requests
#
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


# import logging
# import requests
# logging.captureWarnings(True)
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)


# import requests
# from requests.auth import HTTPBasicAuth
#
# r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
# print(r.status_code)


# import requests
# from requests_oauthlib import OAuth1
#
# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'


# from requests import Request, Session
#
# url = 'http://httpbin.org/post'
# data = {'name': 'germey'}
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
# }
# s = Session()
# req = Request('POST', url, data=data, headers=headers)
# prepped = s.prepare_request(req)
# r = s.send(prepped)
# print(r.text)


# 多进程的用法
# import multiprocessing
#
#
# def process(num):
#     print('Process:', num)
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         p = multiprocessing.Process(target=process, args=(i,))
#         p.start()
#     print('CPU number:' + str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print('Child process name: ' + p.name + ' id: ' + str(p.pid))
#
#     print('Process Ended')


# from multiprocessing import Process, Lock
# import time
#
#
# class MyProcess(Process):
#     def __init__(self, loop, lock):
#         Process.__init__(self)
#         self.loop = loop
#         self.lock = lock
#
#     def run(self):
#         for count in range(self.loop):
#             time.sleep(0.1)
#             self.lock.acquire()
#             print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))
#             self.lock.release()
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10, 15):
#         p = MyProcess(i, lock)
#         p.start()


# from multiprocessing import Process, Semaphore, Lock, Queue
# import time
#
# buffer = Queue(10)
# empty = Semaphore(2)
# full = Semaphore(0)
# lock = Lock()
#
#
# class Consumer(Process):
#
#     def run(self):
#         global buffer, empty, full, lock
#         while True:
#             full.acquire()
#             lock.acquire()
#             buffer.get()
#             print('Consumer pop an element')
#             time.sleep(1)
#             lock.release()
#             empty.release()
#
#
# class Producer(Process):
#     def run(self):
#         global buffer, empty, full, lock
#         while True:
#             empty.acquire()
#             lock.acquire()
#             buffer.put(1)
#             print('Producer append an element')
#             time.sleep(1)
#             lock.release()
#             full.release()
#
#
# if __name__ == '__main__':
#     p = Producer()
#     c = Consumer()
#     p.daemon = c.daemon = True
#     p.start()
#     c.start()
#     p.join()
#     c.join()
#     print('Ended!')


# from multiprocessing import Process, Semaphore, Lock, Queue
# import time
# from random import random
#
# buffer = Queue(10)
# empty = Semaphore(2)
# full = Semaphore(0)
# lock = Lock()
#
# class Consumer(Process):
#
#     def run(self):
#         global buffer, empty, full, lock
#         while True:
#             full.acquire()
#             lock.acquire()
#             print('Consumer get', buffer.get())
#             time.sleep(1)
#             lock.release()
#             empty.release()
#
#
# class Producer(Process):
#     def run(self):
#         global buffer, empty, full, lock
#         while True:
#             empty.acquire()
#             lock.acquire()
#             num = random()
#             print('Producer put ', num)
#             buffer.put(num)
#             time.sleep(1)
#             lock.release()
#             full.release()
#
#
# if __name__ == '__main__':
#     p = Producer()
#     c = Consumer()
#     p.daemon = c.daemon = True
#     p.start()
#     c.start()
#     p.join()
#     c.join()