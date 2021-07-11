# Generated by Django 2.2 on 2021-07-11 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_delete_commentslike'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsLike',
            fields=[
                ('like_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='article.Like')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Comment')),
            ],
            bases=('article.like',),
        ),
    ]
