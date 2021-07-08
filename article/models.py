from django.db import models
from authapp.models import User
from hub.models import Topic


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Раздел')
    title = models.CharField(max_length=64, unique=True, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Статья')
    image = models.ImageField(upload_to='article_images', blank=True, verbose_name='Фото')
    is_active = models.BooleanField(default=True, verbose_name='Активна', db_index=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    @staticmethod
    def get_user_articles(user):
        return Article.objects.filter(user=user, is_active=True)

    @staticmethod
    def get_articles():
        return Article.objects.filter(is_active=True, is_published=True)

    def get_total_likes(self):
        """Возвращает количество лайков для текущей статьи"""
        likes = Like.objects.filter(article=self, is_liked=True)

        return len(likes)

    def get_total_dislikes(self):
        """Возвращает количество дизлайков для текущей статьи"""
        likes = Like.objects.filter(article=self, is_disliked=True)

        return len(likes)

    def set_like_state(self, user, like_action):
        """Создает запись лайка или меняет свойство is_liked для существующей"""
        like_object = Like.objects.filter(article=self, user=user)

        if like_object:
            like_object[0].switch_like(like_action)
            like_object[0].save()

        else:
            if like_action == 'like':
                Like.objects.create(article=self, user=user, is_liked=True)
            else:
                Like.objects.create(article=self, user=user, is_disliked=True)

    def leave_comment(self, user, text):
        """Создание нового комментария к статье"""
        Comment.objects.create(user=user, article=self, text=text)

    def toggle_publish(self):
        """Публикует/Снимает статью с публикации"""
        self.is_published = not self.is_published
        self.save()

    def toggle_hide(self):
        """Удаляет/восстанавливает статью"""
        self.is_active = not self.is_active
        self.save()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)
    is_disliked = models.BooleanField(default=False)

    @staticmethod
    def get_users_article_liked(article):
        likes = Like.objects.filter(article=article, is_liked=True)
        users = [like.user for like in likes]
        return users

    def switch_like(self, like_action):
        """Меняет статус лайка/дизлайка"""
        if like_action == 'like':
            if self.is_like_set:
                self.cancel_liked()
            else:
                self.set_like()

        else:
            if self.is_dislike_set:
                self.cancel_liked()
            else:
                self.set_dislike()

    def set_like(self):
        """Срабатывает при нажатии на кнопку 'like'"""
        self.is_liked = True
        self.is_disliked = False

    def set_dislike(self):
        """Срабатывает при нажатии на кнопку 'dislike'"""
        self.is_liked = False
        self.is_disliked = True

    def cancel_liked(self):
        self.is_liked = False
        self.is_disliked = False

    @property
    def is_like_set(self):
        return self.is_liked and not self.is_disliked

    @property
    def is_dislike_set(self):
        return not self.is_liked and self.is_disliked


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_author_name(self):
        author_name = self.user.get_full_name()
        return author_name

    @property
    def get_author_avatar(self):
        author_avatar = self.user.image
        return author_avatar
