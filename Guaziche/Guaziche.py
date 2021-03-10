#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import csv
import random
import time


# In[2]:


# Setting chrome to run silently
option=webdriver.ChromeOptions()
option.add_argument('headless')


# In[3]:


# Go analyse the weblink
# https://www.guazi.com/sz/buy/o1/


# In[4]:


# url="https://www.guazi.com/sz/buy/o1/"
# driver = webdriver.Chrome(options=option)
# driver.get(url)


# In[5]:


# # Notice that carlist clearfix js-top is not the class name we desire
# carlist = driver.find_element_by_class_name('carlist')
# # Notice that elements here, not element
# lilist = carlist.find_elements_by_tag_name('li')


# In[6]:


# The we prepare for a loop to extract the single piece of data


# In[7]:


# datalist = []


# In[8]:


# for each_li in lilist:
#     name = each_li.find_element_by_class_name('t').text
    
#     # if we do not use text.split('|'), it prints out a string with | sign in it
#     # after using it, we have a list of string with | sign subtracted
    
#     year = each_li.find_element_by_class_name('t-i').text.split('|')[0]
#     distance = each_li.find_element_by_class_name('t-i').text.split('|')[1]
#     price = each_li.find_element_by_class_name('t-price').find_element_by_tag_name('p').text
#     datalist.append([name,year,distance,price])


# In[9]:


# print(datalist)


# In[10]:


def getOnePageCar(url):
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    carlist = driver.find_element_by_class_name('carlist')
    lilist = carlist.find_elements_by_tag_name('li')
    datalist = []
    for each_li in lilist:
        name = each_li.find_element_by_class_name('t').text
        # if we do not use text.split('|'), it prints out a string with | sign in it
        # after using it, we have a list of string with | sign subtracted
        year = each_li.find_element_by_class_name('t-i').text.split('|')[0]
        distance = each_li.find_element_by_class_name('t-i').text.split('|')[1]
        # here we separate currency sign and the digits part for nicer view of data
        price = each_li.find_element_by_class_name('t-price').find_element_by_tag_name('p').text.split('万')[0]
        datalist.append([name,year,distance,price])
    return datalist    


# In[11]:


def getManyPagesCar(pageNumber, fileName):
    allCar = []
    newallCar = []
    for i in range(1, 1 + pageNumber):
        print(f'I am fetching cars on page {i} for ya!')
        url = f'https://www.guazi.com/sz/buy/o{pageNumber}/#bread'
        eachPageCar = getOnePageCar(url)
        allCar += eachPageCar
        time.sleep(random.randint(1,2))
    # delete duplicates
    for car in allCar:
        if car not in newallCar:
            newallCar.append(car)
    with open(fileName, 'w', encoding = 'utf-8') as f:
        csvfile = csv.writer(f)
        csvfile.writerow(['车名','使用时长', '使用里程', '销售价格（万）'])
        for eachCar in newallCar:
            csvfile.writerow(eachCar)
        print('Finished data fetching!')


# In[12]:


# the .csv is important
getManyPagesCar(10, 'Price as of Mar 10th.csv')

