# 安装scrapy和pymongo
# 基于macos

import os

# import scrapy

# 首先确认当前工作目录
# os.system('pwd')

# Todo: 可使用freeze在本目录下来备份package列表以防安装失败或做还原用
# 安装必须模组，此处使用mongo

# install_list = ['scrapy', 'pymongo']
# for x in install_list:
#     tempcmd = "pip3 install -U " + x  # install or upadte to the latest version using pip3
#     print(subprocess.Popen(tempcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                            shell=True).stdout.readlines())

# Todo: 在进入当前目录之后，使用shell创建Scrapy项目
# 脚本创造伊始就发现工作目录已经确定到当前位置
# os.system('pwd')

# 创建项目
os.system('scrapy startproject douban')

# 切换目录
os.chdir('douban/douban/spiders')  # 此处切换工作路径，否则仍旧为脚本当前路径
# os.system('pwd')

# 创建爬虫
os.system('scrapy genspider doubanMovie movie.douban.com')

# 在cfg同级目录下创建测试脚本
os.chdir('../..')
os.system('pwd')
testcode = 'from scrapy import cmdline\n\ncmdline.execute("scrapy crawl Doubanmovie".split())\n'
with open('test.py', 'w') as f:
    f.writelines(testcode)

# 修改setting文件
os.chdir('douban')
os.system('pwd')

with open('settings.py', 'r') as f:
    settings = f.readlines()

settings[19] = 'ROBOTSTXT_OBEY = False\n'  # 改变robot.txt的设置

settings.insert(43, 'COOKIES_ENABLED = False\n')  # 取消模拟登陆

# Todo: User Agent list
#  User Agent list怎么写？

# wrong Xpath format
# /html/body/div[3]/div[1]/div/div[1]/div/div/table[1]/tbody/tr/td[2]/div/a
# //*[@id="content"]/div/div[1]/div/div/table[2]/tbody/tr/td[2]/div/a

with open('settings.py', 'w') as f:
    f.writelines(settings)

# Todo: 定义item

# Todo: 设置数据模板（每条的数据格式）
#  如何分析每条数据格式并运用到其他网站数据挖掘中去

# Todo: 爬虫主类

# Todo: 设置配置文件

# Todo: 抓取后数据的后续处理

# Todo: 执行爬虫程序
