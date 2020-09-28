from django.db import models


class Contact(models.Model):
    last_name = models.CharField(max_length=254, verbose_name='Фамилия')
    first_name = models.CharField(max_length=254, verbose_name='Имя')
    patronymic = models.CharField(max_length=254, null=True, blank=True, verbose_name='Отчество')
    deck = models.TextField(max_length=5000, default='Я просто очень хороший человек.', verbose_name='Описание')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    phone = models.CharField(max_length=254, verbose_name='Номер телефона')
    email = models.EmailField(max_length=254, null=True, blank=True, verbose_name='Email')
    social_page_networks = models.CharField(max_length=254, null=True, blank=True, verbose_name='Страница в соц. сети')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
