from django.db import models

from config import settings


class Routine(models.Model):
    """Класс, описывающий модель Привычка"""
    what = models.CharField(
        max_length=150,
        verbose_name="Что именно необходимо выполнить",
        help_text="",
        blank=True,
        null=True
    )
    when = models.TimeField(
        blank=True,
        null=True,
        verbose_name="Время, когда необходимо выполнять привычку",
        help_text="формат H:M"
    )
    where = models.CharField(
        max_length=150,
        verbose_name="Место, где необходимо выполнять привычку",
        help_text="",
        blank=True,
        null=True
    )
    enjoyable = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Признак приятной привычки ",
        help_text=""
    )
    reward = models.TextField(
        verbose_name="Вознаграждение",
        help_text="",
        blank=True,
        null=True
    )
    reward_routine = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Приятная привычка",
        help_text=""
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        help_text=""
    )
    period = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="периодичность выполнения привычки в днях",
        help_text="по умолчанию ежедневно, но не менее 1 раза в 7 дней",
        blank=True,
        null=True
    )
    time_to_complete = models.PositiveSmallIntegerField(
        verbose_name="время на выполнение привычки в секундах",
        help_text="не больше 120 секунд",
        blank=True,
        null=True
    )
    reminder = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Включить напоминания",
        help_text=""
    )
    last_reminder = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего напоминания",
        help_text=""
    )
    is_public = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Признак публичности привычки",
        help_text=""
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        """строковое представление Привычки"""
        return f'{self.what} {self.when} {self.where}'
