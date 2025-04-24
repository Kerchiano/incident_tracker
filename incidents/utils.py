def build_geojson_features(incidents):
    return [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [incident.longitude, incident.latitude],
            },
            "properties": {
                "id": incident.id,
                "title": incident.title,
                "status": incident.status,
            },
        }
        for incident in incidents
    ]