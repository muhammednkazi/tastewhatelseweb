# Generated by Django 3.0.6 on 2020-07-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20200712_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='video',
            name='content',
            field=models.TextField(default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(default='', max_length=150),
        ),
    ]
