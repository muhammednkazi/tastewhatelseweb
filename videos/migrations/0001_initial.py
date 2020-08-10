# Generated by Django 3.0.6 on 2020-07-08 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('desc', models.TextField(default='', max_length=300)),
                ('pub_date', models.DateTimeField()),
                ('thumbnail', models.ImageField(default='', upload_to='images')),
            ],
        ),
    ]