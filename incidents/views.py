from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Incident
from .serializers import IncidentSerializer, FeatureCollectionSerializer
from .utils import build_geojson_features


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    @swagger_auto_schema(
        method='get',
        responses={200: FeatureCollectionSerializer()},
        operation_summary="Get active incidents in GeoJSON",
        operation_description="Returns active incidents in GeoJSON FeatureCollection format with geometry and custom properties"
    )
    @action(detail=False, methods=['get'], url_path='active')
    def get_geojson(self, request):
        incidents = self.queryset.filter(status='active')
        features = build_geojson_features(incidents)
        return Response({
            "type": "FeatureCollection",
            "features": features
        })
