from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from routine.models import Routine
from routine.validators import routine_period_validator, routine_time_to_complete_validator


class RoutineSerializer(ModelSerializer):
    period = serializers.IntegerField(validators=[routine_period_validator], required=False)
    time_to_complete = serializers.IntegerField(validators=[routine_time_to_complete_validator], required=False)

    def validate(self, attrs):
        errors = []
        obj = self.instance
        if obj:
            if "reward_routine" not in attrs.keys():
                attrs["reward_routine"] = obj.reward_routine
            reward = dict(attrs).get('reward', obj.reward)
            enjoyable = dict(attrs).get('enjoyable', obj.enjoyable)
        else:
            if "reward_routine" not in attrs.keys():
                attrs["reward_routine"] = None
            reward = dict(attrs).get('reward', None)
            enjoyable = dict(attrs).get('enjoyable', None)
        reward_routine = attrs["reward_routine"]
        if reward_routine:
            # if reward_routine.enjoyable is not None:
            if not reward_routine.enjoyable:
                errors.append("В связанной привычке может быть только приятная привычка")
        if enjoyable and (reward or reward_routine):
            errors.append("В приятной привычке не может быть вознаграждения или связанной привычки")

        if reward and reward_routine:
            errors.append("В привычке не может быть одновременно вознаграждение и связанная привычка")

        if errors:
            raise serializers.ValidationError(errors)

        return attrs

    class Meta:
        model = Routine
        fields = "__all__"
        validators = []
