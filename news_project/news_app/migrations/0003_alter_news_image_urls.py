# Generated by Django 4.2.16 on 2024-10-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_alter_news_meta_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_urls',
            field=models.TextField(blank=True, null=True),
        ),
    ]