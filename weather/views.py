from rest_framework.generics import ListAPIView

from weather.models import Weather
from weather.serializers import WeatherSeriliazer


class ListWeatherView(ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSeriliazer
