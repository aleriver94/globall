# Generated by Django 3.0 on 2021-12-15 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
    ]
