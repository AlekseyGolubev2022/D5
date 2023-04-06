from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=0)

    def update_rating(self):
        for_posts = sum(i['rating'] for i in self.posts.values('rating')) * 3
        for_comments = sum(i['rating'] for i in self.user.comments.values('rating'))
        author_posts = self.posts.values('rating')
        for_postcomments = sum(i['rating'] for i in (j for j in author_posts))
        self.rating = for_posts + for_comments + for_postcomments
# --------------------------------------79------------------------------------
        self.save()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(
        'Категория',
        max_length=100,
        help_text='Категория, к которой относится пост',
        unique=True
    )

    def __str__(self):
        return self.name[:30] + '...'

# --------------------------------------79------------------------------------
class Post(models.Model):
    NEWS = 'N'
    ARTICLE = 'A'
    GENRES = [(NEWS, 'новость'), (ARTICLE, 'статья')]

    title = models.CharField(
        'Заголовок', max_length=100, help_text='Заголовок публикации'
    )
    genre = models.CharField(max_length=1, choices=GENRES, default=NEWS)
    text = models.TextField(
        'Текст статьи/новости', help_text='Текст новой публикации')
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='posts'
    )
    categories = models.ManyToManyField(Category, through='PostCategory')

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title[:20] + '...'

    def preview(self):
        return self.title[:124] + '...'

    def like(self):
        """Упрощенный вариант (по заданию) без проверок и геттеров/сеттеров"""
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

# --------------------------------------79------------------------------------
class Comment(models.Model):
    """Список комментариев,
    именованная выборка Post.comments - фильтр id объектов по Посту,
    а выборка User.comments - фильтр объектов по Автору комментария"""
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        help_text='Комментируемый пост'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    text = models.TextField('Комментарий', help_text='Текст комментария')
    created = models.DateTimeField('Дата добавления', auto_now_add=True)
    rating = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:20] + '...'

    def like(self):
        """Упрощенный вариант (по заданию) без проверок и геттеров/сеттеров"""
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
