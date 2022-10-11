from django.urls import path

from weather.views import ListWeatherView


urlpatterns = [
    path("weather", ListWeatherView.as_view(), name="list_weather"),
]
