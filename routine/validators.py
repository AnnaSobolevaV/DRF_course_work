from rest_framework import serializers


def routine_period_validator(value):
    """Метод валидации поля period модели Привычка"""
    if not (value in range(1, 8)):
        raise serializers.ValidationError("Частота выполнения привычки не может быть менее 1 раза в 7 дней")


def routine_time_to_complete_validator(value):
    """Метод валидации поля time_to_complete модели Привычка"""
    if not (value in range(1, 121)):
        raise serializers.ValidationError("Время выполнения не может быть меньше 1 секунды и больше 120 секунд")
