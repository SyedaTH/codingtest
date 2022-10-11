from rest_framework import serializers

from weather.models import Weather


class WeatherSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = [
            "station_id",
            "date",
            "max_temp",
            "min_temp",
            "precipitation",
            "created_timestamp",
            "updated_timestamp",
        ]
