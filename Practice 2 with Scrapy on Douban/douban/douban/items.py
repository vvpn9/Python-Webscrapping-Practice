import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    bd = scrapy.Field()
    star = scrapy.Field()
    quote = scrapy.Field()
