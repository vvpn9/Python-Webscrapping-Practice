import os
import sys

import scrapy

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)
from douban.items import DoubanItem


class DoubamovieSpider(scrapy.Spider):
    name = "doubanmovie"
    allowed_domains = ["movie.douban.com"]
    offset = 0
    url = "https://movie.douban.com/top250?start=0&filter="
    start_urls = (url + str(offset),)

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath(".//div[@class='info']")
        for each in movies:
            item['title'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            item['bd'] = each.xpath(".//div[@class='bd']/p[1]/text()").extract()[0]
            item['star'] = \
            each.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            quote = each.xpath(".//span[@class='inq']/text()").extract()
            if len(quote) != 0:
                item["quote"] = quote[0]
            yield item

        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
