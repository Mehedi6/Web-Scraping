import json
from django.core.management.base import BaseCommand
from transformers import pipeline
from news_app.models import News

class Command(BaseCommand):
    help = 'Analyze news articles and export to JSON'

    def handle(self, *args, **kwargs):
        
        sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        importance_analyzer = pipeline("text-classification", model="roberta-large-mnli")

        unprocessed_news = News.objects.filter(sentiment='', news_score=0.0)

       
        json_file_path = 'F:\\Intern\\news_project\\news_scraper\\news_scraper\\spiders\\business_data.json'

        try:
            with open(json_file_path, 'r', encoding='utf-8') as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            existing_data = []

        article_map = {article['url']: article for article in existing_data}

        for article in unprocessed_news:
            try:
            
                sentiment_result = sentiment_analyzer(article.content[:512])
                sentiment = sentiment_result[0]['label'] if sentiment_result else 'NEUTRAL'
                
            
                importance_result = importance_analyzer(article.content[:512])
                importance = importance_result[0]['score'] if importance_result else 0.0

                
                international_keywords = ["international", "world", "global", "foreign"]
                is_international = any(keyword in article.title.lower() for keyword in international_keywords) or any(
                    keyword in article.content.lower() for keyword in international_keywords
                )

            
                article.sentiment = sentiment
                article.news_score = importance * 100
                article.international = is_international
                
                if article.url in article_map:
                    article_map[article.url]['sentiment'] = sentiment
                    article_map[article.url]['news_score'] = importance * 100
                    article_map[article.url]['international'] = is_international

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing article {article.url}: {str(e)}'))

        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(list(article_map.values()), json_file, ensure_ascii=False, indent=4)

        self.stdout.write(self.style.SUCCESS(f'Successfully processed all news articles. Data exported to {json_file_path}.'))
