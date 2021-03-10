#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import urllib
import os
import time
import random
import numpy as np


# In[2]:


# first we need to find out the change pattern of the url


# In[3]:


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


# In[4]:


address = str(1049732)


# In[5]:


def gethtml(index,number):
    url = f'https://movie.douban.com/celebrity/{number}/photos/?type=C&start=' + str(index)
    res = requests.get(url,headers={'User-Agent':random.choice(user_agent)})
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


# In[6]:


images = []


# In[7]:


# get the # of pics on the first page
imagecount = len(gethtml(0,address).find('ul', class_ = 'poster-col3 clearfix').find_all('img'))


# In[8]:


print(imagecount)


# In[9]:


def delAll(path):
    if os.path.isdir(path):
        files = os.listdir(path)
        # 遍历并删除文件
        for file in files:
            p = os.path.join(path, file)
            if os.path.isdir(p):
                # 递归
                delAll(p)
            else:
                os.remove(p)
        # 删除文件夹
        os.rmdir(path)
    else:
        os.remove(path)


# In[10]:


def getImages(pageNum,name,number):
    if os.path.exists(name):
        delAll(name)
    os.mkdir(name)
    global address,images,imgLen
    for k in range(pageNum):
        # 1、存储soup对象
        eachsoup = gethtml(k*imagecount,number)
        # 2、获取图片列表父元素
        imageList = eachsoup.find('ul', attrs={'class': "poster-col3 clearfix"})
        # 3、获取所有image
        #     通过extend方法，还是一个list，如果用append会是多个list，下面的循环的就要额外处理了
        images.extend(imageList.find_all('img'))
    #3、用循环处理所有li内的具体内容
    for i in range(len(images)):
        try:
            #获取图片后缀名，防止真实网址图片为png，jpg，gif等格式
            suffix = images[i]['src'][-3:]
            image_name = str(i+1)+'.'+suffix
            print(images[i]['src'])
            print(image_name)
            
            # urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None)
            # 将URL表示的网络对象复制到本地文件。如果URL指向本地文件，则对象将不会被复制，除非提供文件名
            
            urllib.request.urlretrieve(images[i]['src'],name + "/" + image_name)      
            time.sleep(np.random.rand())
        except Exception as error:
            print(error)
            print('Save file error!')
    print('Data fetching finished')


# In[11]:


address = str(1004572)
getImages(3,'Gabrielle Anwar',address)

