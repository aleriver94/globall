# Generated by Django 3.0 on 2021-12-11 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211211_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
