#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import json
import random

import requests

# In[2]:


# res = requests.get("https://gkcx.eol.cn/hotschool")
# res.encoding="utf-8"
# print(res.text)


# In[3]:


# only to find out that the page is loaded dynamically
# So I will try to use selenium to repeat the process


# In[4]:


user_agent = [
    "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
]

# In[5]:


# find the data source, under xhr tab there is a link
# https://api.eol.cn/gkcx/api/?access_token=&admissions=&central=&department=&dual_class=&f211=&f985=&is_doublehigh=&keyword=&nature=&page=1&province_id=&school_type=&signsafe=&size=15&sort=view_month&sorttype=desc&type=&uri=apidata/api/gk/school/lists
# there is a page, by definition it is a json file


# In[6]:


data = []


# In[7]:


# url = 'https://api.eol.cn/gkcx/api/?access_token=&keyword=&page=1&province_id=&school_type=&signsafe=&size=20&sort=view_month&sorttype=desc&type=&uri=apidata/api/gk/school/lists'


# In[8]:


def getOnePageJson(url):
    res = requests.get(url, headers={'User-Agent': random.choice(user_agent)})
    json_data = json.loads(res.text)
    # print(json_data)
    items = json_data.get('data').get('item')  # 解码json file中的二级结构，获得以address开始的list of dicts
    # print(items)
    for each_item in items:
        name = each_item.get('name')
        prov_name = each_item.get('province_name')
        type_name = each_item.get('type_name')
        rank = str(each_item.get('rank'))
        view_month = each_item.get('view_month')
        data.append([name, prov_name, type_name, rank, view_month])


# In[9]:


# getOnePageJson(url)


# In[10]:


def save_to_csv(fileName):
    with open(fileName, 'w') as f:
        csvfile = csv.writer(f)
        csvfile.writerow(['学校名字', '所在省份', '学校类型', '网站热度排名', '月点击量'])
        for each_line in data:
            csvfile.writerow(each_line)


# In[11]:


def main(start, end):
    for i in range(start, end + 1):
        print(f'current page is {i}')
        url = f'https://api.eol.cn/gkcx/api/?access_token=&keyword=&page={i}&province_id=&school_type=&signsafe=&size=20&sort=view_month&sorttype=desc&type=&uri=apidata/api/gk/school/lists'
        getOnePageJson(url)
    save_to_csv('Uni_Rank.csv')
    print('Data fetching is over')


# In[12]:


if __name__ == "__main__":
    main(1, 3)
