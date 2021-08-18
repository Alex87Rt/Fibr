# Generated by Django 3.2.4 on 2021-07-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('На рассмотрении', 'На рассмотрении'), ('Принята', 'Принята'), ('Отклонена', 'Отклонена')], db_index=True, default='На рассмотрении', max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
