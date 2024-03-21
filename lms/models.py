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
    subscribe_is_active = models.BooleanField(default=False, verbose_name='активность подписки')

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

'''
Задание 2
Добавьте модель подписки на обновления курса для пользователя.

Модель подписки должна содержать следующие поля: «пользователь» (
FK
 на модель пользователя), «курс» (
FK
 на модель курса). Можете дополнительно расширить модель при необходимости.

Вам необходимо реализовать эндпоинт для установки подписки пользователя и на удаление подписки у пользователя.'''

"""
Воспользуйтесь 
APIView
 и реализуйте логику метода 
post
, который будет отдавать ответ в зависимости от действия.

Пример кода метода 
post
 для управления подпиской:

def post(self, *args, **kwargs):
    user = получаем пользователя из self.requests
    course_id = получаем id курса из self.reqests.data
    course_item = получаем объект курса из базы с помощью get_object_or_404

    subs_item = получаем объекты подписок по текущему пользователю и курса

		# Если подписка у пользователя на этот курс есть - удаляем ее
    if subs_item.exists():
        ...
        message = 'подписка удалена'
		# Если подписки у пользователя на этот курс нет - создаем ее
    else:
        ...
        message = 'подписка добавлена'
		# Возвращаем ответ в API
    return Response({"message": message})

Зарегистрируйте новый контроллер в 
url
 и проверьте его работоспособность в Postman.
"""