"""Store Inventory application

Function:
    Import and convert initial data and allow for adding new product data
"""
from helper_modules.clear_screen import clear_screen
from peewee import InternalError
from models.product import Product, dbhandle


if __name__ == "__main__":
    # handle the database connection and when required create the table
    try:
        dbhandle.connect()
        dbhandle.create_tables([Product], safe=True)
    except InternalError as err:
        print(str(err))

    clear_screen()
