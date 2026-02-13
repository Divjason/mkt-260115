from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class CleanValidatePipeline:
    def process_item(self, item, spider):
        a = ItemAdapter(item)
        # title = item.get("title").strip()
        title = a.get("title").strip()
        url = a.get("url").strip()

        if not title :
            raise DropItem("Missing title")
        if not url :
            raise DropItem("Missing url")

        item["title"] = title
        item["url"] = url

        return item
