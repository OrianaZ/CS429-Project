import scrapy
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class MySpider(scrapy.Spider):
    name = 'myspider'

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('url')]
        self.max_pages = int(kwargs.get('max_pages'))
        self.max_depth = int(kwargs.get('max_depth'))
        self.crawled_count = 0

        parsed_url = urlparse(self.start_urls[0])
        domain_parts = parsed_url.netloc.split('.')
        self.domain = '-'.join(domain_parts[:-1])
        self.path = parsed_url.path.replace('/', '_') if parsed_url.path else 'root'
        
        if not self.domain:
            self.domain = parsed_url.path.replace('/', '_') if parsed_url.path else 'root'

    def parse(self, response):
        html_content = response.body.decode('utf-8')

        filename = f"../CrawledDocuments/{self.domain}_pgs{self.max_pages}_dp{self.max_depth}_page-{self.crawled_count}.html"

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        self.crawled_count += 1

        if self.crawled_count < self.max_pages and response.meta['depth'] < self.max_depth:
            for link in response.css('a::attr(href)').getall():
                yield response.follow(link, callback=self.parse)



# Example usage in terminal:
# scrapy crawl myspider -a url=https://example.com -a max_pages=1 -a max_depth=1