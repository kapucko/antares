from ..settings import manager, pool
from .sport import Sport


def setup_tables():
    tables = (Sport,)
    with manager.allow_sync():
        pool.create_tables(tables, safe=True)