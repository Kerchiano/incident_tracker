from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Incident
from .serializers import IncidentSerializer

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    @action(detail=False, methods=['get'], url_path='map')
    def get_geojson(self, request):
        incidents = self.queryset.filter(status='active')
        features = [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [incident.longitude, incident.latitude],
                },
                "properties": {
                    "id": incident.id,
                    "title": incident.title,
                    "status": incident.status
                }
            }
            for incident in incidents
        ]
        return Response({
            "type": "FeatureCollection",
            "features": features
        })
