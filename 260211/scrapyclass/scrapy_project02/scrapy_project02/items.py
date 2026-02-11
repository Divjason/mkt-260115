import scrapy

class ScrapyProject02Item(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()