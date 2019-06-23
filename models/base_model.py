from peewee import Model, SqliteDatabase
from pathlib import Path


dbhandle = SqliteDatabase(Path('db/inventory.db').resolve())


class BaseModel(Model):
    class Meta:
        database = dbhandle
