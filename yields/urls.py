from django.urls import path

from  .views import ListCropView


urlpatterns = [
    path("yield", ListCropView.as_view(), name="list_crop"),
]
