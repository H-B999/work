# import re
#
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())

import re

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())


# import re
#
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())


# import re
#
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result.group())
# print(result.group(1))


# import re
#
# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
# print(result.group(1))


# import re
# #
# content = '(百度) www.baidu.com'
# result = re.match('\(百度 \) www\.baidu\.com', content)
# print(result.group())


# import re
#
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result.group())

import re

html = '''<div id="songs-list">
<h2 class="title"> 经典老歌 </h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2"> 一路上有你 </li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐"> 沧海一声笑 </a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦"> 往事随风 </a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond"> 光辉岁月 </a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳"> 记事本 </a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君"> 但愿人长久 </a>
</li>
</ul>
</div>'''

# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
# if result:
#     print(result.group(1), result.group(2))


# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)
# print(type(results))
# for result in results:
#     print(result)
#     print(result[0], result[1], result[2])


# import re
#
# content = '54aK54yr5oiR54ix5L2g'
# content = re.sub('\d+', '', content)
# print(content)


# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
# for result in results:
#     print(result[1])


# html = re.sub('<a.*?>|</a>', '', html)
# print(html)
# results = re.findall('<li.*?>(.*?)</li>', html, re.S)
# for result in results:
#     print(result.strip())


# import re
#
# content1 = '2016-12-15 12:00'
# content2 = '2016-12-17 12:55'
# content3 = '2016-12-22 13:21'
# pattern = re.compile('\d{2}:\d{2}')
# result1 = re.sub(pattern, '', content1)
# result2 = re.sub(pattern, '', content2)
# result3 = re.sub(pattern, '', content3)
# print(result1, result2, result3)


#  因为这个网址是HTTP2.0协议，所以requests不支持
# import requests
#
# url = "https://spa16.scrape.center/"
# response = requests.get(url)
# print(response.text)


# import httpx
#
# client = httpx.Client(http2=True)
# response = httpx.get("https://spa16.scrape.center/")
# print(response.text)


import httpx

with httpx.Client(http2=True) as clinet:
    response = clinet.get('https://www.httpbin.org/get')
    print(response.http_version)


