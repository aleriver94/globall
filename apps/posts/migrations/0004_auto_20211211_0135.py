# Generated by Django 3.0 on 2021-12-11 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.TextField(max_length=300, null=True),
        ),
    ]