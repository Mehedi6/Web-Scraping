import scrapy
from datetime import datetime
import re

class BusinessSpiderSpider(scrapy.Spider):
    name = "business_spider"
    allowed_domains = ["bangla.thedailystar.net"]
    start_urls = ["https://bangla.thedailystar.net/business"]

    def parse(self, response):
        article_links = response.css('a::attr(href)').getall()
        for link in article_links:
            if 'business' in link:
                if not link.startswith('http'):
                    link = response.urljoin(link)
                yield scrapy.Request(link, callback=self.parse_article)

    def parse_article(self, response): 
        content = response.css('div.pb-20.clearfix *::text').getall()
        
        
        yield {
            'url': response.url,
            'title': response.css('meta[property="og:title"]::attr(content)').get() or response.css('title::text').get(),
            'meta_description': response.css('meta[name="description"]::attr(content)').get(),
            'news_type': 'Business',
            'media_type': 'Online',
            'image_urls': response.css('meta[property="og:image"]::attr(content)').get(),
            'published_date': response.css('meta[property="article:published_time"]::attr(content)').get(),
            'updated_date': response.css('meta[property="article:modified_time"]::attr(content)').get(),
            'keywords': response.css('meta[name="keywords"]::attr(content)').get(),
            'source': 'The Daily Star',
            'last_scraped': datetime.now().isoformat(),
            'author': response.css('.author a::text').get(),
            'content': ''.join(content),

            'sentiment': '',
            'news_score': 0.0,
            'international': False,
        }
