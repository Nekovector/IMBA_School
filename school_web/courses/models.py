from django.db import models


# Подготовка к ЦТ/ЦЭ
class Queries1(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    phone_number = models.CharField('Номер телефона', default='+375', max_length=13)
    type_of_learning = models.BooleanField('Онлайн обучение', default=False)
    physics_learn = models.BooleanField('Занятия по физике', default=False)
    math_learn = models.BooleanField('Занятие по математике', default=False)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    class Meta:
        verbose_name = 'Заявка (ЦТ/ЦЭ)'
        verbose_name_plural = 'Заявки (ЦТ/ЦЭ)'


# Подготовка к экзаменам после 9-го класса
class Queries2(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    phone_number = models.CharField('Номер телефона', default='+375', max_length=13)
    type_of_learning = models.BooleanField('Онлайн обучение', default=False)
    math_learn = models.BooleanField('Занятие по математике', default=False)


    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    class Meta:
        verbose_name = 'Заявка (После 9-го)'
        verbose_name_plural = 'Заявки (После 9-го)'

#ПОВЫШЕНИЕ УСПЕВАЕМОСТИ
class Queries3(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    phone_number = models.CharField('Номер телефона', default='+375', max_length=13)
    type_of_learning = models.BooleanField('Онлайн обучение', default=False)
    math_learn = models.BooleanField('Занятие по математике', default=False)
    physics_learn = models.BooleanField('Занятия по физике', default=False)
    grade_number = models.IntegerField('Номер класса ученика')

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    class Meta:
        verbose_name = 'Заявка (После 9-го)'
        verbose_name_plural = 'Заявки (После 9-го)'