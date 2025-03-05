from celery import shared_task
from django.utils import timezone
from dateutil.relativedelta import *

from routine.models import Routine
from routine.services import send_telegram_message


@shared_task
def routine_reminder_send_to_tg():
    """Метод, описывающий периодическую задачу для отправки напоминаний о необходимости выполнить Привычки"""
    today = timezone.now().today().date()
    routines = Routine.objects.filter(enjoyable=False)
    for routine in routines:
        message = (f'Вам необходимо выполнить: что: {routine.what} где: {routine.where} когда: {routine.where}, время '
                   f'выполнения {routine.time_to_complete} сек. После этого вас ждет вознаграждение: ')
        if routine.reward:
            message += routine.reward
        elif routine.reward_routine:
            message += f' приятная привычка: {routine.reward_routine} '

        routine_owner = routine.owner
        if routine_owner:
            if routine.reminder:
                if routine_owner.tg_id:
                    if routine.last_reminder is None or routine.last_reminder + relativedelta(
                            days=+routine.period) == today:
                        send_telegram_message(routine_owner.tg_id, message)
                        routine.last_reminder = today
                        routine.save()


@shared_task
def test():
    """Тестовая задача для celery"""
    print("Test is completed")
