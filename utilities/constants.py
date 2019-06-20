from pathlib import Path
from collections import OrderedDict


DB_FOLDER = f"{Path().absolute()}\\db\\"
DB_FILE = "inventory.db"
CSV_FILE_IMPORT = f"{Path().absolute()}\\import_data\\inventory.csv"
CSV_FOLDER_EXPORT = f"{Path().absolute()}\\archive\\"
CSV_FILE_EXPORT = "backup.csv"
MENU = OrderedDict([
    ('a', 'Add product'),
    ('v', 'View selected product'),
    ('b', 'Export data in csv format'),
    ('q', 'QUIT the App')
])
