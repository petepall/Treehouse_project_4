import os
import sys

from models.base_model import dbhandle
from presentation.menu import StoreMenu
from utilities.constants import (CSV_FILE_EXPORT, CSV_FILE_IMPORT,
                                 CSV_FOLDER_EXPORT, DB_FILE, DB_FOLDER, MENU)
from utilities.db_processing import (
    backup_data, create_database, create_product, load_csv_data_in_database,
    view_product)
from utilities.helper_functions import (check_folder_exists, clear_screen,
                                        create_folder, product_search_input,
                                        wait_for_enter)

if __name__ == "__main__":
    if not os.path.isfile(DB_FOLDER + DB_FILE):
        if check_folder_exists(DB_FOLDER):
            dbhandle.connect()
            create_database()
        else:
            create_folder(DB_FOLDER)
            dbhandle.connect()
            create_database()

    if os.path.isfile(CSV_FILE_IMPORT):
        load_csv_data_in_database(CSV_FILE_IMPORT)
    else:
        print(f"The {CSV_FILE_IMPORT} does not exist")
        wait_for_enter()

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
            wait_for_enter("\nYour entry is saved")
        elif selection.lower() == 'v':
            product_id = product_search_input()
            view_product(product_id)
            wait_for_enter()
        elif selection.lower() == 'b':
            if not check_folder_exists(CSV_FOLDER_EXPORT + CSV_FILE_EXPORT):
                create_folder(CSV_FOLDER_EXPORT)
            print(CSV_FOLDER_EXPORT + CSV_FILE_EXPORT)
            wait_for_enter(backup_data(CSV_FOLDER_EXPORT + CSV_FILE_EXPORT))
        else:
            wait_for_enter(selection)
            continue
