import datetime
import uuid

import peewee
from playhouse.shortcuts import model_to_dict

from ..settings import pool


class Model(peewee.Model):
    """Common db model"""

    uid = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    uts = peewee.DateTimeField(default=datetime.datetime.now, index=True)

    class Meta:
        database = pool
        order_by = ('-uts', )

    def to_dict(self):
        return model_to_dict(self, exclude=(type(self).uts,))