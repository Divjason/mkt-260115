import scrapy

class ScrapyProject07Item(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    category = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()
