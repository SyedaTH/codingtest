from rest_framework.generics import ListAPIView


from yields.models import YieldsData
from yields.serializers import YieldsSerializer


class ListCropView(ListAPIView):
    queryset = YieldsData.objects.all()
    serializer_class = YieldsSerializer
