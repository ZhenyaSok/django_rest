from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Subject, Subscribe, Course
from users.models import User


class SubjectTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@ya.ru')
        self.course = Course.objects.create(title='test')
        self.subject = Subject.objects.create(title='Грамматика')
        self.client.force_authenticate(user=self.user)


    # moder_group = Group.objects.get_or_create(name='Модератор')
    # self.user.groups.add(moder_group)

    def test_get_list(self):
        """Тест просмотра списка уроков (list)"""

        response = self.client.get('/lms/subject/list/')

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_create_subject(self):
        """Тест создания урока (create)"""
        data = {
            'title': 'Test',
        }

        response = self.client.post('/lms/subject/create/', data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


    def test_get_subject(self):
        """Тест просмотра урока (retrieve)"""
        response = self.client.get(reverse('lms:subject_get', args=[self.subject.id]))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_subject(self):
        """Тест редактирования урока"""
        data = {
            "title": "Test_new",
            "description": "Test_description"
        }

        response = self.client.patch(
            reverse('lms:subject_update', args=[self.subject.id]), data
        )

        self.subject.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], data['description'])

    def test_delete_subject(self):
        """Тест удаления урока"""
        response = self.client.delete(
            reverse('lms:subject_delete', args=[self.subject.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


    # def test_create_subscribe(self):
    #     """Тест создания подписки"""
    #     self.subscribe = Subscribe.objects.create(
    #
    #         course=self.course.id
    #     )
    #     response = self.client.post(reverse('lms:subscription'))
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     # self.assertEqual(response.data['message'], 'подписка удалена')