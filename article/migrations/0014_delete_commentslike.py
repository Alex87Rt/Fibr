# Generated by Django 2.2 on 2021-07-11 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20210710_2119'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentsLike',
        ),
    ]
