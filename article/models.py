from django.db import models
from authapp.models import User
from hub.models import Topic


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Раздел')
    title = models.CharField(max_length=64, unique=True, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Статья')
    image = models.ImageField(upload_to='article_images', blank=True, verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    @staticmethod
    def get_user_articles(user):
        return Article.objects.filter(user=user)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)

