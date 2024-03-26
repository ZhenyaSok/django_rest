from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Subject, Subscribe, Course
from users.models import User


class SubjectTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@ya.ru')

        self.course = Course.objects.create(
            title='test',
        )
        self.subject = Subject.objects.create(
            title='Грамматика',

        )
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
        response = self.client.get('/lms/subject/1/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_subject(self):
        """Тест редактирования урока"""
        data = {
            "title": "Test_new",
        }

        response = self.client.put(
            '/lms/subject/update/1/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_subject(self):
        """Тест удаления урока"""
        response = self.client.delete(
            '/lms/subject/delete/1/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_subscribe(self):
        """Тест создания подписки"""
        data = {
            "course_id": 1
        }
        response = self.client.post(
            '/lms/subscription/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )