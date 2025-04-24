from rest_framework import serializers
from .models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(
        choices=[('active', 'Active'), ('closed', 'Closed')],
        error_messages={
            "invalid_choice": "Status must be either 'active' or 'closed'."
        }
    )

    class Meta:
        model = Incident
        fields = '__all__'

    def validate_latitude(self, value):
        if not -90 <= value <= 90:
            raise serializers.ValidationError("Latitude must be between -90 and 90 degrees.")
        return value

    def validate_longitude(self, value):
        if not -180 <= value <= 180:
            raise serializers.ValidationError("Longitude must be between -180 and 180 degrees.")
        return value
