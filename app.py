import os

from peewee import InternalError

from models.base_model import dbhandle
from models.product import Product
from utilities.constants import CSV_FILE_IMPORT, DB_FILE, DB_FOLDER
from utilities.csv_processing import clean_csv_data, read_from_csv
from utilities.db_processing import write_rows_to_db
from utilities.helper_functions import (check_folder_exists, clear_screen,
                                        create_folder)


def create_database():
    try:
        dbhandle.connect()
        Product.create_table(safe=True)
        dbhandle.close()
    except InternalError as err:
        print(str(err))


def load_csv_data_in_database():
    loaded_csv = read_from_csv(CSV_FILE_IMPORT)
    csv_data = clean_csv_data(loaded_csv)
    dbhandle.connect()
    write_rows_to_db(csv_data)
    dbhandle.close()


if __name__ == "__main__":
    if not os.path.isfile((DB_FOLDER + DB_FILE)):
        if check_folder_exists(DB_FOLDER):
            create_database()
        else:
            create_folder(DB_FOLDER)
            create_database()

    if os.path.isfile(CSV_FILE_IMPORT):
        load_csv_data_in_database()
    else:
        print(f"The {CSV_FILE_IMPORT} does not exist")
        input("Press the 'ENTER' key to continue")

    clear_screen()
