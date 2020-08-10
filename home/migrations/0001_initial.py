# Generated by Django 3.0.6 on 2020-07-09 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus_table',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=13)),
                ('email', models.CharField(default='', max_length=100)),
                ('desc', models.TextField(default='', max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]