from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null':True, 'blank':True}

'''
Пользователь: все поля от обычного пользователя, 
но авторизацию заменить на email; телефон; город; аватарка. 
Модель пользователя разместите в приложении users'''
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)

    email_verify = models.BooleanField(default=False, verbose_name='проверка почты')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

