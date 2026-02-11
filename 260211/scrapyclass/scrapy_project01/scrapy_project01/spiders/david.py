import scrapy
from scrapy_project01.items import ScrapyProject01Item


class DavidSpider(scrapy.Spider):
    name = "david"
    allowed_domains = ["davelee-fun.github.io"]
    start_urls = ["https://davelee-fun.github.io"]

    def parse(self, response):
        item = ScrapyProject01Item()
        item["title"] = response.css("h1.sitetitle::text").get()
        item["description"] = response.xpath('//p[@class="lead"]/text()').get().strip()
        yield item
