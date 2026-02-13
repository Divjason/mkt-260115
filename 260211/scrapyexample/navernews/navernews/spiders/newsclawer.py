import scrapy
from urllib.parse import urlencode
from navernews.items import NavernewsItem

class NewsclawerSpider(scrapy.Spider):
    name = "newsclawer"
    allowed_domains = ["search.naver.com"]
    start_urls = ["https://search.naver.com"]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
    }

    def __init__(self, query="디지털 마케팅"):
        self.query = query

    def start_requests(self):
        base = "https://search.naver.com/search.naver"
        params = {"where": "news", "query": self.query}
        url = f"{base}?{urlencode(params)}"

        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        nodes = response.css("a.fender-ui_228e3bd1.qWflZiHeQFq9pBzWximH")

        for i, node in enumerate(nodes, 1) :
            title = node.css("::text").get().strip()
            link = node.attrib.get("href", "")

            item = NavernewsItem()
            item["rank"] = i
            item["query"] = self.query
            item["title"] = title
            item["url"] = link

            yield item