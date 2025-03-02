from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Класс для описания команды csu. Создание пользователя - superuser"""

    def handle(self, *args, **options):
        """"""
        user = User.objects.create(
            email='admin_DRF@sky.pro',
            first_name='Admin',
            last_name='cursDRF',
            is_staff=True,
            is_active=True,
            is_superuser=True
        )

        user.set_password('superuser_pass')
        user.save()
