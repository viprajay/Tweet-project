# Generated by Django 5.1.1 on 2024-09-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_tweet_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
