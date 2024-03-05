from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Subject

NULLABLE = {'null':True, 'blank':True}

'''
Пользователь: все поля от обычного пользователя, 
но авторизацию заменить на email; телефон; город; аватарка. 
Модель пользователя разместите в приложении users'''
class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)

    email_verify = models.BooleanField(default=False, verbose_name='проверка почты')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} - {self.phone}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

"""
Задание 2
Добавьте новую модель в приложение users:

Платежи

пользователь,
дата оплаты,
оплаченный курс или урок,
сумма оплаты,
способ оплаты: наличные или перевод на счет.
Поля 
пользователь
, 
оплаченный курс
 и 
отдельно оплаченный урок
 должны быть ссылками на соответствующие модели.

Запишите в таблицу, соответствующую этой модели данные через инструмент фикстур или кастомную команду."""

class Payment(models.Model):
    CASH = 'Наличные'
    ACCOUNT = 'Перевод на счет'


    STATUS_CHOICES = [
        (CASH, "Наличные"),
        (ACCOUNT, "Перевод на счет"),
    ]


    user_pay = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="платежеспособный пользователь", **NULLABLE)
    date_pay = models.DateField(auto_now=False, verbose_name="дата оплаты", **NULLABLE)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="оплаченный курс", **NULLABLE)
    paid_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="оплаченный курс", **NULLABLE)
    payment = models.PositiveIntegerField(verbose_name="сумма оплаты")
    payment_method = models.CharField(max_length=85, choices=STATUS_CHOICES, verbose_name="Способ оплаты", **NULLABLE)

    def __str__(self):
        return f'{self.user_pay} {self.payment} {self.date_pay}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ['-date_pay',]
