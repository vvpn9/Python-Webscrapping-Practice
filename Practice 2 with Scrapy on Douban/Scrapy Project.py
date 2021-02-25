# 安装scrapy和pymongo
# 基于macos

import os

# Todo: 安装必须模组，有则可以略过
# install_list = ['scrapy', 'pymongo']
# for x in install_list:
#     tempcmd = "pip3 install -U " + x  # install or upadte to the latest version using pip3
#     print(subprocess.Popen(tempcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                            shell=True).stdout.readlines())

# Todo: 在进入当前目录之后，使用shell创建Scrapy项目

# 创建项目
os.system('scrapy startproject douban')

# 切换目录
os.chdir('douban/douban/spiders')  # 此处切换工作路径，否则仍旧为脚本当前路径

# 创建爬虫
os.system('scrapy genspider doubanmovie movie.douban.com')

# 在cfg同级目录下创建测试脚本
os.chdir('../..')
os.system('pwd')
run_code = 'from scrapy import cmdline\n\ncmdline.execute("scrapy crawl doubanmovie".split())\n'
with open('run.py', 'w') as f:
    f.writelines(run_code)

# 修改setting文件
os.chdir('douban')
os.system('pwd')

with open('settings.py', 'r') as f:
    settings = f.readlines()

settings[19] = 'ROBOTSTXT_OBEY = False\n'  # 改变robot.txt的设置

settings.insert(43, 'COOKIES_ENABLED = False\n')  # 取消模拟登陆

# 伪造User Agent List
with open('settings.py', 'w') as f:
    f.writelines(settings)

# 修改items.py文件，定义获取信息的种类，可后续按照格式添加
items = ['import scrapy\n', '\n', '\n',
         'class DoubanItem(scrapy.Item):\n',
         '    title = scrapy.Field()\n',  # 电影标题
         '    bd = scrapy.Field()\n',  # 电影信息
         '    star = scrapy.Field()\n',  # 电影评分
         '    quote = scrapy.Field()\n']  # 电影名言

# 写入items
with open('items.py', 'w') as f:  # 重新写入items.py
    f.writelines(items)

# 获取所需爬取字段的Xpath
'''
此处使用Xpath Helper
观察所需要参数的位置，获取目标尾段，再反向测试

电影标题：.//span[@class='title'][1]
电影信息：.//div[@class='bd']/p[1]
电影评分：.//div[@class='star']/span[@class='rating_num']
电影名言：.//span[@class='inq']
'''

# 分析每页链接地址
'''
第一页：https://movie.douban.com/top250?start=0&filter=
第二页：https://movie.douban.com/top250?start=25&filter=
第三页：https://movie.douban.com/top250?start=50&filter=
第四页：https://movie.douban.com/top250?start=75&filter=
'''

# 编写spider目录下doubanmovide.py
os.chdir('spiders')

spiderbody = ['import os\n',
              'import sys\n',
              '\n',
              'import scrapy\n',
              '\n',
              'path = os.path.dirname(os.path.dirname(os.path.dirname('
              'os.path.abspath(__file__))))\n',
              'sys.path.append(path)\n',
              'from douban.items import DoubanItem\n',  # 从编写的items.py中导入类型
              '\n',
              '\n',

              # 创建class类型

              'class DoubamovieSpider(scrapy.Spider):\n',
              '    name = "doubanmovie"\n',
              '    allowed_domains = ["movie.douban.com"]\n',
              '    offset = 0\n',
              '    url = "https://movie.douban.com/top250?start=0&filter="\n',
              '    start_urls = (url + str(offset),)\n',
              '\n',
              '    def parse(self, response):\n',
              '        item = DoubanItem()\n',

              # 此处填写豆瓣电影，用三个引号为保证输出结果格式正确
              r'''        movies = response.xpath(".//div[@class='info']")''',
              '\n',
              '        for each in movies:\n',

              # extract()返回的是一个列表，列表里的每个元素是一个对象
              # extract()把这些对象转换成 Unicode 字符串

              # 电影标题
              r'''            item['title'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]''',
              '\n',

              # 电影信息
              r'''            item['bd'] = each.xpath(".//div[@class='bd']/p[1]/text()").extract()[0]''',
              '\n',

              # 电影评分
              r'''            item['star'] = each.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]''',
              '\n',

              # 电影名言，尾部处理和前三条信息不同
              r'''            quote = each.xpath(".//span[@class='inq']/text()").extract()''',
              '\n',

              '            if len(quote) != 0:\n',
              '                item["quote"] = quote[0]\n',
              '            yield item\n',

              '\n'

              '        if self.offset < 225:\n',
              '            self.offset += 25\n',
              '            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)'
              '\n'
              ]

with open('spiders.py', 'w') as f:
    f.writelines(spiderbody)

# 在setting中设置管道文件
os.chdir('../')

with open('settings.py', 'r') as f:
    settings = f.readlines()

del settings[65:68]  # 删除原有注释

settings.insert(65, "ITEM_PIPELINES = {'douban.pipelines.DoubanPipeline': 300, }\n")

with open('settings.py', 'w') as f:
    f.writelines(settings)

# 创建MongoDB数据库

    # Todo: 设置配置文件

    # Todo: 抓取后数据的后续处理

    # Todo: 执行爬虫程序
