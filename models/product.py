"""Setup of the tables data models
"""
from datetime import datetime
from pathlib import Path

from peewee import (CharField, DateTimeField, IntegerField, Model,
                    PrimaryKeyField, SqliteDatabase)

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


class Product(BaseModel):
    """Class representing the product table in the database

    Parameters
    ----------
    BaseModel : Model
        Inherits the database connection handling
    """
    product_id = PrimaryKeyField(primary_key=True, null=False, unique=True)
    product_name = CharField(50)
    product_quantity = IntegerField(default=0)
    product_price = IntegerField(default=0)
    date_updated = DateTimeField(default=datetime.now())

    class Meta:
        db_table = "products"
        order_by = ("product_id",)
