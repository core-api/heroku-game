from rest_framework import serializers


class PlayTurnSerializer(serializers.Serializer):
    position = serializers.CharField(max_length=100, required=True)

    def validate_position(self, data):
        data = data.lower()
        if not len(data) == 2:
            raise serializers.ValidationError("Position should be in form [abc][123].")

        if data[0] not in ('a', 'b', 'c'):
            raise serializers.ValidationError("Position row should be one of [a|b|c].")

        if data[1] not in ('1', '2', '3'):
            raise serializers.ValidationError("Position row should be one of [1|2|3].")

        if self.instance.get_position(data) != '.':
            raise serializers.ValidationError("You have already played here.")

        return data
