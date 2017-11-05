
import peewee

from .base import Model


class Sport(Model):
    """Sport db model"""

    active = peewee.BooleanField(default=True, index=True)
    name = peewee.CharField(max_length=256, unique=True, index=True)

    class Meta:
        indexes = ((('active', 'name'), True), )


