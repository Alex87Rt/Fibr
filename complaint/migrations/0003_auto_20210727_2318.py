# Generated by Django 3.2.4 on 2021-07-27 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('complaint', '0002_auto_20210727_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='owner',
        ),
        migrations.AddField(
            model_name='complaint',
            name='owner',
            field=models.ForeignKey(default=21, on_delete=django.db.models.deletion.CASCADE, related_name='usercomplaint', to='authapp.user'),
            preserve_default=False,
        ),
    ]