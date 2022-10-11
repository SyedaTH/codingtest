from rest_framework import serializers

from yields.models import YieldsData


class YieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YieldsData
        fields = ["year", "corn_yield", "created_timestamp", "updated_timestamp"]
