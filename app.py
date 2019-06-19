import os
from pathlib import Path

from peewee import InternalError

from models.base_model import dbhandle
from models.product import Product
from utilities.csv_processing import clean_csv_data, read_from_csv
from utilities.db_processing import write_rows_to_db
from utilities.helper_functions import clear_screen

DB_FILE = f"{Path().absolute()}\\db\\inventory.db"
CSV_FILE = f"{Path().absolute()}\\import_data\\inventory.csv"


def create_database():
    try:
        dbhandle.connect()
        Product.create_table(safe=True)
        dbhandle.close()
    except InternalError as err:
        print(str(err))


def load_csv_data_in_database():
    loaded_csv = read_from_csv(CSV_FILE)
    csv_data = clean_csv_data(loaded_csv)
    dbhandle.connect()
    write_rows_to_db(csv_data)
    dbhandle.close()


if __name__ == "__main__":
    if not os.path.isfile(DB_FILE):
        create_database()

    if os.path.isfile(CSV_FILE):
        load_csv_data_in_database()
    else:
        print(f"The {CSV_FILE} does not exist")

    clear_screen()