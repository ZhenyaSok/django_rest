from django.db import models

from config import settings


NULLABLE = {'null':True, 'blank':True}

'''
Курс: название, превью (картинка), описание. 
Урок: название, описание, превью (картинка), 
ссылка на видео. Урок и курс - это связанные между собой сущности. 
Уроки складываются в курс, в одном курсе может быть много уроков. 
Реализуйте связь между ними.'''


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название предмета')
    description = models.TextField(verbose_name='описание предмета', **NULLABLE)
    preview = models.ImageField(verbose_name='картинка', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='администратор')
    price = models.PositiveIntegerField(default=0, verbose_name="цена")

    # last_update = models.DateTimeField(verbose_name='последнее обновление', auto_now=True)

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name='название предмета')
    description = models.TextField(verbose_name='описание предмета', **NULLABLE)
    preview = models.ImageField(verbose_name='картинка', **NULLABLE)
    link = models.URLField(max_length=190, verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)


    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscribe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    status_subscribe = models.BooleanField(default=False, verbose_name='статус подписки', **NULLABLE)


    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

