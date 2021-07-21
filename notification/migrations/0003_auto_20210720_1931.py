# Generated by Django 3.2.4 on 2021-07-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_notification_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='target_id',
            new_name='target',
        ),
        migrations.AlterField(
            model_name='notification',
            name='type_of',
            field=models.CharField(choices=[('Модератор', 'Модератор'), ('Like', 'Like'), ('Dislike', 'Dislike'), ('Новый комментарий', 'Новый комментарий'), ('Снято с публикации', 'Снято с публикации'), ('Комментарий удален', 'Комментарий удален'), ('Статья опубликована', 'Статья опубликована'), ('Cтатья восстановлена', 'Статья восстановлена'), ('Лайк на коммент', 'Лайк на коммент'), ('Дизлайк на коммент', 'Дизлайк на коммент'), ('Ответ на коммент', 'Ответ на коммент')], max_length=50, verbose_name='тип'),
        ),
    ]
