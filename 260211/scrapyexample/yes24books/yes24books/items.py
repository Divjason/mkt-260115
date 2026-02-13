import scrapy

class Yes24BooksItem(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
