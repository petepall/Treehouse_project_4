"""Base model that handles the database handling.
"""
from pathlib import Path

from peewee import Model, SqliteDatabase

dbhandle = SqliteDatabase(f'{Path().absolute()}//database//inventory.db')


# reference from http://blog.adnansiddiqi.me/develop-database-driven-applications-in-python-with-peewee/
class BaseModel(Model):
    """Base class that handles the database connection data

    Parameters
    ----------
    Model : Model
        Peewee ORM base model from which all models start. This resolves
        redundancy for handling the database handle
    """
    class Meta:
        database = dbhandle
