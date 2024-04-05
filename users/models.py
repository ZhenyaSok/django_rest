from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Subject

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=50, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=75, verbose_name='Фамилия', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    is_active = models.BooleanField(default=False, **NULLABLE)
    last_login = models.DateTimeField(auto_now_add=True, verbose_name='время последнего посещения', **NULLABLE)

    email_verify = models.BooleanField(default=False, verbose_name='проверка почты')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} - {self.phone}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


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
    paid_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="оплаченный урок", **NULLABLE)
    payment_summ = models.PositiveIntegerField(verbose_name="сумма оплаты")
    payment_method = models.CharField(max_length=85, choices=STATUS_CHOICES, verbose_name="Способ оплаты", **NULLABLE)

    payment_link = models.URLField(max_length=700, verbose_name='ссылка для оплаты', **NULLABLE)
    payment_id = models.CharField(max_length=255, verbose_name='идентификатор платежа', **NULLABLE)

    def __str__(self):
        return f'{self.user_pay} {self.payment_summ} {self.date_pay}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ['-date_pay',]



