from django.db import models


class Queries(models.Model):
    fio = models.CharField('ФИО', max_length=50)
    phone_number = models.CharField('Номер телефона', default='+375', max_length=13)
    type_of_learning = models.BooleanField('Тип занятия(галочка если оффлайн)', default=True)
    physics_learn = models.BooleanField('Занятия по физике', default=False)
    math_learn = models.BooleanField('Занятие по математике', default=False)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

