import scrapy


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanMovie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    def parse(self, response):
        pass
