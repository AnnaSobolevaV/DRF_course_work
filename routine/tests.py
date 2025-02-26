from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from routine.models import Routine
from users.models import User


class RoutineTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="autotest@mail.ru")
        self.routine = Routine.objects.create(what="autoTestRoutine", owner=self.user)
        self.reward_routine = Routine.objects.create(what="autoTestRewardRoutine", enjoyable=True, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_routine_list(self):
        url = reverse("routine:routine-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'count': 2, 'next': None, 'previous': None,
                                           'results': [{'id': self.routine.pk, 'period': 1, 'time_to_complete': None,
                                                        'what': 'autoTestRoutine', 'when': None, 'where': None,
                                                        'enjoyable': None, 'reward': None, 'reminder': None,
                                                        'last_reminder': None, 'is_public': None,
                                                        'reward_routine': None, 'owner': self.user.pk},
                                                       {'id': self.reward_routine.pk, 'period': 1,
                                                        'time_to_complete': None,
                                                        'what': 'autoTestRewardRoutine', 'when': None, 'where': None,
                                                        'enjoyable': True, 'reward': None, 'reminder': None,
                                                        'last_reminder': None, 'is_public': None,
                                                        'reward_routine': None, 'owner': self.user.pk}]})
        self.assertEqual(Routine.objects.count(), 2)

    def test_routine_retrieve(self):
        url = reverse("routine:routine-detail", args=(self.routine.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id': self.routine.pk, 'period': 1, 'time_to_complete': None,
                                           'what': 'autoTestRoutine', 'when': None, 'where': None,
                                           'enjoyable': None, 'reward': None, 'reminder': None,
                                           'last_reminder': None, 'is_public': None,
                                           'reward_routine': None, 'owner': self.user.pk})

    def test_routine_create(self):
        url = reverse("routine:routine-create")
        data = {"what": "autoTestNew", "owner": self.user.pk}
        response = self.client.post(url, data)
        print("response", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['what'], 'autoTestNew')
        self.assertEqual(Routine.objects.count(), 3)

    def test_routine_update(self):
        url = reverse("routine:routine-detail", args=(self.routine.pk,))
        data = {"what": "autoTestUpdate"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id': self.routine.pk, 'period': 1, 'time_to_complete': None,
                                           'what': 'autoTestUpdate', 'when': None, 'where': None,
                                           'enjoyable': None, 'reward': None, 'reminder': None,
                                           'last_reminder': None, 'is_public': None,
                                           'reward_routine': None, 'owner': self.user.pk})

    def test_routine_delete(self):
        url = reverse("routine:routine-detail", args=(self.routine.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Routine.objects.count(), 1)
