import requests

from bs4 import BeautifulSoup

# 打印soup对象的内容

headers = {
    'user_agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Connection': 'keep-alive'
}

r = requests.get('http://www.baidu.com', headers=headers)

soup = BeautifulSoup(r.content,
                     'html.parser')  # when using r.text I get random codes. So, use r.content instead.

print(soup.prettify())

# 利用标签定位对象
# print('# ' * 30)
# print(soup.title)
# print('# ' * 30)
# print(soup.a)
# print('# ' * 30)
# print(soup.a.name)
# print('# ' * 30)
# print(soup.a.attrs)
# print('# ' * 30)
# print(soup.a['id'])
# print('# ' * 30)
# print(soup.a.get('id'))
# print('# ' * 30)

# 获取属性获取标签内部名字
print(soup.title.string)

# 搜索当前tag下的所有tag子节点，并判断是否符合过滤器条件
# find_all(name=None, attrs={}, recursive=Ture, text=None, limit=None, **kwargs)

# 搜索当前tag下的第一个tag子节点，并判断是否符合过滤器条件
# find(name=None, attrs={},  recursive=Ture, text=None, **kwargs)

# to be continued
