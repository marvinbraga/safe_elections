import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class IdTimeStampedModel(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        get_latest_by = "modified"
        abstract = True
