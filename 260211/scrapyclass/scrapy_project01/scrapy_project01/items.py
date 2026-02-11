import scrapy


class ScrapyProject01Item(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()