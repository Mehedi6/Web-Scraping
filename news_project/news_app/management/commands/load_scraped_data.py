import json
from datetime import datetime
from django.core.management.base import BaseCommand
from news_app.models import News

class Command(BaseCommand):
    help = 'Load scraped data into the News model'

    def handle(self, *args, **kwargs):
        # Load scraped data from JSON
        json_file_path = 'F:/Intern/news_project/news_scraper/news_scraper/spiders/business_data.json'

        # Load the scraped data from the specified file path
        with open(json_file_path, 'r', encoding='utf-8') as file:
            articles = json.load(file)

        for article in articles:
            news = News(
                url=article['url'],
                title=article['title'],
                meta_description=article['meta_description'],
                news_type=article['news_type'],
                media_type=article['media_type'],
                image_urls=article['image_urls'],
                published_date=article['published_date'] if article['published_date'] else None,
                updated_date=article['updated_date'] if article['updated_date'] else None,
                keywords=article.get('keywords', ''),
                source=article['source'],
                last_scraped=datetime.fromisoformat(article['last_scraped']),
                author=article.get('author', 'Unknown'),
                content=article['content'],
            )
            news.save()
