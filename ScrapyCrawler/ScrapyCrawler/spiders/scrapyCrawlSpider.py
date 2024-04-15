import scrapy # type: ignore
import os
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
            
    def clean_title(self, title):
        cleaned_title = ''.join(char for char in title if char.isalnum() or char in ' -')
        cleaned_title = cleaned_title.strip()
        cleaned_title = cleaned_title.replace(' ', '-')
        cleaned_title = cleaned_title.replace('--', '-')      
        cleaned_title = cleaned_title.lower()
        return cleaned_title

    def parse(self, response):
        html_content = response.body.decode('utf-8')
        
        title = response.css('title::text').get()
        if title:
            title = title.strip()
        else:
            title = 'Untitled'
            
        clean_title = self.clean_title(title)

        filename = f"../CrawledDocuments/{clean_title}.html"

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        self.crawled_count += 1

        if self.crawled_count < self.max_pages and response.meta['depth'] < self.max_depth:
            for link in response.css('a::attr(href)').getall():
                yield response.follow(link, callback=self.parse)