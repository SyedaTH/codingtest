from django.db import models

from coding_test.commons.constants import MISSING_VALUE
from coding_test.commons.models import BaseModel


"""
    Weather model stores data collected every day from stations.
"""


class Weather(BaseModel):
    station_id = models.CharField(
        max_length=20)
    date = models.DateField()
    max_temp = models.FloatField(
        default=MISSING_VALUE,
    )
    min_temp = models.FloatField(
        default=MISSING_VALUE,
    )
    precipitation = models.FloatField(
        default=MISSING_VALUE,
    )

    class Meta:
        unique_together = [
            "station_id",
            "date",
        ]

