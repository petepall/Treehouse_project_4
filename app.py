import os
import sys

from models.base_model import dbhandle
from presentation.menu import StoreMenu
from utilities.constants import CSV_FILE_IMPORT, DB_FILE, DB_FOLDER, MENU
from utilities.db_processing import (
    backup_data, create_database, create_product, load_csv_data_in_database,
    view_product)
from utilities.helper_functions import (check_folder_exists, clear_screen,
                                        create_folder)

if __name__ == "__main__":
    dbhandle.connect()
    if not os.path.isfile(DB_FOLDER + DB_FILE):
        if check_folder_exists(DB_FOLDER):
            create_database()
        else:
            create_folder(DB_FOLDER)
            create_database()

    if os.path.isfile(CSV_FILE_IMPORT):
        load_csv_data_in_database(CSV_FILE_IMPORT)
    else:
        print(f"The {CSV_FILE_IMPORT} does not exist")
        try:
            input("Press the 'ENTER' key to continue")
        except KeyboardInterrupt:
            pass

    menu = StoreMenu()
    while True:
        clear_screen()
        selection = menu.menu(MENU, 'Store Inventory')
        if selection.lower() == 'q':
            print("Thank you for using the Store app, see you next time")
            dbhandle.close()
            sys.exit(1)
        elif selection.lower() == 'a':
            create_product()
        elif selection.lower() == 'v':
            view_product()
        elif selection.lower() == 'b':
            backup_data()
        else:
            try:
                input(f"{selection}\nPress 'ENTER' to continue")
            except KeyboardInterrupt:
                pass
            continue
