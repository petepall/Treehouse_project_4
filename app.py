"""Store Inventory application

Function:
    Import and convert initial data and allow for adding new product data
"""
import os
from pathlib import Path

from peewee import InternalError

from helper_modules.clear_screen import clear_screen
from helper_modules.data_processing import clean_data
from models.basemodel import dbhandle
from models.product import Product, load_data_to_database


def create_database():
    try:
        dbhandle.connect()
        dbhandle.create_tables([Product], safe=True)
    except InternalError as err:
        print(str(err))

    dbhandle.close()


if __name__ == "__main__":
    # Check if the database exists, if not create the database and tables
    if not os.path.isfile(f"{Path().absolute()}\\database\\inventory.db"):
        create_database()

    date_to_load = clean_data()
    dbhandle.connect()
    load_data_to_database(date_to_load, Product)
    dbhandle.close()

    # clear_screen()
