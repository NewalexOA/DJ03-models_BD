# news/models.py
from django.db import models

class News_post(models.Model):
    title = models.CharField('Заголовок новости', max_length=100)
    short_description = models.CharField('Краткое описание', max_length=400)
    content = models.TextField('Текст новости')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    creator = models.CharField('Автор', max_length=100)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
