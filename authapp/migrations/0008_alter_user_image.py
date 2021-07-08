# Generated by Django 3.2.4 on 2021-07-07 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='users_avatars/default.jpg', upload_to='users_avatars'),
        ),
    ]
