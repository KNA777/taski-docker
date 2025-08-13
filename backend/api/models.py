from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField(verbose_name='Описание')
    completed = models.BooleanField(verbose_name='Завершен', default=False)

    def _str_(self):
        return self.title
