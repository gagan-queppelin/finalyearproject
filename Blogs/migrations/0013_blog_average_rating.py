# Generated by Django 3.2.5 on 2021-07-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0012_auto_20210718_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
    ]
