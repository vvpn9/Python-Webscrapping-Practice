# 安装scrapy和pymongo
import subprocess

# Todo: 可使用freeze在本目录下来备份package列表以防安装失败或做还原用

install_list = ['scrapy', 'pymongo']
for x in install_list:
    tempcmd = "pip3 install -U " + x  # install or upadte to the latest version using pip3
    print(subprocess.Popen(tempcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           shell=True).stdout.readlines())

# Scrapy主体

# Todo: 在进入当前目录之后，使用shell创建Scrapy工程
# import scrapy

# Todo: 设置数据模板（每条的数据格式）
#  如何分析每条数据格式并运用到其他网站数据挖掘中去

# Todo: 爬虫主类

# Todo: 设置配置文件

# Todo: 抓取后数据的后续处理

# Todo: 执行爬虫程序
