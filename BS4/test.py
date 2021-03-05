import requests

from bs4 import BeautifulSoup

headers = {
    'user_agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Connection': 'keep-alive'
}

r = requests.get('http://www.baidu.com', headers=headers)

print(r.text)

print(r)  # get the response code which is 200

r = requests.post('http://httpbin.org/post')

print(r.text)

# r = requests.get('http://www.baidu.com')
#
# print(r.text)

# r.url 获取请求地址
# r.text或者r.content获取响应内容，requests会自动转码，如有乱码尽量用r.content
# r.encoding来获取或设置网站编码

print(r.url)
print(r.content)
print(r.encoding)

# 使用r.headers获取响应头内容
print(r.headers)

print(type(r))

soup = BeautifulSoup()

# Gramma Pattern：
#   soup：Beautifulsoup(input, parse)
#   input: 一个网页的字符流
#   parse：解析器，可选html.parse、lxml、html5lib等

# 先不区分几个解析器的差别
