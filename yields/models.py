from bulk_update_or_create import BulkUpdateOrCreateQuerySet
from django.db import models

from coding_test.commons.models import BaseModel

"""
    Yields model is used to store crop yield data in the United States by year
"""


class YieldsData(BaseModel):

    year = models.PositiveSmallIntegerField(
        unique=True
    )
    corn_yield = models.IntegerField(
    )

    objects = BulkUpdateOrCreateQuerySet.as_manager()
