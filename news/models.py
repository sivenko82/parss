from django.db import models


class Artik(models.Model):
    title=models.CharField('НАзвание',max_length=50)
    anons=models.CharField('Анонс',max_length=250)
    full=models.TextField('Текст ')
    date=models.DateField('дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='новости'



