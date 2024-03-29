from datetime import date

from peewee import AutoField, CharField, DateField, IntegerField

from models.base_model import BaseModel


class Product(BaseModel):
    """Class representing a product

    Parameters
    ----------
    BaseModel : Model
        Base model handling the connection
    """

    product_id = AutoField()  # automatically is a primary key
    product_name = CharField(max_length=255, unique=True)
    product_quantity = IntegerField(default=0, null=False)
    product_price = IntegerField(default=0, null=False)
    date_updated = DateField(null=False, default=date.today())

    class Meta:
        db_table = "products"
        order_by = ("date_updated",)
