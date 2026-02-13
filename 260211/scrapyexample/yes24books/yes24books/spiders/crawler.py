import scrapy
from yes24books.items import Yes24BooksItem

class CrawlerSpider(scrapy.Spider):
    name = "crawler"
    allowed_domains = ["yes24.com"]
    start_urls = ["https://www.yes24.com/product/category/steadyseller?pageNumber=1&pageSize=24&categoryNumber=001001025007"]

    def parse(self, response):
        books = response.css("ul#yesBestList > li")

        for i, book in enumerate(books[:11], 1) :
            title = book.css("div.info_row.info_name a.gd_name::text").get()
            link = book.css("div.info_row.info_name a.gd_name::attr(href)").get()

            item = Yes24BooksItem()
            item["rank"] = i
            item["title"] = title
            item["url"] = response.urljoin(link)

            yield item


