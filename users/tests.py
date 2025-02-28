
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Набор тестов для модели Пользователь"""
    def setUp(self):
        """Предустановки для тестов"""
        self.user = User.objects.create(email="autotest@mail.ru", is_active=True)
        self.client.force_authenticate(user=self.user)

    def test_user_list(self):
        """Проверка корректности вывода списка Пользователей"""
        url = reverse("users:user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        date_joined = self.user.date_joined.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        self.assertEqual(response.json(), [{'id': self.user.pk, 'password': '', 'last_login': None,
                                            'is_superuser': False, 'first_name': '', 'last_name': '',
                                            'is_staff': False, 'date_joined': date_joined,
                                            'email': 'autotest@mail.ru', 'phone': None, 'avatar': None,
                                            'city': None, 'token': None, 'tg_id': None, 'is_active': True,
                                            'groups': [], 'user_permissions': []}])
        self.assertEqual(User.objects.count(), 1)

    def test_user_retrieve(self):
        """Проверка корректности вывода одного Пользователя"""
        url = reverse("users:user-detail", args=(self.user.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        date_joined = self.user.date_joined.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        self.assertEqual(response.json(), {'id': self.user.pk, 'password': '', 'last_login': None,
                                           'is_superuser': False, 'first_name': '', 'last_name': '',
                                           'is_staff': False, 'date_joined': date_joined,
                                           'email': 'autotest@mail.ru', 'phone': None, 'avatar': None,
                                           'city': None, 'token': None, 'tg_id': None, 'is_active': True,
                                           'groups': [], 'user_permissions': []})

    def test_user_create(self):
        """Проверка корректного создания Пользователя"""
        url = reverse("users:register")
        data = {"email": "autotestNew@mail.ru", "password": "password", "is_active": "True"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'], 'autotestNew@mail.ru')
        self.assertEqual(User.objects.count(), 2)

    def test_user_update(self):
        """Проверка корректного изменения Пользователя"""
        url = reverse("users:user-detail", args=(self.user.pk,))
        data = {"email": "autotestUpdate@mail.ru"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'autotestUpdate@mail.ru')

    def test_user_delete(self):
        """Проверка корректного удаления Пользователя"""
        url = reverse("users:user-detail", args=(self.user.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
