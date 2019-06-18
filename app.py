"""Store Inventory application

Function:
    Import and convert initial data and allow for adding new product data
"""
from peewee import InternalError

from helper_modules.clear_screen import clear_screen
from models.basemodel import dbhandle
from models.product import Product

if __name__ == "__main__":
    # handle the database connection and when required create the table
    try:
        dbhandle.connect()
        dbhandle.create_tables([Product], safe=True)
    except InternalError as err:
        print(str(err))

    clear_screen()
