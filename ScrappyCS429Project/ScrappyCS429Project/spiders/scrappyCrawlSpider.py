import scrapy  # type: ignore
from scrapy.spiders import CrawlSpider, Rule # type: ignore
from scrapy.linkextractors import LinkExtractor  # type: ignore

class MySpider(CrawlSpider):
    name = 'myspider'

    def __init__(self, url=None, max_pages=None, max_depth=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [url] if url else []
        self.max_pages = int(max_pages) if max_pages else None
        self.max_depth = int(max_depth) if max_depth else None

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("URL:", response.url)
        print("HTML Content:", response.text)

        if self.max_depth is None or response.meta.get('depth', 0) < self.max_depth:
            if self.max_pages is None or response.meta.get('page_count', 0) < self.max_pages:
                for link in LinkExtractor(allow=()).extract_links(response):
                    yield scrapy.Request(url=link.url, callback=self.parse, meta={'depth': response.meta.get('depth', 0) + 1, 'page_count': response.meta.get('page_count', 0) + 1})


# Example usage in terminal:
# scrapy crawl myspider -a url=https://example.com -a max_pages=1 -a max_depth=1