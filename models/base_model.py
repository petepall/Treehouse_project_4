from peewee import Model, SqliteDatabase
from pathlib import Path


dbhandle = SqliteDatabase(Path.cwd().absolute() / 'db/inventory.db')


class BaseModel(Model):
    class Meta:
        database = dbhandle
