"""Setup of the tables data models
"""
from datetime import date

from peewee import (CharField, DateField, IntegerField,
                    AutoField, IntegrityError, EXCLUDED)
from models.basemodel import BaseModel


class Product(BaseModel):
    """Class representing the product table in the database

    Parameters
    ----------
    BaseModel : Model
        Inherits the database connection handling
    """
    product_id = AutoField()
    product_name = CharField(max_length=255, unique=True)
    product_quantity = IntegerField(default=0)
    product_price = IntegerField(default=0)
    date_updated = DateField(default=date.today())

    class Meta:
        db_table = "products"
        order_by = ("product_id",)


def load_data_to_database(csv_data, table):
    for row in csv_data:
        try:
            table.create(
                product_name=row['product_name'],
                product_quantity=row['product_quantity'],
                product_price=row['product_price'],
                date_updated=row['date_updated']
            )
        except IntegrityError:
            product = table.get(product_name=row['product_name'])
            if row['date_updated'] > product.date_updated:
                product.product_quantity = row['product_quantity']
                product.product_price = row['product_price']
                product.date_updated = row['date_updated']
                product.save()
