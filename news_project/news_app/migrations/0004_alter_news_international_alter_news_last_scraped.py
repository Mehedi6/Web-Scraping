# Generated by Django 4.2.16 on 2024-10-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_alter_news_image_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='international',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='last_scraped',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
