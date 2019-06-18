"""Setup of the tables data models
"""
from datetime import datetime

from peewee import (CharField, DateTimeField, IntegerField,
                    PrimaryKeyField,)
from models.basemodel import BaseModel


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
