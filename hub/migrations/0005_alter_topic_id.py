# Generated by Django 3.2.4 on 2021-07-11 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0004_auto_20210703_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
