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


class GeometrySerializer(serializers.Serializer):
    type = serializers.CharField(default="Point")
    coordinates = serializers.ListField(
        child=serializers.FloatField(),
        min_length=2,
        max_length=2,
        help_text="Format: [longitude, latitude]"
    )

class PropertiesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    status = serializers.CharField()

class GeoJSONFeatureSerializer(serializers.Serializer):
    type = serializers.CharField(default="Feature")
    geometry = GeometrySerializer()
    properties = PropertiesSerializer()

class FeatureCollectionSerializer(serializers.Serializer):
    type = serializers.CharField(default="FeatureCollection")
    features = GeoJSONFeatureSerializer(many=True)
