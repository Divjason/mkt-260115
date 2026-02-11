import scrapy
from scrapy_project02.items import ScrapyProject02Item

class DavidSpider(scrapy.Spider):
    name = "david"
    allowed_domains = ["davelee-fun.github.io"]
    start_urls = ["https://davelee-fun.github.io"]

    def parse(self, response):
        item = ScrapyProject02Item()
        item["title"] = response.css("h1.sitetitle::text").get()
        item["description"] = response.xpath('//p[@class="lead"]/text()').get()
        yield item