from django.db import models

# Create your models here.
class News(models.Model):
    url = models.URLField(max_length=2048, unique=True)
    title = models.CharField(max_length=255)
    meta_description = models.TextField(null=True, blank=True)
    news_type = models.CharField(max_length=20)
    news_subcategory = models.CharField(max_length=20)
    media_type = models.CharField(max_length=255)
    image_urls = models.TextField(null=True, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    keywords = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=255)
    last_scraped = models.DateTimeField(blank=True, null=True)
    international = models.BooleanField(blank=True, null=True)
    old = models.BooleanField(null=True, blank=True)
    sentiment = models.CharField(max_length=15)
    views = models.IntegerField(default=0)
    news_score = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)
    engagement = models.IntegerField(default=0)
    author = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    class Meta:
        db_table = 'news'
    def __str__(self):
        return self.title
