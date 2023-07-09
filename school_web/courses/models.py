from django.db import models


class Queries(models.Model):
    fio = models.CharField('ФИО', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=13)
    type_of_learning = models.BooleanField(default=True)
    sr_mark = models.FloatField('Средний балл')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
