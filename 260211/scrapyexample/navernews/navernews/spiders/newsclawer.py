import scrapy


class NewsclawerSpider(scrapy.Spider):
    name = "newsclawer"
    allowed_domains = ["search.naver.com"]
    start_urls = ["https://search.naver.com"]

    def parse(self, response):
        pass
